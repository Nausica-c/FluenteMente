import os
import json
import yaml
import re
import random
import hashlib
from datetime import datetime
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

def today_date():
    return datetime.now().strftime("%Y-%m-%d")

def compute_hash(content: str) -> str:
    return hashlib.md5(content.encode("utf-8")).hexdigest()

# =========================
# LOAD
# =========================

def load_articles():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw = f.read().strip()

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
# INCLUDE LAYOUT
# =========================

def assign_include_layout(article):
    cluster = article.get("cluster", "base")
    funnel = article.get("funnel", "tofu")

    return {
        "after_intro": ["tldr-box.html"],
        "after_h1": ["section-in-breve.html"],
        "mid_article": ["bridge-box.html"] if cluster == "expat" else [],
        "before_cta": ["promo-box.html"] if funnel == "bofu" else [],
        "footer": ["trust-box.html", "affiliate-disclosure.html"] if funnel == "bofu" else ["trust-box.html"]
    }

# =========================
# AI ENGINE (semplice stabile)
# =========================

def generate_ai_body(article):
    title = article.get("title", "")
    cluster = article.get("cluster", "")
    funnel = article.get("funnel", "")
    seed = random.randint(1000, 9999)

    return f"""
## Introduzione
Guida pratica su {title} con contesto reale.

## Cos’è
Spiegazione semplice e applicabile.

## Esempi pratici
- esempio 1 reale
- esempio 2 reale
- esempio 3 reale
- esempio 4 reale
- esempio 5 reale

## Errori comuni
- errori tipici italiani nell’uso

## Uso nella vita reale
Situazioni: viaggio, lavoro, vita quotidiana.

SEED: {seed}
CLUSTER: {cluster}
FUNNEL: {funnel}
""".strip()

# =========================
# ARTICLE BUILDER
# =========================

def generate_article(article):
    title = article.get("title", "Untitled")
    layout = article.get("include_layout", {})

    body = generate_ai_body(article)

    content = f"# {title}\n\n"

    for b in layout.get("after_intro", []):
        content += f"{{% include {b} %}}\n\n"

    for b in layout.get("after_h1", []):
        content += f"{{% include {b} %}}\n\n"

    content += body + "\n\n"

    for b in layout.get("mid_article", []):
        content += f"{{% include {b} %}}\n\n"

    if article.get("internal_links"):
        content += "## Articoli correlati\n\n"
        for l in article["internal_links"]:
            content += f"- [{l['title']}]({l['url']})\n"

    for b in layout.get("before_cta", []):
        content += f"\n{{% include {b} %}}\n"

    for b in layout.get("footer", []):
        content += f"\n{{% include {b} %}}\n"

    return content

# =========================
# EXPORT (FIX VERO)
# =========================

def export_markdown(article):

    os.makedirs(POSTS_DIR, exist_ok=True)

    slug = slugify(article.get("title", "untitled"))
    path = f"{POSTS_DIR}/{today_date()}-{slug}.md"

    content = article["final_article"]
    new_hash = compute_hash(content)

    # se esiste già, controlla se è cambiato
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            old_content = f.read()

        old_hash = compute_hash(old_content)

        if old_hash == new_hash:
            print(f"SKIP (unchanged): {slug}")
            return

    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"title: \"{article['title']}\"\n")
        f.write(f"permalink: /{slug}/\n")
        f.write("layout: post\n")
        f.write(f"content_hash: {new_hash}\n")
        f.write("---\n\n")
        f.write(content)

    print(f"UPDATED: {slug}")

# =========================
# PIPELINE
# =========================

def build_output(articles):
    by_cluster, by_funnel = index_articles(articles)

    output = []

    for a in articles:
        a["cluster"] = a.get("cluster", "base")
        a["funnel"] = a.get("funnel", "tofu")

        a["internal_links"] = pick_links(a, by_cluster, by_funnel)
        a["include_layout"] = assign_include_layout(a)

        a["final_article"] = generate_article(a)

        export_markdown(a)

        output.append(a)

    return output

# =========================
# SAVE YAML
# =========================

def save_yaml(data):
    with open(OUTPUT_LINKED, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)

# =========================
# MAIN
# =========================

def main():
    articles = load_articles()
    output = build_output(articles)
    save_yaml(output)
    print("🚀 FIX 1 ENGINE ACTIVE (STABLE MODE)")

if __name__ == "__main__":
    main()
