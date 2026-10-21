# Audit pagine di servizio — FluenteMente

Data revisione: 21 ottobre 2026.

## Pagine generate

| File | URL previsto | Stato contenuto |
|---|---|---|
| `chi-siamo.md` | `/chi-siamo/` | Bozza editoriale completa; nome del responsabile e email da inserire. |
| `privacy.md` | `/privacy/` | Informativa orientativa basata sul repository e sulla documentazione pubblica dell'hosting; titolare, recapiti, tempi di conservazione e trasferimenti da verificare. |
| `cookie.md` | `/cookie/` | Bozza basata su ispezione statica; l'inventario reale va ottenuto testando il sito online. |
| `disclaimer.md` | `/disclaimer/` | Pagina Affiliazioni collegata ai path del footer e dell'include; da aggiornare quando saranno attivi i link affiliati. |

## Risultati dal repository statico

- La configurazione indica GitHub Pages/Jekyll e `launch_mode: true`.
- Non sono stati trovati nel codice esaminato script espliciti per analytics, retargeting o pixel pubblicitari, né form di contatto/newsletter o contenuti social incorporati.
- Il footer contiene già i collegamenti a `/chi-siamo/`, `/privacy/`, `/cookie/` e `/disclaimer/`.
- Il componente di disclosure viene ora mostrato solo se richiesto tramite `show_affiliate_disclosure: true`, invece di apparire indiscriminatamente sulle pagine ordinarie.
- Il link del layout legacy `curiosita.html` è stato indirizzato all’articolo esistente `/come-studiare-inglese-ogni-giorno/`, evitando una destinazione senza pagina nel pacchetto.
- Il repository esaminato non contiene un URL affiliato definitivo da attivare.

## Limitazioni

Non sono stati verificati cookie sulla versione live, non sono stati testati i servizi esterni mediante browser e non è stato eseguito un build Jekyll. La sola ispezione dei file non conferma l'effettivo comportamento del dominio pubblicato. I campi evidenziati devono essere completati prima della messa online.
