---
layout: default
title: Home
description: "Metodo pratico per imparare una lingua anche con 15 minuti al giorno. Percorso guidato, strumenti testati e strategie sostenibili."
---

<div class="hero-section">
  <div class="wrapper hero-content">
    <h1 class="hero-title">Imparare una lingua non deve essere complicato.</h1>
    <p class="hero-subtitle">
      Metodo strutturato, routine sostenibile e strumenti testati.
      Anche se hai solo 15 minuti al giorno.
    </p>
    <div class="hero-buttons">
      <a href="{{ '/inglese/inglese-da-zero/' | relative_url }}" class="btn-primary hero-btn">
        Inizia da Inglese da Zero
      </a>
      <a href="{{ '/metodo-consigliato/' | relative_url }}" class="btn-secondary hero-btn">
        Scopri il Metodo
      </a>
    </div>
  </div>
</div>

<!-- SEZIONE COME FUNZIONA -->

<div class="wrapper" style="padding: 70px 20px;">
  <h2 style="text-align:center; margin-bottom:50px; border:none;">
    Il percorso FluenteMente
  </h2>

  <div class="home-grid">

    <a href="{{ '/inglese/inglese-da-zero/' | relative_url }}" class="home-card">
      <div class="card-icon">🇬🇧</div>
      <h3>1️⃣ Parti da Zero</h3>
      <p>Costruisci le basi corrette, evita gli errori comuni e segui un ordine logico.</p>
      <span class="card-link">Inizia qui →</span>
    </a>

    <a href="{{ '/inglese/routine-15-minuti/' | relative_url }}" class="home-card">
      <div class="card-icon">⏱</div>
      <h3>2️⃣ Crea una Routine</h3>
      <p>15 minuti al giorno bastano, se usati nel modo giusto.</p>
      <span class="card-link">Scopri il piano →</span>
    </a>

    <a href="{{ '/metodo-consigliato/' | relative_url }}" class="home-card">
      <div class="card-icon">🧭</div>
      <h3>3️⃣ Segui un Metodo</h3>
      <p>Smetti di studiare a caso. Percorso strutturato e progressivo.</p>
      <span class="card-link">Vedi il metodo →</span>
    </a>

  </div>
</div>

<!-- HUB LINGUE -->

<div class="wrapper" style="padding: 40px 20px; border-top: 1px solid var(--border-color);">

  <h2 style="text-align:center; margin-bottom:30px; border:none;">
    Scegli la lingua che vuoi imparare
  </h2>

  <div style="text-align:center;">
    <a href="{{ '/hub-lingue/' | relative_url }}" class="btn-outline">
      Vai all'Hub Lingue
    </a>
  </div>

</div>

<!-- METODO CONSIGLIATO SECTION -->

<div class="wrapper" style="padding: 70px 20px; text-align:center;">

  <h2 style="margin-bottom:20px; border:none;">
    Il metodo che consigliamo per fare progressi reali
  </h2>

  <p style="max-width:600px; margin:0 auto 30px; color:var(--text-light);">
    Se vuoi evitare dispersione e avere un percorso già organizzato,
    abbiamo analizzato diversi strumenti e selezionato quello più completo
    per adulti con poco tempo.
  </p>

  <a href="{{ '/metodo-consigliato/' | relative_url }}" class="btn-primary">
    Scopri il Metodo Consigliato
  </a>

</div>

<!-- ULTIMI ARTICOLI -->

<div class="wrapper recent-posts-section" style="padding: 40px 20px 60px; border-top: 1px solid var(--border-color);">

  <h2 style="margin-bottom: 30px; border:none;">
    Ultimi articoli pubblicati
  </h2>

  <ul class="post-list">
    {% for post in site.posts limit:4 %}
      <li style="margin-bottom: 15px;">
        <span class="post-meta" style="color: var(--text-light); font-size: 0.9em;">
          {{ post.date | date: "%d/%m/%Y" }}
        </span>
        <h3 style="margin: 5px 0 0; font-size: 1.1rem;">
          <a href="{{ post.url | relative_url }}" style="color:#1a202c;">
            {{ post.title | escape }}
          </a>
        </h3>
      </li>
    {% endfor %}
  </ul>

</div>
