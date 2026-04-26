import yaml
import re
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
# SAFE LOAD YAML
# =========================

def load_articles():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# =========================
# GROUP BY CLUSTER / FUNNEL
# =========================

def index_articles(articles):
    by_cluster = defaultdict(list)
    by_funnel = defaultdict(list)

    for a in articles:
        if not isinstance(a, dict):
            continue
        if "cluster" in a:
            by_cluster[a["cluster"]].append(a)
        if "funnel" in a:
            by_funnel[a["funnel"]].append(a)

    return by_cluster, by_funnel

# =========================
# INTERNAL LINK SELECTOR
# =========================

def pick_links(article, by_cluster, by_funnel):
    cluster = article.get("cluster")
    funnel = article.get("funnel")

    links = []

    # 1. stesso cluster
    same_cluster = by_cluster.get(cluster, [])
    links += same_cluster[:3]

    # 2. funnel successivo
    current_level = FUNNEL_PRIORITY.get(funnel, 1)
    for f, level in FUNNEL_PRIORITY.items():
        if level > current_level:
            links += by_funnel.get(f, [])[:1]
            break

    # 3. metodo (conversione)
    for a in by_funnel.get("bofu", []):
        if a.get("cluster") == "method":
            links.append(a)
            break

    # remove self duplicates
    seen = set()
    clean = []
    for l in links:
        uid = l.get("id")
        if uid and uid not in seen:
            clean.append(l)
            seen.add(uid)

    return clean[:5]

# =========================
# BUILD OUTPUT SAFE YAML
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

        output.append(a)

    return output

# =========================
# SAFE WRITE (FIX YAML CRASH)
# =========================

def save_yaml(data):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml.safe_dump(
            data,
            f,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False
        )

# =========================
# VALIDATION (ANTI-CRASH)
# =========================

def validate(data):
    for i, a in enumerate(data):
        if "id" not in a:
            raise ValueError(f"Missing id at index {i}")
        if "title" not in a:
            raise ValueError(f"Missing title at id {a.get('id')}")
        if "url" not in a:
            raise ValueError(f"Missing url at id {a.get('id')}")

# =========================
# RUN
# =========================

def main():
    articles = load_articles()

    if not isinstance(articles, list):
        raise ValueError("articles.yml must be a LIST at root level")

    validate(articles)

    output = build_output(articles)
    save_yaml(output)

    print("✅ _articles-linked.yml generated successfully")

if __name__ == "__main__":
    main()
