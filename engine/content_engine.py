import random

def generate_body(article):

    title = article.get("title", "")
    cluster = article.get("cluster", "base")
    funnel = article.get("funnel", "tofu")
    seed = article.get("seed", 0)

    random.seed(seed)

    return f"""
## Introduzione
Guida pratica su {title} con esempi reali.

## Cos’è
Spiegazione semplice e applicabile.

## Esempi pratici
- esempio 1
- esempio 2
- esempio 3
- esempio 4
- esempio 5

## Errori comuni
Errori tipici italiani.

## Uso nella vita reale
Situazioni: viaggio, lavoro, expat.

---
SEED: {seed}
CLUSTER: {cluster}
FUNNEL: {funnel}
""".strip()
