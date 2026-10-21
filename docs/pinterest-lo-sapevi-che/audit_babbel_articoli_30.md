# Audit Babbel — 30 articoli FluenteMente

## Intervento

- Ogni articolo del cluster contiene ora un riferimento contestuale a Babbel o una call to action coerente con il suo contenuto.
- Nei 27 articoli didattici che non citavano già il brand è stato inserito il componente condiviso `babbel-next-step.html`, con testo specifico per il tema della lezione e collegamento alla guida `/babbel-per-imparare-inglese/`.
- `pin01` mantiene la citazione già presente nella sezione sul percorso guidato; `pin30` mantiene la sezione di confronto su Babbel e il link alla guida dedicata.
- `pin27` ha una call to action affiliata configurata con l'URL Awin fornito dall'utente. Il pulsante usa l'URL esatto e mostra la disclosure nello stesso blocco.
- La CTA degli articoli didattici è un collegamento interno, non un'affermazione che il link sia affiliato. Il link commerciale resta centralizzato nella guida dedicata.

## File tecnici aggiunti/modificati

- `_includes/babbel-next-step.html`: CTA contestuale per gli articoli didattici.
- `_includes/babbel-offer.html`: CTA del brand con fallback al sito ufficiale e disclosure condizionata.
- `_config.yml`: `babbel_affiliate_url` impostato con il link Awin fornito dall'utente; `babbel_official_url` resta impostato su `https://it.babbel.com/` come fallback.
- `assets/css/main.css`: stili responsive dei due componenti.
- `articoli/*.md`: aggiunta di riferimenti contestuali; `pin27` aggiornata per rimuovere i TODO visibili al lettore.

## Stato del link affiliato

L'URL Awin ricevuto è stato inserito in `babbel_affiliate_url` e viene richiamato dalla CTA di `babbel-offer.html`. Il collegamento mantiene `rel="sponsored"` (insieme agli attributi tecnici `nofollow noopener`) e la disclosure compare direttamente sotto la CTA. Prima della pubblicazione, verificare il redirect e il tracciamento sul sito live.

## Revisione editoriale

I riferimenti sono intenzionalmente prudenti: Babbel è presentato come una possibile risorsa complementare, non come unico metodo né come garanzia di progresso. Prezzi, sconti, prova, funzioni specifiche e risultati non vengono promessi senza una verifica dedicata.
