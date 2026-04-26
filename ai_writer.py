import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_article_body(title, cluster, funnel):
    prompt = f"""
Sei un SEO content writer per un blog di inglese chiamato FluenteMente.

Scrivi un articolo lungo, pratico e altamente SEO.

TITOLO: {title}
CLUSTER: {cluster}
FUNNEL: {funnel}

REGOLE:
- 1200-2000 parole
- italiano semplice
- esempi reali
- frasi in inglese con traduzione
- struttura H2/H3
- niente riempitivi
- stile insegnante pratico

OUTPUT: solo articolo in markdown
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
