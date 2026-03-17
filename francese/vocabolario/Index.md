---
layout: page
title: "Vocabolario Francese: Liste di parole per livello (A1 - C1)"
description: "Tutte le liste di vocaboli divisi per livello. Parti dalle basi (A1) e arriva alla padronanza completa del francese (C1)."
permalink: /francese/vocabolario/
---

Benvenuto nell'archivio completo del vocabolario. Per aiutarti a studiare in modo strategico, abbiamo diviso le nostre liste di parole in base al tuo livello di partenza. Inizia dalle basi e sblocca i livelli successivi!

<a href="{{ '/francese/' | relative_url }}">⬅ Torna alla guida principale di Francese</a>

<hr>

{% assign vocabolario_posts = site.posts | where_exp: "post", "post.categories contains 'francese' and post.categories contains 'vocabolario'" %}
{% assign unclassified_posts = "" | split: "" %}
{% for post in vocabolario_posts %}
  {% unless post.categories contains 'a1' or post.categories contains 'a2' or post.categories contains 'b1' or post.categories contains 'b2' or post.categories contains 'c1' %}
    {% assign unclassified_posts = unclassified_posts | push: post %}
  {% endunless %}
{% endfor %}

{% if unclassified_posts.size > 0 %}
## 🆕 Nuovi arrivi (In aggiornamento)
<p style="color: #777;"><em>Liste appena pubblicate, in attesa di essere assegnate al livello corretto.</em></p>
<ul>
{% for post in unclassified_posts %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br><small style="color: #555;">{% if post.description %}{{ post.description }}{% else %}{{ post.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% endfor %}
</ul>
<hr>
{% endif %}

## 🟢 Livello A1 (Principiante)
Le parole fondamentali per iniziare a capire e farsi capire in francese.

<ul>
{% assign a1_posts = site.posts | where_exp: "post", "post.categories contains 'francese' and post.categories contains 'vocabolario' and post.categories contains 'a1'" %}
{% for post in a1_posts %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br><small style="color: #555;">{% if post.description %}{{ post.description }}{% else %}{{ post.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato per il livello A1.</em></li>
{% endfor %}
</ul>

{% include promo-box.html type="vocabolario" lang="francese" %}

<hr>
## 🟡 Livello A2 (Elementare) - *Coming Soon ⏳*
<hr>
## 🟠 Livello B1 (Intermedio) - *Coming Soon ⏳*
<hr>
## 🔴 Livello B2 (Intermedio Superiore) - *Coming Soon ⏳*
<hr>
## 🟣 Livello C1 (Avanzato) - *Coming Soon ⏳*
