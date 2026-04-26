import random

def generate_body(article):

    title = article.get("title", "")
    cluster = article.get("cluster", "base")
    funnel = article.get("funnel", "tofu")
    seed = article.get("seed", 0)

    random.seed(seed)

    # =========================
    # CLUSTER CONTEXT BOOST
    # =========================

    cluster_context = {
        "base": "situazioni quotidiane generiche",
        "travel": "viaggi, aeroporti, hotel, trasporti",
        "business": "lavoro, email, colloqui, meeting",
        "expat": "vita all'estero e problemi reali",
        "social": "amicizie, conversazioni, small talk",
        "method": "studio e apprendimento lingua",
    }.get(cluster, "situazioni reali")

    # =========================
    # FUNNEL ADAPTATION
    # =========================

    funnel_boost = {
        "tofu": "introduzione semplice e accessibile",
        "mofu": "esempi pratici e uso reale",
        "bofu": "applicazione avanzata e casi reali complessi",
    }.get(funnel, "uso pratico")

    # =========================
    # RANDOM VARIATION (REAL EFFECT)
    # =========================

    openings = [
        f"In questa guida su {title} vedrai come usarlo in {cluster_context}.",
        f"{title} è fondamentale quando ti trovi in {cluster_context}.",
        f"Capire {title} ti aiuta in situazioni di {cluster_context}.",
    ]

    intro = random.choice(openings)

    # =========================
    # BODY
    # =========================

    return f"""
## Introduzione
{intro}

## Cos’è
{title} viene usato in contesti legati a {cluster_context}. È importante soprattutto per chi vuole migliorare il proprio inglese nella vita reale.

## Esempi pratici
- esempio reale 1 in {cluster_context}
- esempio reale 2 in {cluster_context}
- esempio reale 3 in {cluster_context}
- esempio reale 4 in {cluster_context}
- esempio reale 5 in {cluster_context}

## Errori comuni
Molti italiani sbagliano perché non collegano {title} a situazioni reali di {cluster_context}.

## Uso nella vita reale
Questo concetto si applica soprattutto in: {funnel_boost}.

---
SEED: {seed}
CLUSTER: {cluster}
FUNNEL: {funnel}
""".strip()
