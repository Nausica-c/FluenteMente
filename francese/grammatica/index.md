---
layout: page
title: "Grammatica Francese: Tutti gli articoli"
description: "Regole, congiuntivi ed eccezioni spiegate in modo semplice per padroneggiare la grammatica francese senza impazzire."
permalink: /francese/grammatica/
---

In questa pagina trovi l'archivio completo di tutte le guide e spiegazioni sulla grammatica francese. Dimentica i vecchi libri di scuola: qui impariamo a usare la lingua vera.

<a href="{{ '/francese/' | relative_url }}">⬅ Torna alla guida principale di Francese</a>

<hr>

<ul>
{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'francese' and post.categories contains 'grammatica'" %}
{% for post in category_posts %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br><small style="color: #555;">{% if post.description %}{{ post.description }}{% else %}{{ post.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endfor %}
</ul>

{% include promo-box.html type="grammatica" lang="francese" %}
