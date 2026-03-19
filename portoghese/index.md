---
layout: page
title: "Imparare il Portoghese: Guida, Varianti e Risorse per Italiani"
subtitle: "Dal Portogallo al Brasile: scopri la lingua più musicale del mondo e come parlarla da adulto."
description: "L'hub definitivo per imparare il portoghese. Differenze tra portoghese europeo e brasiliano, pronuncia, falsi amici e frasi utili."
permalink: /portoghese/
---

Il portoghese è una lingua che ti entra nel cuore. Spesso sottovalutato, è la chiave per comunicare in tre continenti e per immergersi in culture straordinarie, dal fado di Lisbona alla bossa nova di Rio de Janeiro.

Per un italiano, il portoghese scritto è quasi comprensibile, ma il parlato nasconde suoni chiusi e ritmi complessi. In questo hub ti guidiamo alla scoperta della lingua lusofona.

{% include promo-box.html type="base" lang="portoghese" %}

---

{% comment %} 
SCUDO DI SICUREZZA: 
1. Prendiamo solo le pagine che hanno categorie (evita crash su nil).
2. Isoliamo quelle del cluster 'portoghese'.
{% endcomment %}
{% assign safe_pages = site.pages | where_exp: "item", "item.categories != nil" %}
{% assign portoghese_pages = safe_pages | where_exp: "item", "item.categories contains 'portoghese'" %}

## 1. Portogallo vs Brasile (Quale scegliere?)

{% assign basi_posts = portoghese_pages | where_exp: "item", "item.tags != nil" | where_exp: "item", "item.tags contains 'basi'" %}

<ul>
{% if basi_posts.size > 0 %}
  {% for post in basi_posts %}
    <li style="margin-bottom: 10px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong></li>
  {% endfor %}
{% else %}
  <li><em>Articoli in lavorazione! Stiamo analizzando le varianti per te.</em></li>
{% endif %}
</ul>

---

## 2. Falsi Amici Portogallo-Italia

{% assign errori_posts = portoghese_pages | where_exp: "item", "item.tags != nil" | where_exp: "item", "item.tags contains 'errori'" %}

<ul>
{% if errori_posts.size > 0 %}
  {% for post in errori_posts %}
    <li style="margin-bottom: 10px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong></li>
  {% endfor %}
{% else %}
  <li><em>Articoli in lavorazione! I falsi amici portoghesi sono in arrivo.</em></li>
{% endif %}
</ul>

---

## 3. La Pronuncia e le Vocali Nasali

{% assign pronuncia_posts = portoghese_pages | where_exp: "item", "item.tags != nil" | where_exp: "item", "item.tags contains 'pronuncia'" %}

<ul>
{% if pronuncia_posts.size > 0 %}
  {% for post in pronuncia_posts %}
    <li style="margin-bottom: 10px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong></li>
  {% endfor %}
{% else %}
  <li><em>Articoli in lavorazione! Stiamo preparando gli audio tutorial.</em></li>
{% endif %}
</ul>

---

## 4. Frasi di Sopravvivenza e Viaggio

{% assign frasi_posts = portoghese_pages | where_exp: "item", "item.tags != nil" | where_exp: "item", "item.tags contains 'frasi'" %}

<ul>
{% if frasi_posts.size > 0 %}
  {% for post in frasi_posts %}
    <li style="margin-bottom: 10px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong></li>
  {% endfor %}
{% else %}
  <li><em>Articoli in lavorazione! Le guide per i tuoi viaggi sono in arrivo.</em></li>
{% endif %}
</ul>

---

<div class="cta-soft-box" style="margin-top: 40px; padding: 30px; background: #f9f9f9; border-left: 5px solid #ff7a59; border-radius: 8px;" markdown="1">

### 🎯 Entra nel mondo lusofono
Il portoghese si impara con il ritmo. Scopri l'app che ti permette di scegliere tra la variante brasiliana e quella europea, guidandoti verso la fluency.

<a class="btn-primary" href="{{ '/recensione-babbel/' | relative_url }}" style="display: inline-block; background: #ff7a59; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px; font-weight: bold; margin-top: 10px;">
Leggi la recensione e inizia a studiare oggi →
</a>

</div>
