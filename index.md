---
layout: default
title: "FluenteMente — Viaggio nel mondo delle lingue (ma con metodo)"
description: "Impara inglese da adulto con poco tempo: roadmap chiara, routine brevi e strumenti testati. Un viaggio nel mondo delle lingue, ma senza caos."
---

{% include header.html %}

<main class="page-content">

  <!-- HERO -->
  <section class="hero-clean">
    <div class="wrapper hero-clean__inner">
      <h1 class="hero-clean__title">
        🌍 Viaggio nel mondo delle lingue.<br />
        Ma con un metodo semplice (da adulti).
      </h1>

      <p class="hero-clean__subtitle">
        Se vuoi imparare <strong>inglese</strong> con poco tempo e senza caos, qui trovi una roadmap chiara,
        routine brevi e strumenti testati. Anche se hai solo <strong>15 minuti al giorno</strong>.
      </p>

      <div class="hero-clean__actions">
        <a class="btn-primary" href="{{ '/inglese-da-zero/' | relative_url }}">Inizia da qui</a>
        <a class="btn-outline" href="{{ '/metodo-consigliato/' | relative_url }}">Scopri il Metodo</a>
      </div>

      <div class="hero-clean__meta" aria-label="Punti chiave">
        <span class="hero-pill">⏱ 15 min/giorno</span>
        <span class="hero-pill">🧠 Sistema anti-caos</span>
        <span class="hero-pill">🗣️ Focus conversazione</span>
      </div>
    </div>
  </section>

  <!-- PROBLEMA -->
  <section class="section-alt">
    <div class="wrapper">
      <h2 class="section-title">Perché non diventi fluente (anche se “studi”)</h2>
      <p class="section-subtitle">
        Il problema quasi mai è la mancanza di impegno. È la mancanza di un sistema ripetibile.
      </p>

      <div class="bullet-grid">
        <div class="bullet-card">
          <h3>📚 Troppa teoria</h3>
          <p>Conosci le regole, ma quando devi parlare ti blocchi.</p>
        </div>

        <div class="bullet-card">
          <h3>🔁 Pochi ripassi</h3>
          <p>Impari oggi, dimentichi domani: manca ripetizione intelligente.</p>
        </div>

        <div class="bullet-card">
          <h3>🎲 Studio casuale</h3>
          <p>Ogni giorno decidi da zero cosa fare. Risultato: molli.</p>
        </div>
      </div>

      <div class="solution-box">
        <h3>✅ La soluzione FluenteMente</h3>
        <p>
          Routine brevi (15 min/giorno), strumenti strutturati e una progressione che non ti faccia mai chiedere:
          “E oggi cosa studio?”
        </p>
      </div>
    </div>
  </section>

  <!-- START HERE (FUNNEL) -->
  <section class="section-soft">
    <div class="wrapper">
      <h2 class="section-title">Da dove vuoi iniziare?</h2>
      <p class="section-subtitle">Scegli il percorso più adatto alla tua situazione (senza dispersione).</p>

      <div class="start-grid">
        <a class="start-card start-card-highlight" href="{{ '/inglese-da-zero/' | relative_url }}">
          <div class="start-icon" aria-hidden="true">🚀</div>
          <h3>Inglese da Zero</h3>
          <p>La guida completa per partire bene, anche se stai ricominciando.</p>
        </a>

        <a class="start-card" href="{{ '/routine/' | relative_url }}">
          <div class="start-icon" aria-hidden="true">⏱</div>
          <h3>Routine 15 minuti</h3>
          <p>Schema pratico e sostenibile per studiare ogni giorno senza stress.</p>
        </a>

        <a class="start-card" href="{{ '/metodo-consigliato/' | relative_url }}">
          <div class="start-icon" aria-hidden="true">🧭</div>
          <h3>Il Metodo</h3>
          <p>I 4 pilastri per imparare davvero: progressione, contesto, ripasso, routine.</p>
        </a>

        <a class="start-card" href="{{ '/recensione-babbel/' | relative_url }}">
          <div class="start-icon" aria-hidden="true">⭐</div>
          <h3>Strumenti</h3>
          <p>Quale app funziona davvero per adulti? Ecco la nostra scelta e perché.</p>
        </a>
      </div>

      <div class="category-links" aria-label="Sezioni utili">
        <a class="chip" href="{{ '/inglese-da-zero/' | relative_url }}">Iniziare</a>
        <a class="chip" href="{{ '/routine/' | relative_url }}">Routine</a>
        <a class="chip" href="{{ '/recensione-babbel/' | relative_url }}">Recensione</a>
        <a class="chip" href="{{ '/risorse/' | relative_url }}">Risorse</a>
      </div>
    </div>
  </section>

  <!-- GUIDE FONDAMENTALI (ridotte e più conversion-first) -->
  <section class="section-alt">
    <div class="wrapper">
      <h2 class="section-title">Le guide fondamentali</h2>
      <p class="section-subtitle">
        Se vuoi risultati veri, parti da queste. Sono le pagine che “reggono” tutto il percorso.
      </p>

      <div class="guide-list">
        <a class="guide-link" href="{{ '/inglese-da-zero/' | relative_url }}">
          Inglese da Zero: i primi passi per iniziare (o ricominciare)
        </a>
        <a class="guide-link" href="{{ '/capisco-ma-non-parlo/' | relative_url }}">
          Capisco l’inglese ma non riesco a parlarlo: come sbloccarsi
        </a>
        <a class="guide-link" href="{{ '/routine/' | relative_url }}">
          Routine Inglese: 15 minuti al giorno per migliorare davvero
        </a>
        <a class="guide-link" href="{{ '/recensione-babbel/' | relative_url }}">
          Babbel: recensione completa e per chi conviene davvero
        </a>
      </div>

      <p style="margin-top:18px; color: var(--text-light);">
        <strong>Nota:</strong> questo mese focus <strong>Inglese</strong>. Le altre lingue arrivano dopo (senza caos).
      </p>
    </div>
  </section>

  <!-- ULTIMI ARTICOLI -->
  <section class="section-soft">
    <div class="wrapper">
      <h2 class="section-title">Ultimi articoli</h2>
      <p class="section-subtitle">Aggiornamenti, guide e strategie pratiche.</p>

      <div aria-label="Lista ultimi articoli">
        {% assign posts_to_show = site.posts | where_exp: "p", "p.draft != true" %}
        {% for post in posts_to_show limit: 6 %}
          <div class="post-row">
            <span class="post-row__date">{{ post.date | date: "%d/%m/%Y" }}</span>
            <a class="post-row__title" href="{{ post.url | relative_url }}">{{ post.title }}</a>
          </div>
        {% endfor %}
      </div>

      <div class="hero-clean__actions" style="margin-top:18px;">
        <a class="btn-outline" href="{{ '/archivio/' | relative_url }}">Vedi tutti gli articoli</a>
        <a class="btn-primary" href="{{ '/metodo-consigliato/' | relative_url }}">Vai al Metodo</a>
      </div>
    </div>
  </section>

  <!-- DISCLAIMER SOFT -->
  <section class="section-alt">
    <div class="wrapper">
      <div class="disclaimer-inline" role="note" aria-label="Nota affiliazioni">
        <div class="disclaimer-icon" aria-hidden="true">ℹ️</div>
        <p class="disclaimer-text">
          <strong>Nota</strong> — Alcuni link in questo sito possono essere affiliati.
          Se acquisti tramite questi link potrei ricevere una piccola commissione, senza costi extra per te.
        </p>
      </div>
    </div>
  </section>

</main>

{% include footer.html %}
