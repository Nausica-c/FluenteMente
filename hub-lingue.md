---
layout: default
title: Hub Lingue
permalink: /hub-lingue/
---

<div class="wrapper" style="padding: 40px 20px;">
    <h1 style="text-align: center; margin-bottom: 20px;">Scegli la lingua che vuoi imparare</h1>
    <p style="text-align: center; color: var(--text-light); max-width: 600px; margin: 0 auto 40px;">Seleziona una delle lingue qui sotto per scoprire le migliori risorse, app, metodi di studio e guide passo-passo per iniziare o perfezionare il tuo livello.</p>

    <div class="language-grid">
        <a href="#" class="lang-card">
            <span class="lang-flag">🇬🇧</span>
            <h2 class="lang-name">Inglese</h2>
            <p class="lang-desc">Imprescindibile per il lavoro e i viaggi.</p>
        </a>
        <a href="#" class="lang-card">
            <span class="lang-flag">🇪🇸</span>
            <h2 class="lang-name">Spagnolo</h2>
            <p class="lang-desc">La seconda lingua madre più parlata al mondo.</p>
        </a>
        <a href="#" class="lang-card">
            <span class="lang-flag">🇫🇷</span>
            <h2 class="lang-name">Francese</h2>
            <p class="lang-desc">La lingua della diplomazia e della cultura.</p>
        </a>
        <a href="#" class="lang-card">
            <span class="lang-flag">🇩🇪</span>
            <h2 class="lang-name">Tedesco</h2>
            <p class="lang-desc">Fondamentale per il business in Europa.</p>
        </a>
        <a href="#" class="lang-card">
            <span class="lang-flag">🇵🇹</span>
            <h2 class="lang-name">Portoghese</h2>
            <p class="lang-desc">Dal fascino di Lisbona all'energia del Brasile.</p>
        </a>
    </div>
</div>

<style>
.language-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-top: 30px;
}
.lang-card {
    background: #fff;
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 30px 20px;
    text-align: center;
    text-decoration: none;
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}
.lang-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    border-color: var(--primary-color);
    text-decoration: none;
}
.lang-flag {
    font-size: 3rem;
    display: block;
    margin-bottom: 15px;
}
.lang-name {
    color: #1a202c;
    margin-bottom: 10px;
    font-size: 1.4rem;
    border: none;
}
.lang-desc {
    color: var(--text-light);
    font-size: 0.95rem;
    margin: 0;
}
</style>
