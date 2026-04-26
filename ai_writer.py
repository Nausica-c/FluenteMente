import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_article_body(title, cluster, funnel, internal_links=None):

    # =========================
    # INTERNAL LINKS → SEO CONTEXT FORTE
    # =========================
    links_text = ""

    if internal_links:
        links_text = "\n".join([
            f"- {l.get('title')} → {l.get('url')} (cluster: {l.get('cluster')}, funnel: {l.get('funnel')})"
            for l in internal_links
            if l.get("title") and l.get("url")
        ])

    # =========================
    # PROMPT V3 (FORZATO + PRATICO)
    # =========================
    prompt = f"""
Sei un SEO content writer senior per FluenteMente.

Scrivi un articolo utile, concreto e immediatamente applicabile.

---

TITOLO: {title}
CLUSTER: {cluster}
FUNNEL: {funnel}

---

OBIETTIVO:
Aiutare italiani a usare inglese reale (viaggio, lavoro, expat).

---

REGOLE CRITICHE:
- ZERO contenuto generico
- ZERO frasi tipo "questo articolo spiega"
- ogni sezione deve insegnare qualcosa di pratico
- usa esempi realistici (aeroporto, hotel, lavoro, amici)
- inserisci sempre inglese + traduzione

---

STRUTTURA OBBLIGATORIA:

## Introduzione
- problema reale
- situazione concreta
- 1 frase inglese + traduzione

## Cos’è e quando si usa
- spiegazione semplice
- quando serve davvero

## Esempi pratici
- almeno 5 esempi reali
- inglese + traduzione

## Errori comuni
- errori tipici italiani
- correzione chiara

## Come usarlo nella vita reale
- viaggio / lavoro / expat

---

INTERNAL LINKING (OBBLIGATORIO):

Integra NATURALMENTE nel testo questi articoli:

{links_text}

REGOLE LINK:
- inserisci link dentro le frasi
- usa anchor naturali SEO
- NON fare lista finale
- NON scrivere "clicca qui"

---

STILE:
- italiano semplice (A2-B1)
- tono pratico, diretto
- niente teoria inutile
- utile subito

---

LUNGHEZZA:
1200–1800 parole

---

OUTPUT:
Solo Markdown.
NON inserire H1 (# titolo).
"""

    # =========================
    # API CALL
    # =========================
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content.strip()

    # =========================
    # 🔥 VALIDAZIONE INTELLIGENTE
    # =========================
    if (
        not content
        or len(content) < 1000
        or "esempio" not in content.lower()
        or "##" not in content
    ):
        return f"""
## Introduzione
Se vuoi capire {title}, qui trovi una guida pratica con esempi reali.

## Cos’è e quando si usa
Spiegazione semplice e concreta.

## Esempi pratici
- esempio reale 1
- esempio reale 2
- esempio reale 3
- esempio reale 4
- esempio reale 5

## Errori comuni
Attenzione agli errori tipici italiani.

## Come usarlo nella vita reale
Situazioni concrete: viaggio, lavoro, vita quotidiana.
""".strip()

    return content
