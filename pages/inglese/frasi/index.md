---
layout: page
title: "Frasi ed Espressioni in Inglese: Tutti gli articoli"
description: "Archivio di frasi pronte all'uso, espressioni per viaggiare e formule per sembrare più fluente."
permalink: /inglese/frasi/
bridge_type: base

next_title: "Hai trovato le frasi giuste: e adesso?"
next_text: "Dopo aver imparato espressioni utili, il passo successivo è inserirle in una routine costante oppure rafforzare il metodo con cui studi per usarle davvero in contesti reali."
next_cta1: "Vai alla routine"
next_url1: "/routine/"
next_cta2: "Leggi il metodo consigliato"
next_url2: "/metodo-consigliato/"
next_micro: "Se vuoi invece tornare all’archivio completo dell’inglese,"
next_microlink: "/inglese/"
next_microanchor: "vai all’hub inglese"
---

Non sai come esprimerti in una certa situazione? In questo archivio trovi tutte le nostre guide dedicate alle frasi e alle espressioni di sopravvivenza in inglese, per lavoro o per i viaggi.

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>

<hr>

<ul>
{% assign frasi_count = 0 %}
{% for item in site.pages %}
  {% if item.url contains '/inglese/frasi/' and item.url != '/inglese/frasi/' %}
    {% assign frasi_count = frasi_count | plus: 1 %}
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

{% if frasi_count == 0 %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endif %}
</ul>

{% include promo-box.html type="base" lang="inglese" %}
