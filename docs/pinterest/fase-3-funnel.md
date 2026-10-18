# Fase 3 — Funnel Pinterest → contenuto → approfondimento → Babbel

## Obiettivo
Portare traffico organico Pinterest su una pagina che mantiene la promessa del Pin, far proseguire la lettura tramite due link interni pertinenti e presentare Babbel solo come opzione da valutare quando il tema riguarda routine, speaking o preparazione pratica. Gli articoli didattici non devono diventare landing page commerciali.

## File creati e modificati
- `_data/pinterest_funnel.yml`: fonte di dati per la rubrica, con 30 Pin collegati ai permalink reali e alle relative guide.
- `_includes/pinterest-funnel-next-step.html`: modulo dinamico che appare solo sulle pagine presenti nel piano e propone due approfondimenti contestuali.
- `docs/pinterest/30-pin-publishing.csv`: file operativo per creare e pubblicare i primi 30 Pin, con URL tracciati.
- `_includes/promo-box.html` e `_includes/components/cta/cta-primary.html`: le pagine informative indirizzano alla recensione sul sito; le pagine dichiarate ad alta intenzione possono portare direttamente al link affiliato.
- `_includes/head.html`: evento GA4 `affiliate_click` sui link Awin, con percorso pagina e Pin ID quando presente nell’URL.
- `_includes/affiliate-disclosure.html`: disclosure resa più precisa e priva di un’affermazione generale su test di prodotto non dimostrata dal repository.

## Percorso raccomandato
1. **Pinterest:** il Pin promette una sola scoperta, un errore o una frase utile.
2. **Articolo di destinazione:** il primo contenuto della pagina risponde alla stessa domanda; il link UTM identifica la singola creatività.
3. **Approfondimento:** in fondo all’articolo, due collegamenti portano a guide che sviluppano un passo naturale successivo.
4. **Valutazione dello strumento:** su una selezione di articoli pertinenti compare un collegamento alla recensione Babbel. La recensione presenta pro, limiti e condizioni prima del link affiliato.
5. **Conversione:** il link Awin è riservato alle pagine ad alta intenzione e il clic viene registrato in GA4 come `affiliate_click`.

## Convenzione UTM
- `utm_source=pinterest`
- `utm_medium=organic_social`
- `utm_campaign=lo_sapevi_che`
- `utm_content=LSC001` (un codice distinto per ciascun Pin).

Non modificare il codice Pin una volta pubblicato. Se si crea una variante grafica dello stesso contenuto, usare un ID nuovo, ad esempio `LSC001B`, e aggiungere la variante al data file/CSV.

## KPI da controllare
- **Pinterest:** impression, salvataggi, clic in uscita e outbound click rate per Pin.
- **GA4:** sessioni con sorgente Pinterest, landing page, engagement e evento `affiliate_click`.
- **Affiliate network:** clic e conversioni registrati da Awin e commissioni confermate.
- **Qualità del percorso:** articoli correlati aperti, clic verso la recensione Babbel e tasso di uscita dalla landing page.

Il solo evento `affiliate_click` misura il clic in uscita, non una vendita. Per valutare le conversioni servono i report Awin e, per una lettura cross-channel, il confronto con le sessioni GA4. Il parametro evento `pin_id` viene inviato quando il clic affiliato avviene su una pagina che conserva `utm_content` nell’URL; dopo la navigazione interna, usa le dimensioni di campagna della sessione GA4 per leggere l’origine Pinterest. I parametri UTM non garantiscono da soli un’attribuzione per singolo Pin nell’interfaccia Awin.

## Regole editoriali e di tracking
- Ogni Pin deve promettere una cosa sola e la pagina di destinazione deve spiegarla davvero.
- Non usare affermazioni numeriche o benefici garantiti se la pagina non li sostiene.
- Gli articoli didattici restano utili anche a chi non acquisterà nulla.
- Le CTA non devono promettere una prova gratuita o una prima lezione gratuita se l’offerta non è verificata per il link e il mercato al momento della pubblicazione.
- Ricontrollare prezzo e condizioni Babbel prima di pubblicare o aggiornare una pagina commerciale.
- Mantenere attiva e coerente l’informativa sui link affiliati.

