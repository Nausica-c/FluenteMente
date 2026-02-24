---
layout: default
title: Home
---

<section class="post" style="padding:1.1rem;">
  <h1 style="margin:.1rem 0 .35rem; letter-spacing:-.02em;">Impara una lingua con metodo (e senza mollare)</h1>
  <p class="muted" style="margin:0;">
    Strategie pratiche, routine brevi e risorse consigliate. Quando ha senso, ti indico anche Babbel in modo trasparente.
  </p>

  <div style="margin-top:1rem; display:flex; gap:.75rem; flex-wrap:wrap;">
    <a class="btn" href="{{ site.babbel_url }}" target="_blank" rel="noopener sponsored">Prova Babbel</a>
    <a class="btn btn-ghost" href="{{ '/hub-lingue/' | relative_url }}">Vai all’Hub lingue</a>
  </div>
</section>

<div style="margin-top:1rem;">
  <h2 style="margin:1rem 0 .5rem;">Ultimi articoli</h2>
  <div class="post" style="padding:1rem;">
    <ul style="margin:0; padding-left:1.25rem;">
      {% for post in site.posts limit:6 %}
        <li style="margin:.35rem 0;">
          <a href="{{ post.url | relative_url }}"><strong>{{ post.title }}</strong></a>
          <span class="muted"> · {{ post.date | date: "%d %b %Y" }}</span>
        </li>
      {% endfor %}
    </ul>
  </div>
</div>
