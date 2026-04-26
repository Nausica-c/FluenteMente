import yaml
from collections import defaultdict

# =========================
# CONFIG
# =========================

INPUT_FILE = "_data/articles.yml"
OUTPUT_FILE = "_data/articles-linked.yml"

FUNNEL_PRIORITY = {
    "tofu": 1,
    "mofu": 2,
    "bofu": 3
}

# =========================
# LOAD SAFE YAML
# =========================

def load_articles():
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        raise ValueError(f"File non trovato: {INPUT_FILE}")

    if not data:
        raise ValueError("articles.yml è vuoto o non valido")

    if not isinstance(data, list):
        raise ValueError("articles.yml deve essere una LISTA di articoli")

    return data

# =========================
# INDEX ARTICLES
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
# PICK LINKS (SAFE + NO SELF LINK)
# =========================

def pick_links(article, by_cluster, by_funnel):
    cluster = article.get("cluster")
    funnel = article.get("funnel")
    article_id = article.get("id")

    links = []

    # 1. stesso cluster (senza self-link)
    for a in by_cluster.get(cluster, []):
        if a.get("id") != article_id:
            links.append(a)
        if len(links) >= 3:
            break

    # 2. funnel successivo
    current_level = FUNNEL_PRIORITY.get(funnel, 1)

    for f, level in FUNNEL_PRIORITY.items():
        if level > current_level:
            for a in by_funnel.get(f, []):
                if a.get("id") != article_id:
                    links.append(a)
                    break
            break

    # 3. link a metodo (BOFU)
    for a in by_funnel.get("bofu", []):
        if a.get("cluster") == "method" and a.get("id") != article_id:
            links.append(a)
            break

    # remove duplicates
    seen = set()
    clean = []

    for l in links:
        lid = l.get("id")
        if lid and lid not in seen:
            clean.append(l)
            seen.add(lid)

    return clean[:5]

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
                "id": x.get("id"),
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
# SAFE WRITE YAML
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
# VALIDATION (ANTI CRASH)
# =========================

def validate(articles):
    required_fields = ["id", "title", "url"]

    for i, a in enumerate(articles):
        if not isinstance(a, dict):
            raise ValueError(f"Elemento non valido in posizione {i}")

        for field in required_fields:
            if field not in a:
                raise ValueError(f"Missing '{field}' in article id={a.get('id')}")

# =========================
# MAIN
# =========================

def main():
    articles = load_articles()

    validate(articles)

    output = build_output(articles)

    if not output:
        raise ValueError("Output vuoto: controlla articles.yml")

    save_yaml(output)

    print("✅ _articles-linked.yml generato con successo")

if __name__ == "__main__":
    main()
