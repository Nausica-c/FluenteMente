---
layout: page
title: "Inglese in Viaggio: L'archivio completo"
description: "Tutte le risorse per viaggiare senza ansie: aeroporto, hotel, ristorante e indicazioni stradali."
permalink: /inglese/viaggio/
bridge_type: viaggio

next_title: "Hai visto le frasi utili per viaggiare: qual è il prossimo passo?"
next_text: "Dopo aver esplorato le risorse per l’inglese in viaggio, il passo utile è consolidare il metodo e trasformare queste espressioni in una routine pratica che ti aiuti davvero sul campo."
next_cta1: "Vai alla routine"
next_url1: "/routine/"
next_cta2: "Leggi il metodo consigliato"
next_url2: "/metodo-consigliato/"
next_micro: "Se vuoi invece tornare all’archivio completo dell’inglese,"
next_microlink: "/inglese/"
next_microanchor: "vai all’hub inglese"
---

In questa sezione trovi tutte le nostre guide pratiche per affrontare i tuoi viaggi all'estero con sicurezza, gestendo ogni situazione: dal check-in in aeroporto all'ordinazione al ristorante.

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>

<hr>

<ul>
{% assign viaggio_count = 0 %}
{% for item in site.pages %}
  {% if item.url contains '/inglese/viaggio/' and item.url != '/inglese/viaggio/' %}
    {% assign viaggio_count = viaggio_count | plus: 1 %}
    <li style="margin-bottom: 15px;">
      👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
      <br><small style="color: #555;">
        {% if item.description %}
          {{ item.description }}
        {% else %}
          {{ item.excerpt | strip_html | truncatewords: 25 }}
        {% endif %}
      </small>
    </li>
  {% endif %}
{% endfor %}

{% if viaggio_count == 0 %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endif %}
</ul>

{% include promo-box.html type="viaggio" lang="inglese" %}
