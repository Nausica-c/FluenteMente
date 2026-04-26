import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# =========================
# INTERNAL LINKS FORMATTER SAFE
# =========================

def format_links(internal_links):
    if not internal_links:
        return ""

    cleaned = []
    for l in internal_links:
        if not isinstance(l, dict):
            continue

        title = l.get("title")
        url = l.get("url")

        if not title or not url:
            continue

        cleaned.append(f"- {title} → {url}")

    return "\n".join(cleaned)

# =========================
# MAIN ENGINE
# =========================

def generate_article_body(title, cluster, funnel, internal_links=None):

    links_text = format_links(internal_links)

    prompt = f"""
Sei un SEO content writer senior per FluenteMente.

Scrivi un articolo utile, concreto e immediatamente applicabile.

TITOLO: {title}
CLUSTER: {cluster}
FUNNEL: {funnel}

OBIETTIVO:
Aiutare italiani a usare inglese reale (viaggio, lavoro, expat).

REGOLE:
- niente teoria inutile
- esempi concreti sempre
- inglese + traduzione

STRUTTURA:

## Introduzione
problema reale + frase inglese

## Cos’è e quando si usa
spiegazione pratica

## Esempi pratici
5 esempi reali con traduzione

## Errori comuni
errori italiani + correzione

## Uso nella vita reale
situazioni: viaggio, lavoro, expat

INTERNAL LINKS (naturali nel testo):
{links_text}

STILE:
semplice A2-B1, pratico, diretto

OUTPUT:
solo markdown, senza H1
"""

    # =========================
    # API CALL (SDK MODERNO)
    # =========================
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content.strip()

    # =========================
    # VALIDAZIONE ROBUSTA
    # =========================
    if (
        not content
        or len(content) < 1000
        or "##" not in content
        or "esempio" not in content.lower()
    ):
        return fallback_article(title)

    return content

# =========================
# FALLBACK COERENTE SEO
# =========================

def fallback_article(title):
    return f"""
## Introduzione
Se vuoi capire {title}, ecco una guida pratica con esempi reali.

## Cos’è e quando si usa
Spiegazione semplice e diretta.

## Esempi pratici
- esempio reale 1
- esempio reale 2
- esempio reale 3
- esempio reale 4
- esempio reale 5

## Errori comuni
Attenzione agli errori tipici italiani.

## Uso nella vita reale
Situazioni concrete: viaggio, lavoro, expat.
""".strip()