## Checklist prima di pubblicare ciascun Pin
- [ ] Verificare che URL e contenuto siano pubblicati e raggiungibili su GitHub Pages.
- [ ] Aprire l’URL tracciato del CSV e controllare che il sito funzioni con i parametri UTM.
- [ ] Verificare che overlay e titolo siano leggibili in formato verticale 2:3.
- [ ] Controllare che il Pin mantenga la stessa promessa del primo paragrafo dell’articolo.
- [ ] Controllare entrambi gli approfondimenti e la CTA (se presente).
- [ ] Dopo la pubblicazione, annotare data e ID del Pin nel CSV e aggiornare lo stato.
- [ ] Dopo aver accumulato dati sufficienti, confrontare Pin per clic in uscita e qualità delle sessioni, non soltanto per impression.

## Destinazioni dei 30 Pin

### LSC001 — Lo sapevi che “actually” non significa “attualmente”?
- **Destinazione:** `/inglese/errori/falsi-amici-inglese-guida/`
- **Overlay:** ACTUALLY ≠ ATTUALMENTE
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/errori/errori-comuni-italiani-inglese/` · `/inglese/da-zero/errori-traduzione-italiani/`

### LSC002 — Lo sapevi che tradurre dall’italiano può rendere l’inglese innaturale?
- **Destinazione:** `/inglese/errori/errori-comuni-italiani-inglese/`
- **Overlay:** 10 ERRORI DA EVITARE
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/errori/falsi-amici-inglese-guida/` · `/inglese/da-zero/come-pensare-in-inglese/`

### LSC003 — Lo sapevi che alcune parole inglesi non hanno una traduzione perfetta in italiano?
- **Destinazione:** `/inglese/curiosita/parole-intraducibili-inglese/`
- **Overlay:** PAROLE SENZA TRADUZIONE PERFETTA
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/curiosita/differenza-idiomi-phrasal-verbs-espressioni/` · `/inglese/curiosita/frasi-inglese-conversazione-fluente/`

### LSC004 — Lo sapevi che si può scrivere “colour” oppure “color”?
- **Destinazione:** `/inglese/curiosita/inglese-britannico-vs-americano/`
- **Overlay:** COLOUR O COLOR?
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/pronuncia/guida-pronuncia-inglese-italiani/` · `/inglese/speaking/tecnica-shadowing-inglese/`

### LSC005 — Lo sapevi che un phrasal verb non è la stessa cosa di un idiom?
- **Destinazione:** `/inglese/curiosita/differenza-idiomi-phrasal-verbs-espressioni/`
- **Overlay:** IDIOM ≠ PHRASAL VERB
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/vocabolari-pratico/25-phrasal-verbs-vita-quotidiana/` · `/inglese/curiosita/frasi-inglese-conversazione-fluente/`

### LSC006 — Lo sapevi che conoscere frasi intere può aiutarti a parlare in modo più naturale?
- **Destinazione:** `/inglese/curiosita/frasi-inglese-conversazione-fluente/`
- **Overlay:** NON SOLO PAROLE: FRASI INTERE
- **CTA Babbel di approfondimento:** sì
- **Guide correlate:** `/inglese/da-zero/come-pensare-in-inglese/` · `/inglese/speaking/small-talk-inglese/`

### LSC007 — Lo sapevi che puoi allenarti a pensare in inglese anche senza un partner?
- **Destinazione:** `/inglese/da-zero/come-pensare-in-inglese/`
- **Overlay:** ALLENA IL CERVELLO IN INGLESE
- **CTA Babbel di approfondimento:** sì
- **Guide correlate:** `/inglese/speaking/pensare-in-inglese/` · `/inglese/mindset/capisco-ma-non-parlo/`

### LSC008 — Lo sapevi che tradurre ogni parola nella testa può rallentare la conversazione?
- **Destinazione:** `/inglese/speaking/pensare-in-inglese/`
- **Overlay:** SMETTI DI TRADURRE PAROLA PER PAROLA
- **CTA Babbel di approfondimento:** sì
- **Guide correlate:** `/inglese/da-zero/come-pensare-in-inglese/` · `/inglese/mindset/capisco-ma-non-parlo/`

### LSC009 — Lo sapevi che capire l’inglese e riuscire a parlarlo sono abilità diverse?
- **Destinazione:** `/inglese/mindset/capisco-ma-non-parlo/`
- **Overlay:** CAPISCO, MA NON PARLO
- **CTA Babbel di approfondimento:** sì
- **Guide correlate:** `/inglese/mindset/ansia-parlare-inglese/` · `/inglese/speaking/tecnica-shadowing-inglese/`

### LSC010 — Lo sapevi che fare errori è una parte normale dell’apprendimento?
- **Destinazione:** `/inglese/mindset/ansia-parlare-inglese/`
- **Overlay:** PAURA DI PARLARE INGLESE?
- **CTA Babbel di approfondimento:** sì
- **Guide correlate:** `/inglese/mindset/capisco-ma-non-parlo/` · `/inglese/speaking/small-talk-inglese/`

### LSC011 — Lo sapevi che ripetere una frase mentre la ascolti si chiama shadowing?
- **Destinazione:** `/inglese/speaking/tecnica-shadowing-inglese/`
- **Overlay:** SHADOWING: ASCOLTA E RIPETI
- **CTA Babbel di approfondimento:** sì
- **Guide correlate:** `/inglese/pronuncia/guida-pronuncia-inglese-italiani/` · `/speaking/migliorare-speaking-inglese/`

### LSC012 — Lo sapevi che cinque frasi al giorno possono diventare una routine sostenibile?
- **Destinazione:** `/inglese/frasi/5-frasi-al-giorno/`
- **Overlay:** 5 FRASI AL GIORNO
- **CTA Babbel di approfondimento:** sì
- **Guide correlate:** `/inglese/metodo/routine-15-minuti/` · `/inglese/metodo/ripetizione-spaziata-lingue/`

### LSC013 — Lo sapevi che “I work” e “I’m working” non raccontano esattamente la stessa cosa?
- **Destinazione:** `/inglese/grammatica-pratica/present-simple-vs-present-continuous/`
- **Overlay:** I WORK O I’M WORKING?
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/grammatica-pratica/tempi-verbali-inglese/` · `/inglese/grammatica-pratica/past-simple-vs-past-continuous/`

