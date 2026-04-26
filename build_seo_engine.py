import os
import json
import yaml
from collections import defaultdict

# =========================
# CONFIG
# =========================

INPUT_FILE = "_data/articles.yml"
OUTPUT_FILE = "_data/articles-linked.yml"

CLUSTER_LINKS = {
    "base": ["travel", "social"],
    "travel": ["expat", "social"],
    "social": ["expat", "business"],
    "expat": ["business", "method"],
    "business": ["method"],
    "culture": ["social", "business"],
    "method": ["bofu"],
}

FUNNEL_PRIORITY = {
    "tofu": 1,
    "mofu": 2,
    "bofu": 3
}

# =========================
# SAFE LOAD
# =========================

def load_articles():
    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(f"Missing input file: {INPUT_FILE}")

    if os.path.getsize(INPUT_FILE) == 0:
        raise ValueError("Input file is EMPTY (0 bytes)")

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw = f.read().strip()

        if not raw:
            raise ValueError("Input file is blank")

        try:
            data = yaml.safe_load(raw)
            if data is not None:
                return data
        except Exception:
            pass

        try:
            return json.loads(raw)
        except Exception as e:
            raise ValueError(f"File is neither valid YAML nor JSON: {e}")

# =========================
# INDEXING
# =========================

def index_articles(articles):
    by_cluster = defaultdict(list)
    by_funnel = defaultdict(list)

    for a in articles:
        if not isinstance(a, dict):
            continue

        cluster = a.get("cluster")
        funnel = a.get("funnel")

        if cluster:
            by_cluster[cluster].append(a)
        if funnel:
            by_funnel[funnel].append(a)

    return by_cluster, by_funnel

# =========================
# INTERNAL LINK ENGINE
# =========================

def pick_links(article, by_cluster, by_funnel):
    cluster = article.get("cluster")
    funnel = article.get("funnel")
    links = []

    # same cluster
    links += by_cluster.get(cluster, [])[:3]

    # cross cluster
    for target in CLUSTER_LINKS.get(cluster, []):
        links += by_cluster.get(target, [])[:1]

    # funnel progression
    current_level = FUNNEL_PRIORITY.get(funnel, 1)
    for f, level in FUNNEL_PRIORITY.items():
        if level > current_level:
            links += by_funnel.get(f, [])[:1]
            break

    # BOFU boost
    links += by_funnel.get("bofu", [])[:1]

    # dedupe
    seen = set()
    clean = []

    for l in links:
        if not isinstance(l, dict):
            continue

        if l.get("id") == article.get("id"):
            continue

        uid = l.get("id")
        if uid and uid not in seen:
            clean.append(l)
            seen.add(uid)

    return clean[:6]

# =========================
# INCLUDE ENGINE (NEW)
# =========================

def assign_include_layout(article):
    cluster = article.get("cluster")
    funnel = article.get("funnel")

    layout = {
        "after_intro": ["tldr-box.html"],
        "after_h1": ["section-in-breve.html"],
        "mid_article": [],
        "before_cta": [],
        "footer": ["trust-box.html"]
    }

    if funnel == "bofu":
        layout["before_cta"].append("promo-box.html")
        layout["footer"].append("affiliate-disclosure.html")

    if cluster == "expat":
        layout["mid_article"].append("bridge-box.html")

    if cluster == "travel":
        layout["mid_article"].append("orient-box.html")

    return layout

# =========================
# ARTICLE GENERATOR (NEW)
# =========================

def generate_article(article):

    title = article.get("title", "")
    layout = article.get("include_layout", {})

    content = f"# {title}\n\n"

    # intro includes
    for box in layout.get("after_intro", []):
        content += f"{{% include {box} %}}\n\n"

    # after H1 includes
    for box in layout.get("after_h1", []):
        content += f"{{% include {box} %}}\n\n"

    # body placeholder (future AI integration point)
    content += "## Contenuto principale\n\n"
    content += article.get("ai_body", "CONTENUTO GENERATO DA AI QUI") + "\n\n"

    # mid includes
    for box in layout.get("mid_article", []):
        content += f"{{% include {box} %}}\n\n"

    # CTA includes
    for box in layout.get("before_cta", []):
        content += f"{{% include {box} %}}\n\n"

    # footer includes
    for box in layout.get("footer", []):
        content += f"{{% include {box} %}}\n\n"

    return content

# =========================
# BUILD OUTPUT
# =========================

def build_output(articles):
    by_cluster, by_funnel = index_articles(articles)

    output = []

    for a in articles:
        if not isinstance(a, dict):
            continue

        linked = pick_links(a, by_cluster, by_funnel)

        a["internal_links"] = [
            {
                "title": x.get("title"),
                "url": x.get("url"),
                "cluster": x.get("cluster"),
                "funnel": x.get("funnel")
            }
            for x in linked
        ]

        # include system
        a["include_layout"] = assign_include_layout(a)

        # article generation
        a["final_article"] = generate_article(a)

        output.append(a)

    return output

# =========================
# SAVE
# =========================

def save_yaml(data):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml.safe_dump(
            data,
            f,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False
        )

# =========================
# VALIDATION
# =========================

def validate(data):
    if not isinstance(data, list):
        raise ValueError("Root must be a LIST of articles")

    for i, a in enumerate(data):
        if not isinstance(a, dict):
            raise ValueError(f"Invalid article at index {i}")

        for field in ["id", "title", "url"]:
            if field not in a:
                raise ValueError(f"Missing {field} in article id={a.get('id')}")

# =========================
# MAIN
# =========================

def main():
    articles = load_articles()
    validate(articles)

    output = build_output(articles)
    save_yaml(output)

    print("✅ _data/articles-linked.yml generated successfully")

if __name__ == "__main__":
    main()
