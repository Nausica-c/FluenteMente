---
layout: page
title: "Imparare il Francese: Guida, Errori e Risorse per Italiani"
subtitle: "Dalle insidiose nasali ai falsi amici: impara a parlare il francese vero (oltre la scuola)."
description: "L'hub definitivo per imparare il francese da italiani. Risorse su pronuncia, grammatica, falsi amici e frasi utili per viaggiare in Francia e non solo."
permalink: /francese/
---

Molti italiani sono convinti che il francese sia "italiano con la *u* e le parole che finiscono in consonante". Questo approccio superficiale è il modo più veloce per non farsi capire a Parigi o Montreal.

Il francese è una lingua di estrema precisione, con una fonetica che non perdona e una struttura grammaticale che, pur somigliando alla nostra, nasconde insidie ovunque. In questo hub raccogliamo le guide per aiutarti a dominare la lingua di Molière.

---

## 1. Basi e Mindset (L'approccio corretto)

Il francese richiede un orecchio attento e la voglia di mettersi in gioco con suoni che in italiano non esistono.

<ul>
{% assign basi_posts = site.categories['francese'] | where_exp: "item", "item.tags contains 'basi'" %}
{% if basi_posts.size > 0 %}
  {% for post in basi_posts %}
    <li>👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong></li>
  {% endfor %}
{% else %}
  <li><em>Articoli in lavorazione! Stiamo preparando le basi del francese per te.</em></li>
{% endif %}
</ul>

---

## 2. Falsi Amici ed Errori Comuni

Attenzione: se dici che una cosa è "morbida", in francese stai dicendo che è "morta" (*morbide*). Scopri come evitare i tranelli più comuni.

<ul>
{% assign errori_posts = site.categories['francese'] | where_exp: "item", "item.tags contains 'errori'" %}
{% if errori_posts.size > 0 %}
  {% for post in errori_posts %}
    <li>👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong></li>
  {% endfor %}
{% else %}
  <li><em>Articoli in lavorazione! La lista dei faux-amis è in arrivo.</em></li>
{% endif %}
</ul>

---

## 3. Pronuncia e Suoni

Dalle vocali nasali alla "R" francese: impara a posizionare la bocca per smettere di sembrare un turista e iniziare a sembrare un locale.

<ul>
{% assign pronuncia_posts = site.categories['francese'] | where_exp: "item", "item.tags contains 'pronuncia'" %}
{% if pronuncia_posts.size > 0 %}
  {% for post in pronuncia_posts %}
    <li>👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong></li>
  {% endfor %}
{% else %}
  <li><em>Articoli in lavorazione! Stiamo preparando le guide fonetiche.</em></li>
{% endif %}
</ul>

---

## 4. Frasi Utili e Vocabolario

Dall'ordinare un *croissant* al gestire una conversazione di lavoro: le frasi fatte che ti salvano la vita.

<ul>
{% assign frasi_posts = site.categories['francese'] | where_exp: "item", "item.tags contains 'frasi'" %}
{% if frasi_posts.size > 0 %}
  {% for post in frasi_posts %}
    <li>👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong></li>
  {% endfor %}
{% else %}
  <li><em>Articoli in lavorazione! Le guide di viaggio sono in arrivo.</em></li>
{% endif %}
</ul>

---

<div class="cta-soft-box" style="margin-top: 30px;">
<h3>🎯 Parla francese con sicurezza</h3>
<p>Il francese è una lingua che va ascoltata e ripetuta. Scopri l'app che consigliamo per padroneggiare la pronuncia e la grammatica francese senza stress.</p>
<a class="btn-primary" href="{{ '/recensione-babbel/' | relative_url }}">
Leggi la recensione e inizia a studiare oggi
</a>
</div>
