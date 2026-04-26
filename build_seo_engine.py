import os
import json
import yaml
import re
from collections import defaultdict

# =========================
# CONFIG
# =========================

INPUT_FILE = "_data/articles.yml"
OUTPUT_LINKED = "_data/articles-linked.yml"
POSTS_DIR = "_posts"

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
# UTIL
# =========================

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")

# =========================
# SAFE LOAD
# =========================

def load_articles():
    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(INPUT_FILE)

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw = f.read().strip()

    if not raw:
        raise ValueError("Empty input file")

    try:
        data = yaml.safe_load(raw)
        if isinstance(data, list):
            return data
    except:
        pass

    return json.loads(raw)

# =========================
# INDEX
# =========================

def index_articles(articles):
    by_cluster = defaultdict(list)
    by_funnel = defaultdict(list)

    for a in articles:
        by_cluster[a.get("cluster", "base")].append(a)
        by_funnel[a.get("funnel", "tofu")].append(a)

    return by_cluster, by_funnel

# =========================
# INTERNAL LINKS
# =========================

def pick_links(article, by_cluster, by_funnel):
    cluster = article.get("cluster", "base")
    funnel = article.get("funnel", "tofu")

    links = []
    seen = set()

    def add(items):
        for i in items:
            if not isinstance(i, dict):
                continue
            uid = i.get("id")
            if not uid or uid in seen or uid == article.get("id"):
                continue
            links.append(i)
            seen.add(uid)

    add(by_cluster.get(cluster, [])[:3])

    for c in CLUSTER_LINKS.get(cluster, []):
        add(by_cluster.get(c, [])[:1])

    current = FUNNEL_PRIORITY.get(funnel, 1)
    for f, lvl in FUNNEL_PRIORITY.items():
        if lvl > current:
            add(by_funnel.get(f, [])[:1])
            break

    add(by_funnel.get("bofu", [])[:1])

    return links[:6]

# =========================
# INCLUDES SYSTEM
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
# ARTICLE GENERATOR
# =========================

def generate_article(article):
    title = article.get("title", "Untitled")
    layout = article.get("include_layout", {})

    body = article.get("ai_body") or f"Contenuto generato per {title}"

    content = f"# {title}\n\n"

    for b in layout.get("after_intro", []):
        content += f"{{% include {b} %}}\n\n"

    for b in layout.get("after_h1", []):
        content += f"{{% include {b} %}}\n\n"

    content += "## Contenuto principale\n\n"
    content += body + "\n\n"

    for b in layout.get("mid_article", []):
        content += f"{{% include {b} %}}\n\n"

    content += "## Conclusione\n\n"

    for b in layout.get("before_cta", []):
        content += f"{{% include {b} %}}\n\n"

    for b in layout.get("footer", []):
        content += f"{{% include {b} %}}\n\n"

    return content

# =========================
# MARKDOWN EXPORT (🔥 AUTOPUBLISH CORE)
# =========================

def export_markdown(article):
    os.makedirs(POSTS_DIR, exist_ok=True)

    title = article.get("title", "untitled")
    slug = slugify(title)

    path = f"{POSTS_DIR}/{slug}.md"

    content = article["final_article"]

    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"title: \"{title}\"\n")
        f.write(f"permalink: /{slug}/\n")
        f.write("---\n\n")
        f.write(content)

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

        a["include_layout"] = assign_include_layout(a)

        a["final_article"] = generate_article(a)

        # 🔥 AUTOPUBLISH STEP
        export_markdown(a)

        output.append(a)

    return output

# =========================
# SAVE YAML
# =========================

def save_yaml(data):
    os.makedirs(os.path.dirname(OUTPUT_LINKED), exist_ok=True)

    with open(OUTPUT_LINKED, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)

# =========================
# MAIN
# =========================

def main():
    articles = load_articles()

    output = build_output(articles)

    save_yaml(output)

    print("🚀 AUTOPUBLISH COMPLETATO")

if __name__ == "__main__":
    main()
