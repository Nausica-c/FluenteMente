import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_article_body(title, cluster, funnel, internal_links=None):

    links_text = ""

    # 🔥 convert internal links into readable SEO context
    if internal_links:
        links_text = "\n".join(
            [f"- {l.get('title')} ({l.get('url')})" for l in internal_links]
        )

    prompt = f"""
Sei un SEO content writer senior per il blog FluenteMente.

Scrivi un articolo COMPLETO pronto per Jekyll.

---

## TITOLO
{title}

## CLUSTER
{cluster}

## FUNNEL
{funnel}

---

## OBIETTIVO
Aiutare italiani a imparare inglese pratico per vita reale (viaggi, lavoro, expat).

---

## STRUTTURA OBBLIGATORIA

Devi seguire ESATTAMENTE questa struttura:

# INTRODUZIONE
- problema reale dell’utente
- contesto pratico
- 1 frase in inglese con traduzione

## Cos’è {title}
Spiegazione semplice e chiara

## Esempi pratici
- almeno 5 esempi reali
- inglese + traduzione italiana

## Errori comuni
- errori tipici italiani

## Come usarlo nella vita reale
- situazioni reali (viaggio / lavoro / expat)

---

## INTERNAL LINKING (OBBLIGATORIO)

Usa questi articoli come riferimento naturale nel testo:

{links_text}

REGOLE LINK:
- integrati nelle frasi
- NO lista separata
- NO "clicca qui"
- anchor naturali SEO

---

## STILE
- italiano semplice (A2-B1)
- tono insegnante pratico
- niente frasi generiche tipo "questo articolo esplora"
- concreto, utile, realistico
- 1200–2000 parole

---

## OUTPUT
Solo articolo Markdown puro.
Nessuna spiegazione.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
