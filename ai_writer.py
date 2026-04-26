import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_article_body(title, cluster, funnel, internal_links=None):

    # =========================
    # INTERNAL LINKS → SEO CONTEXT
    # =========================
    links_text = ""

    if internal_links:
        links_text = "\n".join(
            [f"- {l.get('title')} ({l.get('url')})" for l in internal_links if l.get("title") and l.get("url")]
        )

    # =========================
    # PROMPT V3 (ANTI-CONTENUTO VUOTO)
    # =========================
    prompt = f"""
Sei un SEO content writer senior per il blog FluenteMente.

Scrivi un articolo COMPLETO, concreto e utile.

---

TITOLO: {title}
CLUSTER: {cluster}
FUNNEL: {funnel}

---

OBIETTIVO:
Aiutare italiani a usare l’inglese nella vita reale.

---

REGOLE FONDAMENTALI:
- NON scrivere contenuto generico
- NON usare frasi tipo "questo articolo esplora"
- ogni sezione deve insegnare qualcosa di pratico
- esempi realistici (viaggio, lavoro, vita quotidiana)
- inserisci frasi in inglese + traduzione

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
- minimo 5 esempi
- inglese + traduzione

## Errori comuni
- errori tipici italiani
- spiegazione + correzione

## Come usarlo nella vita reale
- contesti: viaggio / lavoro / expat

---

INTERNAL LINKING (OBBLIGATORIO):

Integra naturalmente nel testo questi articoli:

{links_text}

REGOLE:
- inserisci link nelle frasi
- usa anchor naturali
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
NON inserire H1 (# titolo) perché è già nel template.
"""

    # =========================
    # API CALL (VERSIONE STABILE)
    # =========================
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content

    # =========================
    # FAILSAFE (ANTI ARTICOLO VUOTO)
    # =========================
    if not content or len(content) < 800:
        return f"""
## Introduzione
Se vuoi capire {title}, qui trovi una guida pratica con esempi reali.

## Contenuto
Spiegazione base con applicazioni concrete.

## Esempi
- esempio semplice
- esempio reale

## Errori comuni
Errori tipici da evitare.

## Uso reale
Come usarlo nella vita quotidiana.
""".strip()

    return content
