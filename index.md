---
layout: default
title: Home
description: "Metodo pratico per imparare una lingua anche con 15 minuti al giorno. Percorsi guidati, risorse testate e strategia sostenibile."
---

<!-- HERO -->
<section class="hero-clean">
  <div class="wrapper hero-clean__inner">
    <h1 class="hero-clean__title">Imparare una lingua non deve essere un caos.</h1>
    <p class="hero-clean__subtitle">
      Metodo chiaro, routine sostenibile e strumenti testati.
      Anche se hai solo 15 minuti al giorno.
    </p>

    <div class="hero-clean__actions">
      <a href="{{ '/risorse/' | relative_url }}" class="btn-primary">Inizia da qui</a>
      <a href="{{ '/hub-lingue/' | relative_url }}" class="btn-outline">Scegli una lingua</a>
    </div>

    <div class="hero-clean__meta">
      <span class="hero-pill">⏱ 15 min/giorno</span>
      <span class="hero-pill">🧠 Metodo in 4 pilastri</span>
      <span class="hero-pill">🚀 Percorso guidato</span>
    </div>
  </div>
</section>

<!-- PROBLEMA / SOLUZIONE -->
<section class="section-soft">
  <div class="wrapper">
    <h2 class="section-title">Perché non diventi fluente (anche se “studi”)</h2>
    <p class="section-subtitle">
      Il problema quasi sempre non è la mancanza di impegno. È la mancanza di un sistema.
    </p>

    <div class="bullet-grid">
      <div class="bullet-card">
        <h3>📚 Troppa teoria</h3>
        <p>Conosci le regole, ma non sai ordinare un caffè.</p>
      </div>

      <div class="bullet-card">
        <h3>🔁 Pochi ripassi</h3>
        <p>Impari oggi, dimentichi domani perché manca ripetizione intelligente.</p>
      </div>

      <div class="bullet-card">
        <h3>😵 Studio casuale</h3>
        <p>Ogni giorno decidi da zero cosa fare. Risultato: molli.</p>
      </div>
    </div>

    <div class="solution-box">
      <h3>✅ La soluzione FluenteMente</h3>
      <p>
        Routine brevi (15 min/giorno), strumenti strutturati e una progressione che non ti faccia mai chiedere:
        <em>“E oggi cosa studio?”</em>
      </p>
    </div>
  </div>
</section>

<!-- START HERE -->
<section class="section-alt">
  <div class="wrapper">
    <h2 class="section-title">🗺️ Da dove vuoi iniziare?</h2>
    <p class="section-subtitle">Scegli il percorso più adatto alla tua situazione.</p>

    <div class="start-grid">
      <div class="start-card start-card-highlight">
        <div class="start-icon">🧠</div>
        <h3>Il Metodo</h3>
        <p>Scopri i 4 pilastri per imparare davvero e costruire una routine che dura.</p>
        <a href="{{ '/metodo-consigliato/' | relative_url }}" class="card-link">👉 Scopri il Metodo</a>
      </div>

      <div class="start-card">
        <div class="start-icon">🌍</div>
        <h3>La Pratica</h3>
        <p>Scegli la lingua e segui un percorso completo: pronuncia, vocaboli, routine.</p>
        <a href="{{ '/hub-lingue/' | relative_url }}" class="card-link">👉 Vai all’Hub Lingue</a>
      </div>

      <div class="start-card">
        <div class="start-icon">⭐</div>
        <h3>Gli Strumenti</h3>
        <p>Quale app funziona davvero per adulti? Qui trovi la nostra scelta.</p>
        <a href="{{ '/recensione-babbel/' | relative_url }}" class="card-link">👉 Recensione Babbel</a>
      </div>
    </div>
  </div>
</section>

<!-- GUIDE FONDAMENTALI -->
<section class="section-soft">
  <div class="wrapper">
    <h2 class="section-title">📚 Le guide fondamentali</h2>
    <p class="section-subtitle">
      Le letture obbligatorie per smettere di essere un “eterno principiante” e iniziare a parlare sul serio.
    </p>

    <div class="guide-list">
      <a href="{{ '/inglese/inglese-da-zero/' | relative_url }}" class="guide-link">
        🇬🇧 Inglese da Zero: i primi passi per iniziare (o ricominciare)
      </a>

      <a href="{{ '/come-imparare-lingua-da-zero/' | relative_url }}" class="guide-link">
        🧭 Come imparare una lingua da zero: la roadmap definitiva
      </a>

      <a href="{{ '/metodo-consigliato/' | relative_url }}" class="guide-link">
        🧠 Il Metodo Consigliato: progressione, contesto, ripasso, routine
      </a>
    </div>

    <div class="category-links">
      <a class="chip" href="{{ '/inglese/' | relative_url }}">🇬🇧 Inglese</a>
      <a class="chip" href="{{ '/spagnolo/' | relative_url }}">🇪🇸 Spagnolo</a>
      <a class="chip" href="{{ '/francese/' | relative_url }}">🇫🇷 Francese</a>
      <a class="chip" href="{{ '/tedesco/' | relative_url }}">🇩🇪 Tedesco</a>
      <a class="chip" href="{{ '/portoghese/' | relative_url }}">🇵🇹 Portoghese</a>
    </div>
  </div>
</section>

<!-- ULTIMI ARTICOLI -->
<section class="section-alt">
  <div class="wrapper">
    <h2 class="section-title">📰 Ultimi articoli</h2>
    <p class="section-subtitle">Aggiornamenti, guide e strategie pratiche.</p>

    <ul class="post-list">
      {% for post in site.posts limit:6 %}
        <li class="post-row">
          <span class="post-row__date">{{ post.date | date: "%d/%m/%Y" }}</span>
          <a class="post-row__title" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
        </li>
      {% endfor %}
    </ul>
  </div>
</section>
