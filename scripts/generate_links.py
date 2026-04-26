import yaml
from collections import defaultdict

# =========================
# LOAD ARTICLES
# =========================
with open("_data/articles.yml", "r", encoding="utf-8") as f:
    articles = yaml.safe_load(f)

# =========================
# INDEXING
# =========================
by_cluster = defaultdict(list)
by_funnel = defaultdict(list)
by_id = {}

for a in articles:
    by_cluster[a["cluster"]].append(a)
    by_funnel[a["funnel"]].append(a)
    by_id[a["id"]] = a

# =========================
# HUB MAP
# =========================
def get_hub(article):
    if article["id"] in [1, 2, 20]:
        return 1
    if article["cluster"] == "method":
        return 81
    if article["cluster"] == "monetization":
        return 88
    return 1

# =========================
# SAME CLUSTER LINKS
# =========================
def same_cluster_links(article, limit=3):
    cluster_items = by_cluster[article["cluster"]]
    return [
        a["id"] for a in cluster_items
        if a["id"] != article["id"]
    ][:limit]

# =========================
# CROSS CLUSTER LOGIC
# =========================
def cross_links(article):
    cluster = article["cluster"]

    if cluster == "viaggio":
        return [31, 41, 3]

    if cluster == "expat":
        return [3, 61, 81]

    if cluster == "business":
        return [31, 1, 81]

    if cluster == "base":
        return [1, 81]

    if cluster == "method":
        return [1, 88]

    return [1]

# =========================
# FUNNEL FLOW
# =========================
def funnel_next(article):
    if article["funnel"] == "tofu":
        return [a["id"] for a in articles if a["funnel"] == "mofu" and a["cluster"] == article["cluster"]][:1]

    if article["funnel"] == "mofu":
        return [81, 88]

    return [88]

# =========================
# BUILD OUTPUT
# =========================
linked = []

for a in articles:

    linked_article = {
        **a,
        "internal_links": {
            "hub": [get_hub(a)],
            "same_cluster": same_cluster_links(a),
            "cross_cluster": cross_links(a),
            "funnel_next": funnel_next(a)
        }
    }

    linked.append(linked_article)

# =========================
# SAVE FILE
# =========================
with open("_articles-linked.yml", "w", encoding="utf-8") as f:
    yaml.dump(linked, f, allow_unicode=True, sort_keys=False)

print("✅ _articles-linked.yml generato con successo")
