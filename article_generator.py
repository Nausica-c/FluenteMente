from ai_writer import generate_article_body
import random

def build_article(article):

    title = article.get("title", "")
    cluster = article.get("cluster", "base")
    funnel = article.get("funnel", "tofu")
    internal_links = article.get("internal_links") or []

    seed = random.randint(1000, 9999)

    # 🔥 AI GENERATION (con contesto completo)
    body = generate_article_body(
        title=title,
        cluster=cluster,
        funnel=funnel,
        internal_links=internal_links
    )

    # 🔥 FALLBACK ROBUSTO (anti empty / low quality)
    if not body or len(body.strip()) < 1000:
        body = f"""
# Introduzione
Se vuoi capire {title}, sei nel posto giusto.

## Cos’è {title}
Spiegazione semplice e diretta con esempi concreti.

## Esempi pratici
- esempio reale 1
- esempio reale 2
- esempio reale 3
- esempio reale 4

## Errori comuni
Attenzione agli errori tipici degli italiani quando usano questo concetto.

## Come usarlo nella vita reale
Situazioni reali: viaggio, lavoro, vita quotidiana.

## Mini riepilogo
Concetto usato in modo pratico e immediato.
""".strip()

    article["ai_body"] = body
    article["seed"] = seed

    return article
