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
# SAFE LOAD (FIX CRASH ROOT CAUSE)
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

        # YAML FIRST (your real format)
        try:
            data = yaml.safe_load(raw)
            if data is not None:
                return data
        except Exception:
            pass

        # JSON fallback
        try:
            return json.loads(raw)
        except Exception as e:
            raise ValueError(f"File is neither valid YAML nor JSON: {e}")

# =========================
# INDEX
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

    # 1. same cluster (high relevance)
    links += by_cluster.get(cluster, [])[:3]

    # 2. cross cluster strategy
    for target in CLUSTER_LINKS.get(cluster, []):
        links += by_cluster.get(target, [])[:1]

    # 3. funnel progression
    current_level = FUNNEL_PRIORITY.get(funnel, 1)
    for f, level in FUNNEL_PRIORITY.items():
        if level > current_level:
            links += by_funnel.get(f, [])[:1]
            break

    # 4. BOFU conversion boost
    links += by_funnel.get("bofu", [])[:1]

    # remove duplicates + self
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

        output.append(a)

    return output

# =========================
# SAVE SAFE YAML
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
# VALIDATION (CI SAFE)
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
# RUN
# =========================

def main():
    articles = load_articles()
    validate(articles)

    output = build_output(articles)
    save_yaml(output)

    print("✅ _data/articles-linked.yml generated successfully")

if __name__ == "__main__":
    main()