### LSC014 — Lo sapevi che “I went” e “I have been” guardano al passato in modi diversi?
- **Destinazione:** `/inglese/grammatica-pratica/present-perfect-vs-past-simple/`
- **Overlay:** PAST SIMPLE O PRESENT PERFECT?
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/grammatica-pratica/tempi-verbali-inglese/` · `/inglese/grammatica-pratica/past-simple-vs-past-continuous/`

### LSC015 — Lo sapevi che “get up” e “get along” hanno significati diversi?
- **Destinazione:** `/inglese/grammatica/get-up-down-in-out/`
- **Overlay:** GET + PARTICELLA = NUOVO SIGNIFICATO
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/vocabolari-pratico/25-phrasal-verbs-vita-quotidiana/` · `/inglese/curiosita/differenza-idiomi-phrasal-verbs-espressioni/`

### LSC016 — Lo sapevi che imparare i phrasal verbs in frasi complete li rende più facili da ricordare?
- **Destinazione:** `/inglese/vocabolari-pratico/25-phrasal-verbs-vita-quotidiana/`
- **Overlay:** 25 PHRASAL VERBS QUOTIDIANI
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/grammatica/get-up-down-in-out/` · `/inglese/metodo/ripetizione-spaziata-lingue/`

### LSC017 — Lo sapevi che una presentazione in inglese può seguire una struttura semplice?
- **Destinazione:** `/inglese/beginner/presentarsi-in-inglese/`
- **Overlay:** COME PRESENTARTI IN INGLESE
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/beginner/come-salutare-inglese/` · `/inglese/beginner/paesi-nazionalita-inglese/`

### LSC018 — Lo sapevi che “How are you?” non richiede sempre una risposta lunga?
- **Destinazione:** `/inglese/beginner/come-salutare-inglese/`
- **Overlay:** SALUTARE IN INGLESE
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/beginner/presentarsi-in-inglese/` · `/inglese/speaking/small-talk-inglese/`

### LSC019 — Lo sapevi che numeri come thirteen e thirty si distinguono soprattutto dal suono finale?
- **Destinazione:** `/inglese/beginner/numeri-in-inglese/`
- **Overlay:** NUMERI IN INGLESE: ATTENZIONE AL SUONO
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/pronuncia/15-parole-difficili-pronuncia/` · `/inglese/beginner/vocabolario-base-inglese/`

