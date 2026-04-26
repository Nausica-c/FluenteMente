import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# =========================
# INTERNAL LINKS (SEO MODE)
# =========================

def format_links(internal_links):
    if not internal_links:
        return ""

    blocks = []
    for l in internal_links:
        if not isinstance(l, dict):
            continue

        title = l.get("title")
        url = l.get("url")

        if not title or not url:
            continue

        # SEO anchor naturale
        blocks.append(f"- {title} ({url})")

    return "\n".join(blocks)


# =========================
# SAFE FALLBACK
# =========================

def fallback_article(title):
    return f"""
## Introduzione
Guida pratica su {title} con esempi reali e immediati.

## Cos’è e quando si usa
Spiegazione semplice e applicabile nella vita reale.

## Esempi pratici
- esempio reale 1
- esempio reale 2
- esempio reale 3
- esempio reale 4
- esempio reale 5

## Errori comuni
Errori tipici italiani e come evitarli.

## Uso nella vita reale
Situazioni: viaggio, lavoro, expat.
""".strip()


# =========================
# MAIN ENGINE V4
# =========================

def generate_article_body(title, cluster, funnel, internal_links=None):

    links_text = format_links(internal_links)

    prompt = f"""
Sei un SEO content writer senior per FluenteMente.

OBIETTIVO:
insegnare inglese pratico (viaggio, lavoro, vita reale).

TITOLO: {title}
CLUSTER: {cluster}
FUNNEL: {funnel}

REGOLE OBBLIGATORIE:
- niente teoria inutile
- esempi reali SEMPRE
- ogni esempio deve avere inglese + traduzione
- tono A2-B1
- concreto e diretto

STRUTTURA OBBLIGATORIA:

## Introduzione
problema reale + frase inglese

## Cos’è e quando si usa
spiegazione pratica + contesto reale

## Esempi pratici
5 esempi con:
- inglese
- traduzione

## Errori comuni
errori italiani + correzione

## Uso nella vita reale
situazioni: viaggio, lavoro, expat

---

INTERNAL LINKS (da integrare NATURALMENTE nel testo):
{links_text}

REGOLE LINK:
- NON fare lista finale
- inserisci i link dentro frasi
- usa anchor naturali SEO
- NON scrivere "clicca qui"

---

OUTPUT:
solo markdown
NO H1
minimo 1200 parole
"""

    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        content = response.choices[0].message.content.strip()

        # =========================
        # VALIDAZIONE V4
        # =========================
        if (
            not content
            or len(content) < 900
            or "##" not in content
            or "esempio" not in content.lower()
        ):
            return fallback_article(title)

        return content

    except Exception:
        return fallback_article(title)
