import json
import yaml
from collections import defaultdict

INPUT_FILE = "data/articles.json"
OUTPUT_FILE = "_data/articles-linked.yml"


# =========================
# LOAD DATA
# =========================
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    articles = json.load(f)


# =========================
# INDEX BY CLUSTER / ROLE
# =========================
clusters = defaultdict(list)
hub_articles = []

for a in articles:
    clusters[a["cluster"]].append(a)
    if a["role"] == "hub":
        hub_articles.append(a)


# =========================
# BUILD INTERNAL LINKS
# =========================
def build_links(article):
    links = []

    # 1. SAME CLUSTER LINKS (SEO topical authority)
    same_cluster = clusters[article["cluster"]]

    for a in same_cluster:
        if a["id"] != article["id"]:
            links.append({
                "title": a["title"],
                "url": a["url"],
                "type": "cluster"
            })

    # 2. HUB BOOST (if not hub → link to hub)
    if article["role"] != "hub":
        for h in hub_articles:
            if h["cluster"] == article["cluster"]:
                links.append({
                    "title": h["title"],
                    "url": h["url"],
                    "type": "hub"
                })

    # 3. BOFU BOOST (if TOFU/MOFU → link to conversion pages)
    if article["funnel"] != "bofu":
        for a in articles:
            if a["funnel"] == "bofu":
                links.append({
                    "title": a["title"],
                    "url": a["url"],
                    "type": "bofu"
                })

    # limit links (avoid spam)
    return links[:8]


# =========================
# BUILD FINAL STRUCTURE
# =========================
output = []

for a in articles:
    new_article = dict(a)
    new_article["links"] = build_links(a)
    output.append(new_article)


# =========================
# SORT BY ID
# =========================
output.sort(key=lambda x: x["id"])


# =========================
# WRITE YAML SAFELY
# =========================
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    yaml.dump(
        output,
        f,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False
    )

print("✅ SEO ENGINE COMPLETED")
print(f"📦 Articles processed: {len(output)}")
