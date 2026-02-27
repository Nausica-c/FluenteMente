---
layout: page
title: "Imparare il Portoghese: Guida, Varianti e Risorse per Italiani"
subtitle: "Dal Portogallo al Brasile: scopri la lingua più musicale del mondo e come parlarla da adulto."
description: "L'hub definitivo per imparare il portoghese. Differenze tra portoghese europeo e brasiliano, pronuncia, falsi amici e frasi utili."
permalink: /portoghese/
---

Il portoghese è una lingua che ti entra nel cuore. Spesso sottovalutato, è la chiave per comunicare in tre continenti e per immergersi in culture straordinarie, dal fado di Lisbona alla bossa nova di Rio de Janeiro.

Per un italiano, il portoghese scritto è quasi comprensibile, ma il parlato nasconde suoni chiusi e ritmi complessi. In questo hub ti guidiamo alla scoperta della lingua lusofona.

---

## 1. Portogallo vs Brasile (Quale scegliere?)

Le differenze di accento, vocabolario e grammatica tra il portoghese europeo e quello brasiliano. Da dove iniziare?

<ul>
{% assign basi_posts = site.categories['portoghese'] | where_exp: "item", "item.tags contains 'basi'" %}
{% if basi_posts.size > 0 %}
  {% for post in basi_posts %}
    <li>👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong></li>
  {% endfor %}
{% else %}
  <li><em>Articoli in lavorazione! Stiamo analizzando le varianti per te.</em></li>
{% endif %}
</ul>

---

## 2. Falsi Amici Portogallo-Italia

Attenzione a non fare confusione tra "propina" (che in portoghese è semplicemente la tassa universitaria!) e altri trabocchetti linguistici.

<ul>
{% assign errori_posts = site.categories['portoghese'] | where_exp: "item", "item.tags contains 'errori'" %}
{% if errori_posts.size > 0 %}
  {% for post in errori_posts %}
    <li>👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong></li>
  {% endfor %}
{% else %}
  <li><em>Articoli in lavorazione! I falsi amici portoghesi sono in arrivo.</em></li>
{% endif %}
</ul>

---

## 3. La Pronuncia e le Vocali Nasali

Imparare a pronunciare la "tilde" (ã) e a distinguere i suoni aperti e chiusi che rendono il portoghese così unico.

<ul>
{% assign pronuncia_posts = site.categories['portoghese'] | where_exp: "item", "item.tags contains 'pronuncia'" %}
{% if pronuncia_posts.size > 0 %}
  {% for post in pronuncia_posts %}
    <li>👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong></li>
  {% endfor %}
{% else %}
  <li><em>Articoli in lavorazione! Stiamo preparando gli audio tutorial.</em></li>
{% endif %}
</ul>

---

## 4. Frasi di Sopravvivenza e Viaggio

Tutto quello che ti serve per muoverti tra Lisbona, Porto, Rio o São Paulo con naturalezza.

<ul>
{% assign frasi_posts = site.categories['portoghese'] | where_exp: "item", "item.tags contains 'frasi'" %}
{% if frasi_posts.size > 0 %}
  {% for post in frasi_posts %}
    <li>👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong></li>
  {% endfor %}
{% else %}
  <li><em>Articoli in lavorazione! Le guide per i tuoi viaggi sono in arrivo.</em></li>
{% endif %}
</ul>

---

<div class="cta-soft-box" style="margin-top: 30px;">
<h3>🎯 Entra nel mondo lusofono</h3>
<p>Il portoghese si impara con il ritmo. Scopri l'app che ti permette di scegliere tra la variante brasiliana e quella europea, guidandoti verso la fluency.</p>
<a class="btn-primary" href="{{ '/recensione-babbel/' | relative_url }}">
Leggi la recensione e inizia a studiare oggi
</a>
</div>
