---
layout: default
title: Home
---

<div class="hero-section">
  <div class="wrapper hero-content">
    <h1 class="hero-title">Imparare una lingua non deve essere un’impresa impossibile.</h1>
    <p class="hero-subtitle">
      Metodi pratici, routine brevi e strategie basate sulla scienza per parlare davvero,
      anche se hai solo 15 minuti al giorno.
    </p>

    <div class="hero-buttons">
      <a href="{{ '/routine/' | relative_url }}" class="btn-primary hero-btn">Inizia da una routine (15 min)</a>
      <a href="{{ '/metodo-consigliato/' | relative_url }}" class="btn-secondary hero-btn">Vedi il metodo consigliato</a>
    </div>

    <p class="hero-note">
      Sei arrivato/a da Pinterest? Parti dalle routine: sono pensate per essere applicate subito.
    </p>
  </div>
</div>

<div class="wrapper" style="padding: 50px 20px 10px;">
  <h2 style="text-align: center; margin-bottom: 18px; border: none;">Inizia da qui</h2>
  <p style="text-align:center; color: var(--text-light); max-width: 780px; margin: 0 auto 28px;">
    Scegli il percorso più adatto al tuo momento: routine semplice, pagina ponte (metodo) o recensione completa.
  </p>

  <div class="start-grid">
    <a href="{{ '/routine/' | relative_url }}" class="start-card">
      <div class="start-icon">🗓️</div>
      <h3>Routine & piani</h3>
      <p>Routine da 15 minuti, piani 7/30 giorni e studio sostenibile per non mollare.</p>
      <span class="card-link">Vai alle routine →</span>
    </a>

    <a href="{{ '/metodo-consigliato/' | relative_url }}" class="start-card start-card-highlight">
      <div class="start-icon">🧭</div>
      <h3>Metodo consigliato</h3>
      <p>Pagina ponte: criteri chiari + il metodo che consiglio per fare progressi con costanza.</p>
      <span class="card-link">Scopri il metodo →</span>
    </a>

    <a href="{{ '/recensione-babbel/' | relative_url }}" class="start-card">
      <div class="start-icon">⭐</div>
      <h3>Recensione Babbel</h3>
      <p>Analisi completa: pro/contro, prezzi e come usarlo nel modo più efficace.</p>
      <span class="card-link">Leggi la recensione →</span>
    </a>
  </div>
</div>

<div class="wrapper" style="padding: 40px 20px 60px;">
  <h2 style="text-align: center; margin-bottom: 40px; border: none;">Le guide fondamentali di FluenteMente</h2>

  <div class="home-grid">
    <a href="{{ '/5-errori-imparare-lingua/' | relative_url }}" class="home-card">
      <div class="card-icon">🛑</div>
      <h3>I 5 Errori Fatali</h3>
      <p>Studi la grammatica ma non riesci a parlare? Scopri cosa ti blocca e come sbloccarti oggi stesso.</p>
      <span class="card-link">Leggi l'articolo →</span>
    </a>

    <a href="{{ '/risorse/' | relative_url }}" class="home-card">
      <div class="card-icon">🧰</div>
      <h3>Risorse (Guida Definitiva)</h3>
      <p>Una raccolta ordinata: cosa studiare, come farlo e quali strumenti usare senza perdere tempo.</p>
      <span class="card-link">Apri la guida →</span>
    </a>

    <a href="{{ '/recensione-babbel/' | relative_url }}" class="home-card">
      <div class="card-icon">⭐</div>
      <h3>Recensione Babbel</h3>
      <p>Metodo, costi, pro/contro e consigli pratici per integrarlo in una routine da 15 minuti.</p>
      <span class="card-link">Leggi la recensione →</span>
    </a>
  </div>

  <div class="category-links">
    <a class="chip" href="{{ '/routine/' | relative_url }}">Routine</a>
    <a class="chip" href="{{ '/pronuncia/' | relative_url }}">Pronuncia</a>
    <a class="chip" href="{{ '/vocaboli/' | relative_url }}">Vocaboli</a>
    <a class="chip" href="{{ '/listening/' | relative_url }}">Listening</a>
    <a class="chip" href="{{ '/hub-lingue/' | relative_url }}">Hub Lingue</a>
  </div>
</div>

<div class="wrapper recent-posts-section" style="padding: 20px 20px 60px; border-top: 1px solid var(--border-color);">
  <h2 style="margin-bottom: 30px; border: none;">Ultimi articoli pubblicati</h2>
  <ul class="post-list">
    {% for post in site.posts limit:4 %}
    <li style="margin-bottom: 15px;">
      <span class="post-meta" style="color: var(--text-light); font-size: 0.9em;">{{ post.date | date: "%d/%m/%Y" }}</span>
      <h3 style="margin: 5px 0 0; font-size: 1.2rem;">
        <a href="{{ post.url | relative_url }}" style="color: #1a202c;">{{ post.title | escape }}</a>
      </h3>
    </li>
    {% endfor %}
  </ul>
</div>

<style>
/* HERO (Light + Pinterest-friendly) */
.hero-section{
  background: linear-gradient(180deg, #f8fafc 0%, #ffffff 80%);
  border-bottom: 1px solid var(--border-color);
  color: var(--text-main);
  padding: 70px 20px 55px;
  text-align: center;
}
.hero-content{ max-width: 900px; }
.hero
