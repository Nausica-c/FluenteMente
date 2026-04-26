from ai_writer import generate_article_body
import random

def build_article(article):

    title = article.get("title", "")
    cluster = article.get("cluster", "base")
    funnel = article.get("funnel", "tofu")

    seed = random.randint(1000, 9999)

    # ✔ mantenere compatibilità con AI writer classico
    body = generate_article_body(
        title=title,
        cluster=cluster,
        funnel=funnel,
        seed=seed
    )

    # 🔥 fallback robusto
    if not body or len(body) < 800:
        body = f"""
## Introduzione
Guida pratica su {title}.

## Spiegazione
Contenuto educativo con esempi.

## Esempi
- esempio 1
- esempio 2

## Conclusione
Applicazione pratica nel mondo reale.
""".strip()

    article["ai_body"] = body
    article["seed"] = seed

    return article
