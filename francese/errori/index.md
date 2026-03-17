---
layout: page
title: "Errori e Faux Amis in Francese: L'archivio"
description: "Scopri gli errori più comuni degli italiani in francese e impara a riconoscere i temutissimi falsi amici (faux amis)."
permalink: /francese/errori/
---

In questa pagina abbiamo raccolto tutti gli articoli che ti aiuteranno a non commettere più gli scivoloni tipici degli italiani quando parlano in francese. Attento alle traduzioni letterali!

<a href="{{ '/francese/' | relative_url }}">⬅ Torna alla guida principale di Francese</a>

<hr>

<ul>
{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'francese' and post.categories contains 'errori'" %}
{% for post in category_posts %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br><small style="color: #555;">{% if post.description %}{{ post.description }}{% else %}{{ post.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endfor %}
</ul>

{% include promo-box.html type="errori" lang="francese" %}
