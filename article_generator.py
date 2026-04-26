from ai_writer import generate_article_body
import random

def build_article(article):

    title = article.get("title", "")
    cluster = article.get("cluster", "base")
    funnel = article.get("funnel", "tofu")
    internal_links = article.get("internal_links", [])

    seed = random.randint(1000, 9999)

    # 🔥 CONTEXT per AI (vero upgrade)
    body = generate_article_body(
        title=title,
        cluster=cluster,
        funnel=funnel,
        internal_links=internal_links
    )

    # 🔥 VALIDAZIONE SERIA (anti contenuto vuoto)
    if not body or len(body) < 1000:
        body = f"""
# Introduzione
Se vuoi capire {title}, sei nel posto giusto.

## Cos’è {title}
Spiegazione semplice e diretta.

## Esempi pratici
- esempio reale 1
- esempio reale 2
- esempio reale 3

## Errori comuni
Attenzione agli errori tipici italiani.

## Come usarlo nella vita reale
Situazioni concrete (viaggio, lavoro, vita quotidiana).
""".strip()

    article["ai_body"] = body
    article["seed"] = seed

    return article
