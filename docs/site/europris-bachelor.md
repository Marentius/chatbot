# Sanntids Salgsvisualisering

Kilde: https://marentius.no/projects/europris-bachelor

# Sanntids Salgsvisualisering

En webapplikasjon som visualiserer salgsdata i sanntid på et interaktivt Norgeskart, utviklet for å gi Europris innsikt i salgsaktivitet gjennom en engasjerende og visuelt tydelig presentasjon.

Gj.snitt latens

Butikker

Animasjon

Sanntid

Leaflet-kart med OpenStreetMap og GeoJSON-baserte fylkesgrenser

## Blomstervisualisering

Salgsdata visualiseres som animerte SVG-blomster i ulike farger og størrelser basert på handlekurvens verdi.

### Lite salg

0 - 299 kr

Blå blomst, 30px

### Mellomstort salg

300 - 999 kr

Oransje blomst, 60px

### Stort salg

1000+ kr

Grønn blomst, 120px

## Nøkkelfunksjoner

### Animerte blomstermarkører

Hvert salg visualiseres som en SVG-blomst som "blomstrer" på kartet i 3 sekunder for å forhindre visuell overbelastning

### Verdikategorisering

Blomstens størrelse og farge indikerer handlekurvens verdi: blå/30px (0-299kr), oransje/60px (300-999kr), grønn/120px (1000kr+)

### ~2ms gjennomsnittlig latens

Målt dataflyt på 1-4ms fra backend til frontend, med gjennomsnitt på 1.94ms via WebSocket

### Interaktivt Norgeskart

Leaflet-kart med GeoJSON-baserte fylkes- og landegrenser, klikkbare butikkmarkører med popup-informasjon

## Systemarkitektur

#### Azure Event Hubs

Salgsdata fra Europris sine kassasystemer strømmes til Azure Event Hubs - en skalerbar event-streaming plattform som håndterer millioner av events.

#### Java Spring Boot Backend

Containerisert backend kjøres i Azure Container Apps. Konsumerer events fra Event Hubs, prosesserer salgsdata til JSON og sender videre via WebSocket-server.

#### WebSocket Sanntidskommunikasjon

Data pushes umiddelbart til alle tilkoblede klienter via WebSocket. Ingen polling - kontinuerlig toveis kommunikasjon med målt latens på 1-4ms.

#### React/Next.js Frontend

Hostes på Azure Static Web Apps. Leaflet-kart med OpenStreetMap-tiles og GeoJSON-baserte norges- og fylkesgrenser. Animerte blomstermarkører visualiserer hvert salg.

#### CI/CD Pipeline

Automatisk bygging og distribusjon via Bitbucket Pipelines til Azure-miljøet ved hver commit.

## Teknisk Stack

### Frontend

### Backend

### Cloud & Infrastruktur

## Testing & Resultater

### Test på storskjerm

Applikasjonen ble testet på Europris sin storskjerm på hovedkontoret. Alle visuelle elementer forble tydelige, og funksjonalitetene fungerte som tiltenkt uten skaleringsproblemer.

### Brukertest

Løsningen ble beskrevet som "enkel og oversiktlig" av testpersonene. Alle oppgaver ble gjennomført uten problemer, og det ble ikke avdekket noen tekniske feil.

Jeg utviklet hele den tekniske løsningen alene - fra backend-arkitektur med Java Spring Boot og Azure Event Hubs-integrasjon, til frontend med React/Next.js, Leaflet kartvisualisering og WebSocket sanntidskommunikasjon.

Prosjektet ble gjennomført som bacheloroppgave i et team på fire, der jeg hadde ansvaret for all koding mens teamet bidro med research, dokumentasjon og testing.

— Testperson fra Europris