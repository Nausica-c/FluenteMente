from ai_writer import generate_article_body
import random

def build_article(article):

    title = article.get("title", "")
    cluster = article.get("cluster", "base")
    funnel = article.get("funnel", "tofu")

    # 🔥 SEO CONTEXT ENRICHMENT
    seed = random.randint(1000, 9999)

    context = {
        "title": title,
        "cluster": cluster,
        "funnel": funnel,
        "seed": seed,
        "intent": "learn english fluency practical usage",
        "tone": "teacher practical simple"
    }

    body = generate_article_body(context)

    # 🔥 VALIDAZIONE MINIMA (IMPORTANTISSIMO)
    if not body or len(body) < 500:
        body = f"## Contenuto base\n\nSpiegazione di {title} con esempi pratici."

    article["ai_body"] = body
    article["seed"] = seed

    return article
