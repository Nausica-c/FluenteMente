# Controlli prima della pubblicazione

## Contenuti
- [ ] Rileggere grammatica, esempi e traduzioni con una revisione linguistica finale.
- [ ] Verificare che titolo SEO e meta description siano coerenti con la pagina effettiva.
- [ ] Controllare gli esempi in inglese con fonti linguistiche affidabili prima della pubblicazione.
- [ ] Verificare che ciascun contenuto mantenga l’intento specifico indicato nel brief e non si sovrapponga inutilmente agli altri.

## Jekyll e destinazioni
- [ ] Unire i file alla base grafica conservata, senza sovrascrivere CSS, layout o include.
- [ ] Verificare il rendering della home page e dei 30 permalink con il baseurl `/FluenteMente`.
- [ ] Controllare che i link del menu, la pagina informativa sull’affiliazione e le pagine di servizio esistano oppure aggiornare la navigazione.
- [ ] Confrontare i permalink con gli URL pubblicati e predisporre redirect per eventuali URL sostituiti.
- [ ] Aprire i 30 URL generati in anteprima e verificare tutti i link interni.

## Affiliazione e Babbel
- [ ] Verificare le funzioni, i prezzi, il rinnovo, la disdetta e le condizioni correnti di Babbel da fonti ufficiali.
- [ ] Inserire l’URL affiliato corretto soltanto dopo averlo verificato.
- [ ] Mantenere una disclosure chiara vicino al link affiliato e verificare che rimandi alla pagina informativa del sito.
- [ ] Non pubblicare sconti, prove o promesse di risultato non confermati.

## Pubblicazione e SEO
- [ ] Controllare sitemap, canonical, metadata, immagini social e stato `launch_mode` della base grafica.
- [ ] Verificare `index, follow`, canonical e sitemap per i contenuti editoriali. Mantenere temporaneamente `noindex, follow` e `sitemap: false` sulle pagine di servizio con campi incompleti.


## Pagine di servizio: controlli obbligatori

- [ ] Compilare nome/denominazione del titolare e recapito reale in `privacy.md`, `chi-siamo.md` e `disclaimer.md`.
- [ ] Verificare i tempi di conservazione e i ruoli applicabili ai fornitori sulla base dei servizi effettivamente usati.
- [ ] Testare la versione online con un browser pulito: cookie, local storage, richieste di rete e contenuti caricati da terzi; documentare nome, fornitore, finalità, durata e categoria dei cookie rilevati.
- [ ] Se sono presenti strumenti non tecnici, valutare una piattaforma di gestione del consenso e bloccare tali strumenti prima del consenso, quando richiesto.
- [ ] Verificare ogni link affiliato attivo, il contratto/programmazione utilizzata e la disclosure vicina al collegamento.
- [ ] Se si aggiungono analytics, form, newsletter, embed o pixel, aggiornare privacy e cookie prima di abilitarli.
- [ ] Compilare un build Jekyll e verificare tutti i permalink e la visualizzazione mobile.
- [ ] Completare i campi reali delle pagine di servizio e i controlli tecnici prima del deploy definitivo; il repository usa ora `launch_mode: false` per rendere indicizzabili i contenuti editoriali.

Riferimenti ufficiali consultati per predisporre le bozze: GDPR (Regolamento UE 2016/679), Garante Privacy — Linee guida cookie del 10 giugno 2021, documentazione GitHub Pages e GitHub Privacy Statement, Regolamento Digital Chart dello IAP. Le pagine sono bozze operative, non certificano da sole la conformità legale della configurazione finale.
