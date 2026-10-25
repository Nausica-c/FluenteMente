# FluenteMente — interventi al funnel Babbel

Data: 25 ottobre 2026  
Ambito: copy, rilevanza delle CTA, tracciabilità del link affiliato e prevenzione dei duplicati di build.

## Modifiche applicate

- Le CTA soft verso la guida Babbel sono mantenute negli articoli a maggiore affinità con routine e metodo di studio (PIN01, PIN20, PIN21 e PIN23). Sono state rimosse dalle mini-lezioni linguistiche e dagli articoli situazionali per evitare che il messaggio commerciale compaia quasi automaticamente dopo ogni lezione. PIN30 continua a collegarsi alla guida Babbel in modo contestuale.
- Il componente condiviso `_includes/babbel-next-step.html` usa un titolo e un testo del collegamento più chiari, senza linguaggio urgente o promesse.
- La guida PIN27 è stata ampliata con criteri pratici per valutare Babbel, possibili limiti, una griglia di confronto e riferimenti ufficiali su attività, prezzi, rinnovo e disdetta. La pagina dichiara che non si tratta di un test indipendente.
- Il pulsante affiliato usa una formulazione specifica, conserva `rel="sponsored nofollow noopener"` e la disclosure immediatamente sotto il link. Il parametro Awin `clickref` viene completato con l'ID del contenuto (per esempio `pin27`) per consentire una distinzione lato report affiliato, se supportata dal programma.
- Le versioni più recenti dei 30 articoli sono ora le sole sorgenti attive in `articoli/`, che partecipa alla build Jekyll. Le vecchie versioni e i file accessori prima presenti nella cartella sono conservati in `_archive/legacy-articles/articoli-pre-consolidamento/`, esclusa dalla build. `percorsi/` contiene le sorgenti attive dei quattro hub; le copie precedenti sono conservate in `_archive/legacy-structure/previous-hub-copies/`. I manifest puntano a `articoli/` per tutti i 30 articoli.

## Tracciamento e lancio

Il link include attributi `data-*` descrittivi, ma questi da soli **non inviano eventi analitici**. Nessun sistema GA4 è attivato da questo intervento: prima di aggiungere analytics occorre configurare consenso e informativa in base agli strumenti effettivamente usati, quindi associare il clic affiliato all'evento `affiliate_click`.

`launch_mode: false` abilita l’indicizzazione dei contenuti editoriali. Le pagine di servizio incomplete restano temporaneamente `noindex, follow` e fuori dalla sitemap. Prima del deploy definitivo verificare build GitHub Actions, URL Awin, privacy/cookie, disclosure, canonical, sitemap e link interni.


## Aggiornamento indicizzazione — 25 ottobre 2026

- Impostato `launch_mode: false` per emettere `index, follow` sui contenuti editoriali pubblici.
- Confermato che `jekyll-sitemap` genera la sitemap del progetto; non viene aggiunto un `robots.txt` sotto il percorso del progetto perché non è il file host-level usato dai crawler.
- Il template SEO rispetta `page.robots` e `page.no_canonical`; la pagina 404 resta `noindex, follow` senza canonical.
- Le pagine Privacy, Cookie, Chi siamo e Affiliazioni restano temporaneamente `noindex, follow` e fuori dalla sitemap perché contengono campi o verifiche da completare. Rimuovere tali esclusioni dopo aver inserito dati reali e validato la configurazione.
- La build Jekyll e la verifica della sitemap live devono ancora essere eseguite su GitHub Actions dopo il caricamento del pacchetto.
