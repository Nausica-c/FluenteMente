import os
import yaml
from collections import defaultdict

# =========================
# CONFIG
# =========================

INPUT_FILE = "_data/keywords.yml"
OUTPUT_FILE = "_data/articles-linked.yml"

CLUSTERS = {
    "base": ["travel", "social"],
    "travel": ["expat", "social"],
    "social": ["expat", "business"],
    "expat": ["business", "method"],
    "business": ["method"],
    "culture": ["social"],
    "method": ["bofu"]
}

FUNNEL_ORDER = {
    "tofu": 1,
    "mofu": 2,
    "bofu": 3
}

# =========================
# LOAD KEYWORDS
# =========================

def load_keywords():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# =========================
# AI ARTICLE GENERATION (SIMULATED CORE)
# =========================

def generate_article_text(item):
    keyword = item["keyword"]

    return f"""
## Introduzione

Se vuoi capire {keyword}, sei nel posto giusto.

## Spiegazione semplice

{keyword} è una situazione reale che incontri spesso nella vita quotidiana.

## Esempi pratici

- esempio 1 con {keyword}
- esempio 2 con {keyword}
- esempio 3 con {keyword}

## Conclusione

Ora sai come gestire {keyword} nella vita reale.
"""

# =========================
# INCLUDE ENGINE
# =========================

def generate_includes(item):
    cluster = item.get("cluster")
    funnel = item.get("funnel")

    includes = {
        "after_intro": ["tldr-box.html"],
        "mid_article": [],
        "before_cta": [],
        "footer": ["trust-box.html"]
    }

    if cluster == "travel":
        includes["mid_article"].append("orient-box.html")

    if cluster == "expat":
        includes["mid_article"].append("bridge-box.html")

    if funnel == "bofu":
        includes["before_cta"].append("promo-box.html")

    return includes

# =========================
# INTERNAL LINKING ENGINE
# =========================

def build_links(article, all_articles):
    cluster = article["cluster"]
    funnel = article["funnel"]

    links = []

    for a in all_articles:
        if a["cluster"] == cluster and a["keyword"] != article["keyword"]:
            links.append(a)

    for a in all_articles:
        if FUNNEL_ORDER.get(a["funnel"], 1) > FUNNEL_ORDER.get(funnel, 1):
            links.append(a)

    return links[:5]

# =========================
# ARTICLE BUILDER
# =========================

def build_article(item, all_articles):

    article = {
        "title": item["keyword"].title(),
        "cluster": item["cluster"],
        "funnel": item["funnel"],
        "url": f"/{item['keyword'].replace(' ', '-')}/"
    }

    article["ai_body"] = generate_article_text(item)
    article["include_layout"] = generate_includes(item)
    article["internal_links"] = build_links(item, all_articles)

    # FINAL ARTICLE
    article["final_article"] = render_article(article)

    return article

# =========================
# RENDER ENGINE
# =========================

def render_article(article):

    content = f"# {article['title']}\n\n"

    content += "## Introduzione\n\n"

    for box in article["include_layout"]["after_intro"]:
        content += f"{{% include {box} %}}\n\n"

    content += article["ai_body"] + "\n"

    for box in article["include_layout"]["mid_article"]:
        content += f"{{% include {box} %}}\n\n"

    content += "## Conclusione\n\n"

    for box in article["include_layout"]["before_cta"]:
        content += f"{{% include {box} %}}\n\n"

    content += "## Migliora il tuo inglese\n\n"
    content += "Scopri il metodo FluenteMente per parlare inglese davvero.\n\n"

    for box in article["include_layout"]["footer"]:
        content += f"{{% include {box} %}}\n\n"

    return content

# =========================
# PIPELINE
# =========================

def main():

    keywords = load_keywords()
    articles = []

    for item in keywords:
        article = build_article(item, articles)
        articles.append(article)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml.dump(articles, f, allow_unicode=True, sort_keys=False)

    print("🚀 V2 BLOG ENGINE COMPLETE")

if __name__ == "__main__":
    main()
