---
layout: page
title: "Francese in Viaggio: L'archivio completo"
description: "Dal ristorante all'aeroporto: tutte le guide e le espressioni utili per il tuo prossimo viaggio in Francia."
permalink: /francese/viaggio/
---

Le guide pratiche e i frasari per viaggiare in Francia e nei paesi francofoni in totale autonomia, senza ansie.

<a href="{{ '/francese/' | relative_url }}">⬅ Torna alla guida principale di Francese</a>

<hr>

<ul>
{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'francese' and post.categories contains 'viaggio'" %}
{% for post in category_posts %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br><small style="color: #555;">{% if post.description %}{{ post.description }}{% else %}{{ post.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endfor %}
</ul>

{% include promo-box.html type="viaggio" lang="francese" %}
