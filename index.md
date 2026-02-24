---
layout: default
title: Home
---

<div class="hero-section">
    <div class="wrapper hero-content">
        <h1 class="hero-title">Imparare una lingua non deve essere un'impresa impossibile.</h1>
        <p class="hero-subtitle">Scopri metodi pratici, strumenti testati e strategie basate sulla scienza per imparare a parlare davvero, anche se hai solo 15 minuti al giorno.</p>
        <div class="hero-buttons">
            <a href="{{ '/risorse/' | relative_url }}" class="btn-primary hero-btn">Inizia dalla Guida Definitiva</a>
            <a href="{{ '/hub-lingue/' | relative_url }}" class="btn-secondary hero-btn">Scegli una Lingua</a>
        </div>
    </div>
</div>

<div class="wrapper" style="padding: 60px 20px;">
    <h2 style="text-align: center; margin-bottom: 40px; border: none;">Le guide fondamentali di FluenteMente</h2>
    
    <div class="home-grid">
        
        <a href="{{ '/5-errori-imparare-lingua/' | relative_url }}" class="home-card">
            <div class="card-icon">🛑</div>
            <h3>I 5 Errori Fatali</h3>
            <p>Studi la grammatica ma non riesci a parlare? Scopri cosa ti blocca e come sbloccarti oggi stesso.</p>
            <span class="card-link">Leggi l'articolo →</span>
        </a>

        <a href="{{ '/migliori-app-lingue-2026/' | relative_url }}" class="home-card">
            <div class="card-icon">📱</div>
            <h3>Le 3 Migliori App del 2026</h3>
            <p>Abbiamo testato Duolingo, Rosetta Stone e Babbel. Scopri quale funziona davvero per gli adulti.</p>
            <span class="card-link">Confronta le app →</span>
        </a>

        <a href="{{ '/recensione-babbel/' | relative_url }}" class="home-card">
            <div class="card-icon">⭐</div>
            <h3>Recensione Babbel</h3>
            <p>Analisi completa del metodo, dei costi e del perché il piano Lifetime è l'investimento più intelligente.</p>
            <span class="card-link">Leggi la recensione →</span>
        </a>

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
.hero-section {
    background-color: #1a202c; /* Sfondo scuro per far risaltare il testo */
    color: #ffffff;
    padding: 80px 20px;
    text-align: center;
}

.hero-content {
    max-width: 800px;
}

.hero-title {
    font-size: 3rem;
    color: #ffffff;
    line-height: 1.2;
    margin-bottom: 20px;
}

.hero-subtitle {
    font-size: 1.25rem;
    color: #cbd5e1;
    margin-bottom: 40px;
}

.hero-buttons {
    display: flex;
    gap: 20px;
    justify-content: center;
    flex-wrap: wrap;
}

.hero-btn {
    margin-top: 0;
}

.btn-secondary {
    display: inline-block;
    background-color: transparent;
    color: #ffffff;
    padding: 15px 35px;
    font-size: 1.1rem;
    font-weight: bold;
    border-radius: 50px;
    text-decoration: none;
    border: 2px solid #ffffff;
    transition: background-color 0.3s, color 0.3s;
}

.btn-secondary:hover {
    background-color: #ffffff;
    color: #1a202c;
    text-decoration: none;
}

.home-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
}

.home-card {
    background: #ffffff;
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 30px;
    text-decoration: none;
    color: var(--text-main);
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    display: flex;
    flex-direction: column;
}

.home-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    border-color: var(--primary-color);
    text-decoration: none;
}

.card-icon {
    font-size: 2.5rem;
    margin-bottom: 15px;
}

.home-card h3 {
    color: #1a202c;
    margin-top: 0;
    margin-bottom: 10px;
    font-size: 1.3rem;
}

.home-card p {
    font-size: 0.95rem;
    color: var(--text-light);
    flex-grow: 1;
}

.card-link {
    color: var(--primary-color);
    font-weight: bold;
    font-size: 0.9rem;
    margin-top: 15px;
}

/* Adattamenti per mobile */
@media screen and (max-width: 600px) {
    .hero-title { font-size: 2.2rem; }
    .hero-buttons { flex-direction: column; }
    .hero-btn { width: 100%; text-align: center; }
}
</style>
