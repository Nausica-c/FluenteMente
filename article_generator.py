from ai_writer import generate_article_body

def build_article(article):
    title = article["title"]
    cluster = article.get("cluster", "base")
    funnel = article.get("funnel", "tofu")

    body = generate_article_body(title, cluster, funnel)

    article["ai_body"] = body
    return article
