# Audit collegamenti interni — FluenteMente

**Aggiornato:** 21 ottobre 2026  
**Ambito:** home page, 30 articoli della rubrica Pinterest “Lo sapevi che…?”, quattro nuovi hub tematici, menu principale.  
**Fonte:** repository ZIP fornito nel progetto; non è stata eseguita una verifica del sito pubblicato online.

## Risultato

- Articoli inclusi: **30** (30 ID Pin univoci).
- Home page inclusa: **1**.
- Hub nuovi creati: **4** — C2, C3, C4 e C5.
- Pagine di contenuto nella mappa: **35**.
- Destinazioni interne non risolte nel corpo della home, degli articoli e degli hub: **0**.
- Articoli senza collegamento al proprio hub o guida centrale: **0**.

## Quattro hub creati

| Cluster | URL | Articoli raccolti |
|---|---|---:|
| C2 — Inglese pratico per conversare | `/inglese-pratico-per-parlare/` | 5 |
| C3 — Espressioni naturali e inglese parlato | `/espressioni-inglesi-naturali/` | 5 |
| C4 — Parole inglesi che si confondono facilmente | `/parole-inglesi-confuse/` | 6 |
| C5 — Errori comuni e differenze grammaticali | `/errori-comuni-inglese/` | 6 |

I cluster C1 e C6 continuano ad avere una guida centrale già compresa nei 30 articoli: pin23 e pin30. Le guide centrali collegano i relativi articoli di supporto.

## Collegamenti aggiunti

- Ogni articolo di supporto collega alla rispettiva guida di cluster o al contenuto centrale.
- Ogni hub elenca tutti gli articoli assegnati al proprio cluster e rimanda a percorsi complementari.
- La home page mostra i sei percorsi editoriali, mantenendo anche gli elenchi degli articoli.
- Il menu principale è stato aggiornato per puntare a pagine presenti nel pacchetto, evitando le precedenti destinazioni generiche non incluse.
- La mappa CSV allegata riporta link in entrata, link in uscita e destinazioni non risolte per pagina.

## Controlli da completare prima della pubblicazione

1. **Footer e pagine legali:** il footer della base grafica contiene link a `/chi-siamo/, /privacy/, /cookie/, /disclaimer/`. Queste pagine non sono incluse in questo intervento e devono essere create/revisionate in base alle effettive informazioni del sito, prima di pubblicare.
2. **Build Jekyll:** non è stata eseguita una compilazione con Jekyll; la verifica effettuata è statica su front matter e destinazioni Liquid `relative_url`.
3. **Sito online:** i permalink sono configurati nei file ma non è stato controllato che siano già pubblicati e raggiungibili sul sito remoto.
4. **Affiliazione Babbel:** la pagina pin27 conserva un promemoria esplicito per verificare le informazioni correnti e inserire il link affiliato e la disclosure prima della pubblicazione.

## Dettaglio anomalie

Nessuna destinazione `relative_url` non risolta nei contenuti inclusi (home, 30 articoli e quattro hub).
Tutti i 30 articoli sono collegati alla guida centrale o al rispettivo hub; le pagine centrali elencano gli articoli del proprio cluster.
