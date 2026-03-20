---
layout: page
title: "Errori e False Friends in Inglese: L'archivio"
description: "Scopri gli errori più comuni degli italiani in inglese e impara a riconoscere i temutissimi false friends."
permalink: /inglese/errori/
bridge_type: errori

next_title: "Hai riconosciuto gli errori: qual è il prossimo passo?"
next_text: "Dopo aver capito cosa evitare, il passo utile è consolidare le basi con una routine costante e un metodo che ti aiuti a parlare in modo più naturale e sicuro."
next_cta1: "Vai alla routine"
next_url1: "/routine/"
next_cta2: "Leggi il metodo consigliato"
next_url2: "/metodo-consigliato/"
next_micro: "Se vuoi invece tornare all’archivio completo dell’inglese,"
next_microlink: "/inglese/"
next_microanchor: "vai all’hub inglese"
---

In questa pagina abbiamo raccolto tutti gli articoli che ti aiuteranno a non commettere più gli scivoloni tipici degli italiani quando parlano inglese. Conosci il tuo nemico (la traduzione letterale)!

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>

<hr>

<ul>
{% assign errori_count = 0 %}
{% for item in site.pages %}
  {% if item.url contains '/inglese/errori/' and item.url != '/inglese/errori/' %}
    {% assign errori_count = errori_count | plus: 1 %}
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

{% if errori_count == 0 %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endif %}
</ul>

{% include promo-box.html type="errori" lang="inglese" %}
