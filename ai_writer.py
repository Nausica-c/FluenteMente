import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# =========================
# LINKS → SEO ANCHOR FORMAT
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

        # SEO anchor più naturale
        cleaned.append(f"{title} ({url})")

    return "\n".join(cleaned)

# =========================
# MAIN ENGINE
# =========================

def generate_article_body(title, cluster, funnel, internal_links=None):

    links_text = format_links(internal_links)

    prompt = f"""
Sei un SEO content writer senior per FluenteMente.

OBIETTIVO:
insegnare inglese pratico per italiani (viaggio, lavoro, expat).

---

TITOLO: {title}
CLUSTER: {cluster}
FUNNEL: {funnel}

---

REGOLE CRITICHE:
- zero teoria inutile
- sempre esempi reali
- inglese + traduzione
- tono semplice A2-B1
- contenuto immediatamente utilizzabile

---

STRUTTURA OBBLIGATORIA:

## Introduzione
problema reale + 1 frase inglese + traduzione

## Cos’è e quando si usa
spiegazione pratica concreta

## Esempi pratici
minimo 5 esempi reali:
- inglese + traduzione

## Errori comuni
errori italiani + correzione

## Uso nella vita reale
viaggio / lavoro / expat

---

INTERNAL LINKS (OBBLIGATORI DENTRO IL TESTO):
Usa questi articoli e integrali naturalmente nelle frasi:

{links_text}

REGOLE LINKING:
- NON fare lista finale
- NON mettere URL isolati
- integra i link nel contesto
- ogni link deve essere naturale

---

OUTPUT:
solo markdown
NO H1
"""

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content.strip()

    # =========================
    # VALIDAZIONE STABILE
    # =========================
    if (
        not content
        or len(content) < 600
        or "##" not in content
    ):
        return fallback_article(title, internal_links)

    return content

# =========================
# FALLBACK SEO-COHERENT
# =========================

def fallback_article(title, internal_links=None):

    links_text = format_links(internal_links)

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

---

Articoli correlati:
{links_text}
""".strip()
