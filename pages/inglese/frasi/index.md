---
layout: page
title: "Frasi ed Espressioni in Inglese: Tutti gli articoli"
description: "Archivio di frasi pronte all'uso, espressioni per viaggiare e formule per sembrare più fluente."
permalink: /inglese/frasi/
---

Non sai come esprimerti in una certa situazione? In questo archivio trovi tutte le nostre guide dedicate alle frasi e alle espressioni di sopravvivenza in inglese.

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>

<hr>

<ul>
{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'inglese' and post.categories contains 'frasi'" %}
{% for post in category_posts %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br><small style="color: #555;">
      {% if post.description %}{{ post.description }}{% else %}{{ post.excerpt | strip_html | truncatewords: 25 }}{% endif %}
    </small>
  </li>
{% endfor %}
</ul>
