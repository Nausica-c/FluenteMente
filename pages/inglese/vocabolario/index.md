---
layout: page
title: "Vocabolario Inglese: Liste di parole per livello (A1 - C1)"
description: "Tutte le liste di vocaboli divisi per livello. Parti dalle basi (A1) e arriva alla padronanza completa dell'inglese (C1)."
permalink: /inglese/vocabolario/
---

Benvenuto nell'archivio completo del vocabolario. Per aiutarti a studiare in modo strategico senza sentirti sopraffatto, abbiamo diviso le nostre liste di parole in base al tuo livello di partenza. 

Inizia dalle basi e sblocca i livelli successivi man mano che ti senti più sicuro!

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>

<hr>

{% comment %} LOGICA DI SALVATAGGIO: Cerca post senza livello e li mostra solo se esistono {% endcomment %}
{% assign vocabolario_posts = site.posts | where_exp: "post", "post.categories contains 'inglese' and post.categories contains 'vocabolario'" %}
{% assign unclassified_posts = "" | split: "" %}

{% for post in vocabolario_posts %}
  {% unless post.categories contains 'a1' or post.categories contains 'a2' or post.categories contains 'b1' or post.categories contains 'b2' or post.categories contains 'c1' %}
    {% assign unclassified_posts = unclassified_posts | push: post %}
  {% endunless %}
{% endfor %}

{% if unclassified_posts.size > 0 %}
## 🆕 Nuovi arrivi (In aggiornamento)
<p style="color: #777;"><em>Liste appena pubblicate, in attesa di essere assegnate al livello corretto. Puoi già iniziare a studiarle qui!</em></p>

<ul>
{% for post in unclassified_posts %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br><small style="color: #555;">
      {% if post.description %}{{ post.description }}{% else %}{{ post.excerpt | strip_html | truncatewords: 25 }}{% endif %}
    </small>
  </li>
{% endfor %}
</ul>
<hr>
{% endif %}
{% comment %} FINE LOGICA DI SALVATAGGIO {% endcomment %}


## 🟢 Livello A1 (Principiante)
Le parole fondamentali per iniziare a capire e farsi capire. Le basi assolute per sopravvivere in inglese.

<ul>
{% assign a1_posts = site.posts | where_exp: "post", "post.categories contains 'inglese' and post.categories contains 'vocabolario' and post.categories contains 'a1'" %}
{% for post in a1_posts %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br><small style="color: #555;">
      {% if post.description %}{{ post.description }}{% else %}{{ post.excerpt | strip_html | truncatewords: 25 }}{% endif %}
    </small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato per il livello A1.</em></li>
{% endfor %}
</ul>

{% include promo-box.html type="vocabolario" lang="inglese" %}

<hr>

## 🟡 Livello A2 (Elementare) - *Coming Soon ⏳*
Il vocabolario per gestire situazioni quotidiane semplici (fare la spesa, chiedere indicazioni, parlare della propria famiglia).
<p style="color: #777;"><em>Stiamo preparando centinaia di nuove parole per questo livello. Torna a trovarci presto!</em></p>

<hr>

## 🟠 Livello B1 (Intermedio) - *Coming Soon ⏳*
Le parole che ti servono per viaggiare in autonomia, esprimere opinioni, raccontare eventi passati e gestire imprevisti.
<p style="color: #777;"><em>Stiamo preparando centinaia di nuove parole per questo livello. Torna a trovarci presto!</em></p>

<hr>

## 🔴 Livello B2 (Intermedio Superiore) - *Coming Soon ⏳*
Il vocabolario per lavorare in inglese, sostenere un colloquio e comprendere i madrelingua a velocità naturale.
<p style="color: #777;"><em>Stiamo preparando centinaia di nuove parole per questo livello. Torna a trovarci presto!</em></p>

<hr>

## 🟣 Livello C1 (Avanzato) - *Coming Soon ⏳*
Termini complessi, sfumature di significato, lessico accademico e business avanzato. Per padroneggiare la lingua al 100%.
<p style="color: #777;"><em>Stiamo preparando centinaia di nuove parole per questo livello. Torna a trovarci presto!</em></p>

