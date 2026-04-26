import os
import json
import yaml
import random
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

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw = f.read().strip()

    if not raw:
        raise ValueError("Input file is empty")

    try:
        data = yaml.safe_load(raw)
        if isinstance(data, list):
            return data
    except Exception:
        pass

    try:
        data = json.loads(raw)
        if isinstance(data, list):
            return data
    except Exception as e:
        raise ValueError(f"Invalid YAML/JSON: {e}")

    raise ValueError("Root must be a LIST of articles")

# =========================
# INDEX
# =========================

def index_articles(articles):
    by_cluster = defaultdict(list)
    by_funnel = defaultdict(list)

    for a in articles:
        if not isinstance(a, dict):
            continue

        by_cluster[a.get("cluster", "base")].append(a)
        by_funnel[a.get("funnel", "tofu")].append(a)

    return by_cluster, by_funnel

# =========================
# LINK ENGINE (IMPROVED)
# =========================

def pick_links(article, by_cluster, by_funnel):
    cluster = article.get("cluster", "base")
    funnel = article.get("funnel", "tofu")

    links = []
    seen = set()

    def add(items):
        for i in items:
            uid = i.get("id")
            if not uid or uid in seen:
                continue
            if uid == article.get("id"):
                continue
            links.append(i)
            seen.add(uid)

    # 1. same cluster (strong relevance)
    add(by_cluster.get(cluster, [])[:3])

    # 2. cross cluster expansion
    for target in CLUSTER_LINKS.get(cluster, []):
        add(by_cluster.get(target, [])[:1])

    # 3. funnel progression
    current = FUNNEL_PRIORITY.get(funnel, 1)
    for f, lvl in FUNNEL_PRIORITY.items():
        if lvl > current:
            add(by_funnel.get(f, [])[:1])
            break

    # 4. BOFU conversion boost
    add(by_funnel.get("bofu", [])[:1])

    # 5. randomness anti-SEO footprint (IMPORTANT)
    random.shuffle(links)

    return links[:6]

# =========================
# INCLUDE ENGINE
# =========================

def assign_include_layout(article):
    cluster = article.get("cluster", "base")
    funnel = article.get("funnel", "tofu")

    layout = {
        "after_intro": ["tldr-box.html"],
        "after_h1": ["section-in-breve.html"],
        "mid_article": [],
        "before_cta": [],
        "footer": ["trust-box.html"]
    }

    if cluster == "travel":
        layout["mid_article"].append("orient-box.html")

    if cluster == "expat":
        layout["mid_article"].append("bridge-box.html")

    if funnel == "bofu":
        layout["before_cta"].append("promo-box.html")
        layout["footer"].append("affiliate-disclosure.html")

    return layout

# =========================
# AI CONTENT (BASIC ENGINE)
# =========================

def generate_ai_body(article):
    title = article.get("title", "Untitled")
    cluster = article.get("cluster", "base")

    return f"""
Introduzione a {title}.

Spiegazione semplice e pratica.

Contesto reale nel cluster {cluster}.

Errori comuni degli italiani.

Esempi pratici utilizzabili subito.
"""

# =========================
# ARTICLE BUILDER
# =========================

def generate_article(article):
    title = article.get("title", "Untitled")
    layout = article.get("include_layout", {})
    body = article.get("ai_body", "")

    content = f"# {title}\n\n"

    for box in layout.get("after_intro", []):
        content += f"{{% include {box} %}}\n\n"

    for box in layout.get("after_h1", []):
        content += f"{{% include {box} %}}\n\n"

    content += "## Contenuto principale\n\n"
    content += body + "\n\n"

    for box in layout.get("mid_article", []):
        content += f"{{% include {box} %}}\n\n"

    content += "## Conclusione\n\n"

    for box in layout.get("before_cta", []):
        content += f"{{% include {box} %}}\n\n"

    for box in layout.get("footer", []):
        content += f"{{% include {box} %}}\n\n"

    return content

# =========================
# BUILD PIPELINE
# =========================

def build_output(articles):
    by_cluster, by_funnel = index_articles(articles)

    output = []

    for a in articles:
        if not isinstance(a, dict):
            continue

        a["cluster"] = a.get("cluster", "base")
        a["funnel"] = a.get("funnel", "tofu")

        # links
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

        # includes
        a["include_layout"] = assign_include_layout(a)

        # AI body
        a["ai_body"] = generate_ai_body(a)

        # final article
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
        raise ValueError("Root must be a list")

    for i, a in enumerate(data):
        if not isinstance(a, dict):
            raise ValueError(f"Invalid item at index {i}")

        if not a.get("title"):
            raise ValueError(f"Missing title at index {i}")

# =========================
# MAIN
# =========================

def main():
    articles = load_articles()
    validate(articles)

    output = build_output(articles)
    save_yaml(output)

    print("🚀 articles-linked.yml generated successfully")

if __name__ == "__main__":
    main()