### LSC020 — Lo sapevi che non devi imparare tutte le parole inglesi per cominciare a comunicare?
- **Destinazione:** `/inglese/beginner/vocabolario-base-inglese/`
- **Overlay:** PARTI DAL VOCABOLARIO ESSENZIALE
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/beginner/percorso-inglese-da-zero/` · `/metodo/come-ricordare-parole/`

### LSC021 — Lo sapevi che “Can I have…” può essere una richiesta naturale al ristorante?
- **Destinazione:** `/inglese/viaggio/inglese-al-ristorante/`
- **Overlay:** ORDINARE AL RISTORANTE IN INGLESE
- **CTA Babbel di approfondimento:** sì
- **Guide correlate:** `/inglese/viaggio/inglese-al-bar/` · `/inglese/viaggio/kit-30-frasi-inglese-viaggio/`

### LSC022 — Lo sapevi che “boarding pass” è la carta d’imbarco?
- **Destinazione:** `/inglese/viaggio/inglese-aeroporto-frasi/`
- **Overlay:** INGLESE IN AEROPORTO
- **CTA Babbel di approfondimento:** sì
- **Guide correlate:** `/inglese/viaggio/inglese-aeroporto-trasporti/` · `/inglese/viaggio/come-preparare-viaggio-7-giorni/`

### LSC023 — Lo sapevi che “Could I have a quieter room?” è utile per chiedere una stanza più silenziosa?
- **Destinazione:** `/inglese/viaggio/inglese-in-hotel/`
- **Overlay:** CHECK-IN IN HOTEL: FRASI UTILI
- **CTA Babbel di approfondimento:** sì
- **Guide correlate:** `/inglese/frasi/check-in-hotel-camera-silenziosa/` · `/inglese/viaggio/kit-30-frasi-inglese-viaggio/`

### LSC024 — Lo sapevi che “Do you have this in a different size?” è utile quando fai shopping?
- **Destinazione:** `/inglese/viaggio/inglese-shopping-estero/`
- **Overlay:** FARE SHOPPING IN INGLESE
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/viaggio/inglese-al-ristorante/` · `/inglese/viaggio/kit-30-frasi-inglese-viaggio/`

### LSC025 — Lo sapevi che preparare 30 frasi prima di partire può aiutarti a sentirti più pronto?
- **Destinazione:** `/inglese/viaggio/kit-30-frasi-inglese-viaggio/`
- **Overlay:** 30 FRASI INGLESI PER VIAGGIARE
- **CTA Babbel di approfondimento:** sì
- **Guide correlate:** `/inglese/viaggio/inglese-per-viaggiare/` · `/inglese/viaggio/come-preparare-viaggio-7-giorni/`

### LSC026 — Lo sapevi che puoi organizzare il ripasso dell’inglese in sette giorni prima di un viaggio?
- **Destinazione:** `/inglese/viaggio/come-preparare-viaggio-7-giorni/`
- **Overlay:** 7 GIORNI PRIMA DI PARTIRE
- **CTA Babbel di approfondimento:** sì
- **Guide correlate:** `/inglese/viaggio/kit-30-frasi-inglese-viaggio/` · `/inglese/viaggio/inglese-aeroporto-trasporti/`

### LSC027 — Lo sapevi che una buona email in inglese può essere chiara senza sembrare fredda?
- **Destinazione:** `/inglese/business/email-formali-inglese/`
- **Overlay:** EMAIL FORMALI IN INGLESE
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/business/video-call-frasi-utili/` · `/inglese/business/colloquio-di-lavoro-domande/`

### LSC028 — Lo sapevi che “Could I jump in?” può aiutarti a intervenire in una riunione?
- **Destinazione:** `/inglese/business/video-call-frasi-utili/`
- **Overlay:** RIUNIONI IN INGLESE
- **CTA Babbel di approfondimento:** no
- **Guide correlate:** `/inglese/business/email-formali-inglese/` · `/inglese/business/colloquio-lavoro-inglese/`

### LSC029 — Lo sapevi che preparare esempi concreti rende più semplice rispondere in inglese a un colloquio?
- **Destinazione:** `/inglese/business/colloquio-di-lavoro-domande/`
- **Overlay:** COLLOQUIO DI LAVORO IN INGLESE
- **CTA Babbel di approfondimento:** sì
- **Guide correlate:** `/inglese/business/colloquio-lavoro-inglese/` · `/inglese/business/video-call-frasi-utili/`

### LSC030 — Lo sapevi che una routine breve è più facile da mantenere se decidi prima cosa fare?
- **Destinazione:** `/inglese/metodo/routine-15-minuti/`
- **Overlay:** 15 MINUTI DI INGLESE AL GIORNO
- **CTA Babbel di approfondimento:** sì
- **Guide correlate:** `/inglese/metodo/routine/` · `/inglese/metodo/ripetizione-spaziata-lingue/`
