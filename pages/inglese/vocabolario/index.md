---
layout: page
title: "Vocabolario Inglese: Liste di parole per livello (A1 - C1)"
description: "Tutte le liste di vocaboli inglesi divise per livello, con guide pratiche per studiare le parole che servono davvero."
permalink: /inglese/vocabolario/
bridge_type: vocabolario

next_title: "Hai trovato le parole giuste: qual è il prossimo passo?"
next_text: "Dopo aver studiato il vocabolario, il passo utile è inserirlo in una routine costante e collegarlo a un metodo che ti aiuti a usarlo davvero in frasi e situazioni reali."
next_cta1: "Vai alla routine"
next_url1: "/routine/"
next_cta2: "Leggi il metodo consigliato"
next_url2: "/metodo-consigliato/"
next_micro: "Se vuoi invece tornare all’archivio completo dell’inglese,"
next_microlink: "/inglese/"
next_microanchor: "vai all’hub inglese"
---

In questa pagina trovi tutte le nostre guide di vocabolario inglese organizzate per livello. L’obiettivo non è memorizzare liste infinite, ma imparare parole utili e davvero riutilizzabili nella vita quotidiana, nello studio, nei viaggi e nel lavoro.

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>

<hr>

{% assign vocab_pages = "" | split: "" %}
{% assign unclassified_pages = "" | split: "" %}
{% assign a1_pages = "" | split: "" %}
{% assign a2_pages = "" | split: "" %}
{% assign b_pages = "" | split: "" %}
{% assign c1_pages = "" | split: "" %}

{% for item in site.pages %}
  {% if item.url contains '/inglese/vocabolario/' and item.url != '/inglese/vocabolario/' %}
    {% assign vocab_pages = vocab_pages | push: item %}

    {% if item.url contains '/a1/' %}
      {% assign a1_pages = a1_pages | push: item %}
    {% elsif item.url contains '/a2/' %}
      {% assign a2_pages = a2_pages | push: item %}
    {% elsif item.url contains '/b1/' or item.url contains '/b2/' %}
      {% assign b_pages = b_pages | push: item %}
    {% elsif item.url contains '/c1/' %}
      {% assign c1_pages = c1_pages | push: item %}
    {% else %}
      {% assign unclassified_pages = unclassified_pages | push: item %}
    {% endif %}
  {% endif %}
{% endfor %}

{% if unclassified_pages.size > 0 %}
## 🆕 Nuovi arrivi (In aggiornamento)

<ul>
{% for item in unclassified_pages %}
  <li style="margin-bottom: 15px;">
    👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong><br>
    <small style="color: #555;">
      {% if item.description %}
        {{ item.description }}
      {% else %}
        {{ item.excerpt | strip_html | truncatewords: 25 }}
      {% endif %}
    </small>
  </li>
{% endfor %}
</ul>

<hr>
{% endif %}

## 🟢 Livello A1 (Principiante)

<ul>
{% for item in a1_pages %}
  <li style="margin-bottom: 15px;">
    👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong><br>
    <small style="color: #555;">
      {% if item.description %}
        {{ item.description }}
      {% else %}
        {{ item.excerpt | strip_html | truncatewords: 25 }}
      {% endif %}
    </small>
  </li>
{% else %}
  <li><em>Nessun articolo per questo livello.</em></li>
{% endfor %}
</ul>

<hr>

## 🟡 Livello A2 (Pre-Intermedio)

<ul>
{% for item in a2_pages %}
  <li style="margin-bottom: 15px;">
    👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong><br>
    <small style="color: #555;">
      {% if item.description %}
        {{ item.description }}
      {% else %}
        {{ item.excerpt | strip_html | truncatewords: 25 }}
      {% endif %}
    </small>
  </li>
{% else %}
  <li><em>Nessun articolo per questo livello.</em></li>
{% endfor %}
</ul>

<hr>

## 🟠 Livelli B1 / B2 (Intermedio)

<ul>
{% for item in b_pages %}
  <li style="margin-bottom: 15px;">
    👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong><br>
    <small style="color: #555;">
      {% if item.description %}
        {{ item.description }}
      {% else %}
        {{ item.excerpt | strip_html | truncatewords: 25 }}
      {% endif %}
    </small>
  </li>
{% else %}
  <li><em>Nessun articolo per questo livello.</em></li>
{% endfor %}
</ul>

<hr>

## 🔴 Livello C1 (Avanzato)

<ul>
{% for item in c1_pages %}
  <li style="margin-bottom: 15px;">
    👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong><br>
    <small style="color: #555;">
      {% if item.description %}
        {{ item.description }}
      {% else %}
        {{ item.excerpt | strip_html | truncatewords: 25 }}
      {% endif %}
    </small>
  </li>
{% else %}
  <li><em>Nessun articolo per questo livello.</em></li>
{% endfor %}
</ul>

{% include promo-box.html type="vocabolario" lang="inglese" %}
