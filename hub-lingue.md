---
layout: default
title: Hub Lingue
seo_title: "Scegli la Lingua da Imparare | Guide e Metodo FluenteMente"
description: "Scegli la lingua che vuoi imparare: guide complete, routine, consigli pratici e metodo consigliato."
permalink: /hub-lingue/
---

<div class="wrapper hub-wrapper">

  <header class="hub-header">
    <h1>Quale lingua vuoi imparare?</h1>
    <p>
      Scegli una lingua e troverai:
      guide pratiche, errori comuni, vocaboli essenziali,
      piani di studio da 15 minuti e il metodo che consigliamo per fare progressi reali.
    </p>
  </header>

  <div class="language-grid">

    <!-- INGLESE -->
    <a href="{{ '/inglese/' | relative_url }}" class="lang-card">
      <div class="lang-emoji">🇬🇧</div>
      <h2>Inglese</h2>
      <p>La lingua globale: lavoro, viaggi e comunicazione internazionale.</p>
      <span class="lang-cta">Scopri il percorso →</span>
    </a>

    <!-- SPAGNOLO -->
    <a href="{{ '/spagnolo/' | relative_url }}" class="lang-card">
      <div class="lang-emoji">🇪🇸</div>
      <h2>Spagnolo</h2>
      <p>Perfetto per viaggiare e comunicare in mezzo mondo.</p>
      <span class="lang-cta">Scopri il percorso →</span>
    </a>

    <!-- FRANCESE -->
    <a href="{{ '/francese/' | relative_url }}" class="lang-card">
      <div class="lang-emoji">🇫🇷</div>
      <h2>Francese</h2>
      <p>Cultura, diplomazia e opportunità internazionali.</p>
      <span class="lang-cta">Scopri il percorso →</span>
    </a>

    <!-- TEDESCO -->
    <a href="{{ '/tedesco/' | relative_url }}" class="lang-card">
      <div class="lang-emoji">🇩🇪</div>
      <h2>Tedesco</h2>
      <p>Fondamentale per business e carriera in Europa.</p>
      <span class="lang-cta">Scopri il percorso →</span>
    </a>

    <!-- PORTOGHESE -->
    <a href="{{ '/portoghese/' | relative_url }}" class="lang-card">
      <div class="lang-emoji">🇵🇹</div>
      <h2>Portoghese</h2>
      <p>Dall’Europa al Brasile: una lingua in forte crescita.</p>
      <span class="lang-cta">Scopri il percorso →</span>
    </a>

  </div>

  <!-- Sezione Metodo -->
  <section class="hub-method">
    <h2>Non sai da dove iniziare?</h2>
    <p>
      Prima ancora di scegliere la lingua, assicurati di avere
      un metodo strutturato e sostenibile.
    </p>
    <div class="hub-buttons">
      <a href="{{ '/metodo-consigliato/' | relative_url }}" class="btn-outline">
        Vedi il metodo consigliato
      </a>
      <a href="{{ '/recensione-babbel/' | relative_url }}" class="btn-primary">
        Leggi la recensione Babbel
      </a>
    </div>
  </section>

</div>

<style>
.hub-wrapper {
  padding: 50px 20px 60px;
}

.hub-header {
  text-align: center;
  max-width: 750px;
  margin: 0 auto 50px;
}

.hub-header h1 {
  font-size: 2.6rem;
  margin-bottom: 15px;
}

.hub-header p {
  color: var(--text-light);
  font-size: 1.1rem;
}

.language-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 24px;
  margin-bottom: 60px;
}

.lang-card {
  background: #fff;
  border: 1px solid var(--border-color);
  border-radius: 14px;
  padding: 28px 22px;
  text-align: center;
  text-decoration: none;
  color: var(--text-main);
  transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
}

.lang-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 25px rgba(0,0,0,0.05);
  border-color: var(--primary-color);
  text-decoration: none;
}

.lang-emoji {
  font-size: 3rem;
  margin-bottom: 14px;
}

.lang-card h2 {
  margin: 0 0 10px;
  font-size: 1.4rem;
  border: none;
  color: #1a202c;
}

.lang-card p {
  color: var(--text-light);
  font-size: 0.95rem;
  margin-bottom: 14px;
}

.lang-cta {
  color: var(--primary-color);
  font-weight: 700;
  font-size: .9rem;
}

.hub-method {
  text-align: center;
  background: #ffffff;
  border: 1px solid var(--border-color);
  padding: 40px;
  border-radius: 16px;
}

.hub-method h2 {
  margin-bottom: 10px;
  border: none;
}

.hub-method p {
  color: var(--text-light);
  margin-bottom: 20px;
}

.hub-buttons {
  display: flex;
  justify-content: center;
  gap: 15px;
  flex-wrap: wrap;
}

@media (max-width: 600px) {
  .hub-header h1 {
    font-size: 2rem;
  }
}
</style>
