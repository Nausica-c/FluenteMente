# Audit Babbel — 30 articoli FluenteMente

## Intervento aggiornato — 25 ottobre 2026

La promozione di Babbel è stata resa selettiva: il brand non viene inserito automaticamente come blocco promozionale al termine di ogni mini-lezione.

- Le CTA soft del componente `_includes/babbel-next-step.html` sono mantenute in PIN20 (routine 5+5+5), PIN21 (ripasso del vocabolario) e PIN23 (studio quotidiano), dove l'intento editoriale è strettamente collegato all'organizzazione della pratica.
- PIN01 mantiene soltanto il collegamento contestuale già presente nel testo, evitando di ripetere la stessa destinazione con un secondo box. PIN30 mantiene il collegamento interno verso la guida Babbel perché l'articolo tratta direttamente la scelta di un corso.
- Le CTA soft sono state rimosse dalle mini-lezioni di singole espressioni, falsi amici, grammatica e situazioni quotidiane, per dare priorità agli approfondimenti didattici correlati. PIN27 resta la pagina principale con CTA affiliata diretta.
- La guida PIN27 è stata ampliata con criteri di valutazione, limiti da considerare, una griglia di confronto e collegamenti alle informazioni ufficiali su attività, prezzi, rinnovo e disdetta. La pagina chiarisce che non si tratta di un test indipendente.

## Componenti e tracciamento

- `_includes/babbel-next-step.html`: collegamento interno a bassa pressione verso la guida di valutazione Babbel.
- `_includes/babbel-offer.html`: CTA affiliata con copy specifico, fallback al sito ufficiale e disclosure immediatamente sotto il link.
- `_config.yml`: mantiene l'URL Awin fornito dall'utente e la pagina ufficiale come fallback. Il valore `clickref` viene completato con il `pin_id` della pagina (PIN27 usa `pin27`) per distinguere la provenienza nei report Awin, se supportato dalla configurazione del programma.
- Gli attributi `data-*` sulla CTA sono metadati per un futuro collegamento analitico e non inviano eventi da soli. GA4 non è stato attivato perché prima vanno configurati consenso e informativa per gli strumenti effettivamente utilizzati.

## Pre-pubblicazione

Le versioni più recenti dei 30 articoli sono ora le sole sorgenti attive in `articoli/`. Le copie che prima si trovavano in quella cartella sono conservate in `_archive/legacy-articles/articoli-pre-consolidamento/`, esclusa dalla build. La directory `percorsi/` mantiene copie precedenti degli hub ed è esclusa; le sorgenti attive degli hub sono nella radice. Al momento dell’audit era previsto il completamento della build GitHub Actions e dei controlli Awin, privacy, cookie, disclosure e destinazioni. La configurazione di indicizzazione è stata aggiornata successivamente; vedere la sezione “Aggiornamento stato indicizzazione”.


## Aggiornamento stato indicizzazione — 25 ottobre 2026

La nota relativa a `launch_mode: true` descrive lo stato rilevato nell'audit originale. La configurazione corrente è stata successivamente aggiornata a `launch_mode: false`: i contenuti editoriali possono essere indicizzati. Le pagine Privacy, Cookie, Chi siamo e Affiliazioni rimangono temporaneamente `noindex, follow` ed escluse dalla sitemap finché i campi e i controlli non sono completati. La build e la verifica live devono ancora essere eseguite dopo il deploy.


## Consolidamento delle sorgenti PIN — 25 ottobre 2026

Le 30 versioni più recenti sono state spostate dalla radice in `articoli/`; i permalink sono invariati. Le precedenti versioni e i file accessori trovati nella vecchia cartella sono preservati in `_archive/legacy-articles/articoli-pre-consolidamento/`.
