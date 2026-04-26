import os
import yaml
import re
import random
import hashlib
from datetime import datetime

# =========================
# CONFIG
# =========================

INPUT_FILE = "_data/articles.yml"
OUTPUT_LINKED = "_data/articles-linked.yml"
POSTS_DIR = "_posts"

# =========================
# UTILS
# =========================

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")

def today():
    return datetime.now().strftime("%Y-%m-%d")

def hash_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

# =========================
# LOAD ARTICLES
# =========================

def load_articles():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []

# =========================
# CONTENT GENERATION (NO AI COMPLEXITY)
# =========================

def generate_body(article):
    title = article.get("title", "")
    cluster = article.get("cluster", "base")
    funnel = article.get("funnel", "tofu")

    seed = article.get("seed") or random.randint(1000, 9999)
    random.seed(seed)

    return f"""
## Introduzione
Guida pratica su {title} con esempi reali.

## Cos’è
Spiegazione semplice e immediata.

## Esempi pratici
- esempio 1
- esempio 2
- esempio 3
- esempio 4
- esempio 5

## Errori comuni
Errori tipici italiani.

## Uso nella vita reale
Situazioni: viaggio, lavoro, expat.

---
SEED: {seed}
CLUSTER: {cluster}
FUNNEL: {funnel}
""".strip()

# =========================
# BUILD ARTICLE
# =========================

def build_article(article):
    body = generate_body(article)
    return f"# {article.get('title','Untitled')}\n\n{body}\n"

# =========================
# EXPORT SAFE (NO REGEN IF SAME)
# =========================

def export_post(article, content):
    os.makedirs(POSTS_DIR, exist_ok=True)

    slug = slugify(article.get("title", "untitled"))
    path = f"{POSTS_DIR}/{today()}-{slug}.md"

    new_hash = hash_text(content)

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            old = f.read()
        if hash_text(old) == new_hash:
            print(f"SKIP {slug}")
            return

    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"title: \"{article['title']}\"\n")
        f.write(f"permalink: /{slug}/\n")
        f.write("layout: post\n")
        f.write(f"content_hash: {new_hash}\n")
        f.write("---\n\n")
        f.write(content)

    print(f"UPDATED {slug}")

# =========================
# PIPELINE
# =========================

def build():
    articles = load_articles()
    output = []

    for a in articles:
        a["cluster"] = a.get("cluster", "base")
        a["funnel"] = a.get("funnel", "tofu")

        content = build_article(a)

        export_post(a, content)

        a["final_article"] = content
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
    output = build()
    save_yaml(output)
    print("V0 CLEAN ENGINE COMPLETE")

if __name__ == "__main__":
    main()
