# RegTime

Kilde: https://marentius.no/projects/regtime

# RegTime

Et skybasert timeregistreringssystem designet for enkel og sikker logging av arbeidstimer. Støtter flere kunder, kalendervisning, rapportgenerering og Excel-eksport.

## Systemarkitektur

#### Next.js 15 Frontend

React 19-basert frontend med Material UI 7 for et moderne og responsivt brukergrensesnitt. Hostet på Vercel.

#### Spring Boot 3.5 Backend

Java 21 backend med Spring Security for autentisering og Spring Data JPA for databasetilgang. Containerisert med Docker.

#### PostgreSQL via Supabase

Skybasert PostgreSQL-database hostet på Supabase for pålitelig og skalerbar datalagring.

#### Cloudflare Zero Trust Tunnel

Sikker tilkobling mellom Docker-containere og internett via Cloudflare Tunnel, uten behov for eksponerte porter.

## Funksjoner

### Timeregistrering

Registrer arbeidstimer på tvers av kunder og kategorier med støtte for bulk-registrering.

### Kalendervisning

Se alle registrerte timer i en oversiktlig kalendervisning for enkel navigering.

### Rapportgenerering

Generer detaljerte rapporter med mulighet for Excel-eksport via ExcelJS.

### Kunde- og kategorihåndtering

Administrer kunder og kategorier for strukturert og organisert tidslogging.

### Sikker autentisering

Spring Security med JWT-basert autentisering for trygg tilgang til systemet.

### Statistikk og oversikt

Dashboard med oversikt over registrerte timer, fordelt på kunder og perioder.

## Teknisk Stack

### Backend

### Frontend

### Infrastruktur

RegTime er bygget som en komplett fullstack-applikasjon med Java Spring Boot backend, Next.js frontend, PostgreSQL database og Docker-containerisering. Alt deployet med CI/CD via GitHub Container Registry og Cloudflare Tunnel.