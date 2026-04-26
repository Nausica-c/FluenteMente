import os
import json
import yaml
import re
import hashlib
import random
from datetime import datetime
from collections import defaultdict

# =========================
# CONFIG
# =========================

INPUT_FILE = "_data/articles.yml"
OUTPUT_LINKED = "_data/articles-linked.yml"
POSTS_DIR = "_posts"

# =========================
# UTIL
# =========================

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")

def today_date():
    return datetime.now().strftime("%Y-%m-%d")

def hash_content(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()

# =========================
# LOAD DATA
# =========================

def load_articles():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data if isinstance(data, list) else []

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
# LINKS (SIMPLE + SAFE)
# =========================

def pick_links(article, by_cluster):
    cluster = article.get("cluster", "base")

    candidates = by_cluster.get(cluster, [])
    links = []

    for c in candidates:
        if c.get("id") != article.get("id"):
            links.append({
                "title": c.get("title"),
                "url": c.get("url", "#")
            })

    return links[:5]

# =========================
# CONTENT ENGINE (STABLE)
# =========================

def generate_body(article):
    title = article.get("title", "")
    cluster = article.get("cluster", "base")
    funnel = article.get("funnel", "tofu")

    seed = article.get("seed") or random.randint(1000, 9999)
    random.seed(seed)

    return f"""
## Introduzione
Guida pratica su {title}.

## Cos’è
Spiegazione semplice e chiara del concetto.

## Esempi pratici
- esempio reale 1
- esempio reale 2
- esempio reale 3
- esempio reale 4
- esempio reale 5

## Errori comuni
Attenzione agli errori tipici degli italiani.

## Uso nella vita reale
Situazioni: viaggio, lavoro, vita quotidiana.

---
SEED: {seed}
CLUSTER: {cluster}
FUNNEL: {funnel}
""".strip()

# =========================
# ARTICLE BUILDER
# =========================

def build_article(article, links):
    title = article.get("title", "Untitled")

    body = generate_body(article)

    content = f"# {title}\n\n"
    content += body + "\n\n"

    if links:
        content += "## Articoli correlati\n\n"
        for l in links:
            content += f"- [{l['title']}]({l['url']})\n"

    return content

# =========================
# EXPORT (NO REGEN IF NOT CHANGED)
# =========================

def export_post(article, content):

    os.makedirs(POSTS_DIR, exist_ok=True)

    slug = slugify(article.get("title", "untitled"))
    path = f"{POSTS_DIR}/{today_date()}-{slug}.md"

    new_hash = hash_content(content)

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            old = f.read()

        if hash_content(old) == new_hash:
            print(f"⏭ SKIP {slug}")
            return

    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"title: \"{article['title']}\"\n")
        f.write(f"permalink: /{slug}/\n")
        f.write("layout: post\n")
        f.write(f"content_hash: {new_hash}\n")
        f.write("---\n\n")
        f.write(content)

    print(f"✔ UPDATED {slug}")

# =========================
# PIPELINE
# =========================

def build_output(articles):

    by_cluster, by_funnel = index_articles(articles)

    output = []

    for a in articles:
        a["cluster"] = a.get("cluster", "base")
        a["funnel"] = a.get("funnel", "tofu")

        if not a.get("seed"):
            a["seed"] = random.randint(1000, 9999)

        links = pick_links(a, by_cluster)

        content = build_article(a, links)

        export_post(a, content)

        a["final_article"] = content
        a["internal_links"] = links

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
    print("🚀 V1 CLEAN SYSTEM ACTIVE")

if __name__ == "__main__":
    main()
