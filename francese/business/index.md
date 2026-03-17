---
layout: page
title: "Francese per il Lavoro: L'archivio completo"
description: "Guide su come scrivere email, affrontare colloqui di lavoro e partecipare a riunioni in lingua francese."
permalink: /francese/business/
---

Tutte le risorse per migliorare il tuo francese professionale e aprirti nuove opportunità di carriera nei paesi francofoni.

<a href="{{ '/francese/' | relative_url }}">⬅ Torna alla guida principale di Francese</a>

<hr>

<ul>
{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'francese' and post.categories contains 'business'" %}
{% for post in category_posts %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br><small style="color: #555;">{% if post.description %}{{ post.description }}{% else %}{{ post.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endfor %}
</ul>

{% include promo-box.html type="business" lang="francese" %}
