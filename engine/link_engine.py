def pick_internal_links(article, by_cluster, by_funnel):

    cluster = article.get("cluster", "base")
    funnel = article.get("funnel", "tofu")

    links = []
    seen = set()

    def add(items):
        for i in items:
            if not isinstance(i, dict):
                continue

            if i.get("id") == article.get("id"):
                continue

            if i.get("id") in seen:
                continue

            if i.get("title") and i.get("url"):
                links.append(i)
                seen.add(i.get("id"))

    # 1. stesso cluster (massima rilevanza)
    add(by_cluster.get(cluster, [])[:3])

    # 2. cluster collegati SEO (espansione semantica)
    cluster_map = {
        "base": ["travel", "social"],
        "travel": ["expat", "social"],
        "social": ["expat", "business"],
        "expat": ["business", "method"],
        "business": ["method"],
        "method": ["bofu"],
    }

    for c in cluster_map.get(cluster, []):
        add(by_cluster.get(c, [])[:1])

    # 3. funnel progression (conversion path)
    funnel_priority = ["tofu", "mofu", "bofu"]
    current = funnel_priority.index(funnel)

    if current < len(funnel_priority) - 1:
        next_funnel = funnel_priority[current + 1]
        add(by_funnel.get(next_funnel, [])[:1])

    return links[:5]
