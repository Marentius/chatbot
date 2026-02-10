# Vetle Marentius Nilsen

## Om meg

Vetle Marentius Nilsen er en engasjert fullstack-utvikler med 2 års erfaring, ansatt hos Visma SmartSkill AS siden 2023. Han jobber med å bygge moderne webapplikasjoner og har erfaring med alt fra frontend til backend. Han brenner for clean code, god arkitektur og kontinuerlig læring. Han har over 1000+ commits på GitHub.

## Kontaktinformasjon

- E-post: vetlenilseen@hotmail.com
- Porteføljeside: https://marentius.no
- GitHub: https://github.com/Marentius
- LinkedIn: https://www.linkedin.com/in/vetle-marentius-nilsen-07b962174/

## Ferdigheter og teknologier

### Frontend
- React
- Next.js
- TypeScript
- Tailwind CSS
- React Native (Expo)
- Material UI
- HTML/CSS/SCSS

### Backend
- Java Spring Boot
- Node.js
- Python (FastAPI)
- C# / .NET 9
- REST APIs
- WebSocket / STOMP
- Entity Framework Core

### DevOps & Cloud
- Docker & Docker Compose
- Microsoft Azure (Event Hubs, Container Apps, Static Web Apps, AI Search, Azure OpenAI, Azure SQL)
- Google Cloud
- Supabase (PostgreSQL, Auth, Storage)
- CI/CD (Bitbucket Pipelines, GitHub Actions)
- Git
- Cloudflare Zero Trust Tunnel
- Vercel
- Raspberry Pi (selvhostet backend)

### Andre ferdigheter
- RAG (Retrieval-Augmented Generation) med AI
- OCR (Tesseract, ocrmypdf)
- UI/UX og Branding
- Responsivt design
- Tauri (desktop-apper)
- Leaflet / GeoJSON (kartvisualisering)

## Arbeidserfaring

### Visma SmartSkill AS — Fullstack Developer (2023 – nå)

Vetle jobber som fullstack-utvikler i Visma SmartSkill AS. Han jobber med React og Google Cloud, og har bidratt på flere interne produkter:

#### Veilederen Innbygger (AB120-Citizen)
En multi-tenant AI-chatbot-plattform for norske kommuner. Gir RAG-basert spørsmål og svar med støtte for tekst og tale (ElevenLabs). Bygget med .NET 9 backend og TypeScript/Vite frontend. Bruker Azure OpenAI (GPT-4o), Azure AI Search, Azure SQL og Azure Container Apps. Inkluderer multi-tenant arkitektur med API-nøkler, Visma Connect OAuth, og automatisk bruksregistrering.

#### Branding Control Center (AB121)
Et Next.js-verktøy som lar redaktører oppdatere branding-innhold i et GitHub-repository uten å måtte jobbe direkte i Git. Støtter opplasting av hero-bilder for flere brands (Glup, SmartSkill, Veilederen, Nexus SmartSkill), med automatisk WebP-konvertering, karusellhåndtering, og forhåndsvisning. Oppretter automatisk branch og PR per endring. Bruker GitHub OAuth.

#### Documentation Portal (AB122)
En dokumentasjonsportal for interne produkter.

#### Visma Login Branding
Transformerte standard Visma-innloggingssider til skreddersydde, merkevarebyggede opplevelser for fire kunder: Veilederen.no, SmartSkill, Glup.no og Nexus SmartSkill. Inkluderte custom fargepalett og gradient, logo-integrasjon, tilpasset bakgrunnsgraflikk og responsivt design. Teknologi: CSS, SCSS, Visma SDK.

## Utdanning

### Bacheloroppgave (2025)
Vetle fullførte sin bacheloroppgave i 2025 med prosjektet "Europris Real-Time Sales Visualization" — en webapplikasjon som visualiserer salgstransaksjoner i sanntid på et interaktivt Norgeskart for Europris AS.

## Prosjekter

### Europris Real-Time Sales Visualization — Bacheloroppgave (2025)

En webapplikasjon som visualiserer sanntids salgsdata fra 100+ butikker på et interaktivt Norgeskart, utviklet for Europris AS som bacheloroppgave.

**Nøkkeltall:**
- 1,94 ms gjennomsnittlig latens (målt 1–4 ms via WebSocket)
- 24/7 sanntidsdrift
- Animerte visualiseringer med 3-sekunders bloom-sykluser

**Visualiseringssystem:**
Salg vises som animerte SVG-blomster fargekodet etter transaksjonsverdi:
- Blå blomster (30px): 0–299 kr
- Oransje blomster (60px): 300–999 kr
- Grønne blomster (120px): 1000+ kr

**Kjernefunksjoner:**
- Animerte blomstermarkører som bloomer på kartet for å unngå visuell rot
- Interaktivt Norgeskart med GeoJSON-baserte fylkes- og landegrenser
- Klikkbare butikkmarkører med popup-informasjon
- Under 2 ms dataflyt-latens fra backend til frontend

**Teknologi:**
- Frontend: React, Next.js, Leaflet, React-Leaflet, GeoJSON
- Backend: Java Spring Boot, WebSocket, STOMP, Maven
- Sky-infrastruktur: Azure Event Hubs, Azure Container Apps, Azure Static Web Apps, CI/CD via Bitbucket Pipelines

**Omfang:**
Vetle utviklet hele den tekniske løsningen alene — arkitektur, backend-integrasjon og frontend-implementasjon — mens teamet på fire bidro med forskning, dokumentasjon og testing.

**Brukertesting:**
Testing ved Europris' hovedkontor viste at alle visuelle elementer forble tydelige på store skjermer. Brukertestdeltakere beskrev løsningen som "enkel og oversiktlig", og fullførte alle oppgaver uten tekniske problemer.

### VIDD — Turapp (personlig prosjekt)

En React Native/Expo mobilapp for sporing og deling av turer i naturen. Brukere kan GPS-spore aktiviteter, laste opp geotaggede bilder, oppdage steder, følge andre brukere, og tjene poeng gjennom et gamification-system.

**Teknologi:** React Native 0.81, Expo SDK 54, TypeScript, Supabase (PostgreSQL + Auth + Storage)

**Funksjoner:**
- GPS-sporing med expo-location
- Interaktivt kart med Google Maps
- Bildeopplasting med komprimering
- Følg andre brukere og se deres turer
- Gamification med poengsystem (+10 for verifisert sted, +5 for geotagget bilde, +2 for offentlig deling)
- Leaderboard og brukerstatistikk
- Community-verifisering av steder
- 20 aktivitetskategorier (gåtur, topptur, badeplass, sykkeltur osv.)
- OAuth-innlogging (Google, Apple)

### Receiptly — Digital kvitteringshåndtering (personlig prosjekt)

En mobilvennlig webapp for å ta bilde av kvitteringer, gjøre OCR og organisere utgifter.

**Funksjoner:**
- Bildeopplasting fra kamera eller filsystem
- Automatisk OCR med Tesseract for uttrekk av butikk, beløp og dato
- Tagging og søk i kvitteringer
- Statistikk over utgifter per måned og kategori

**Teknologi:** FastAPI (Python), SQLAlchemy, Tesseract OCR, Next.js 15, Tailwind CSS

### RegTime — Timeregistrering (personlig prosjekt)

Et komplett, skybasert system for enkel og sikker timeregistrering.

**Funksjoner:**
- Brukerautentisering med brukernavn og passord
- Kunde- og kategorihåndtering
- Tidsregistrering med bulk-registrering (flere oppføringer samtidig)
- Kalendervisning med fargekoding
- Sammendrag og rapporter med Excel-eksport
- Responsivt design for desktop og mobil

**Teknologi:** Spring Boot 3.5 (Java 21), Next.js 15, React 19, Material UI 7, PostgreSQL (Supabase), Docker

**Deployment:** Backend kjører som Docker-container på en Raspberry Pi, eksponert via Cloudflare Zero Trust Tunnel på RTapi.marentius.com. Frontend deployet på Vercel på regtime.marentius.com.

### FileConverter — Universelt filkonverteringsverktøy (personlig prosjekt)

Et universelt filkonverteringsverktøy med CLI og GUI, publisert som open source på GitHub.

**Funksjoner:**
- Bildekonvertering: PNG, JPG, WebP, TIFF, BMP, GIF, HEIC med resize og kvalitetskontroll
- Dokumentkonvertering: DOCX, PPTX, XLSX til/fra PDF via LibreOffice og Pandoc
- PDF-operasjoner: komprimering, sammenslåing, splitting med Ghostscript/qpdf
- OCR: PDF til søkbar PDF, bilde til tekst med Tesseract
- Preset-system for web, print, thumbnail, sosiale medier
- Batch-prosessering med parallell konvertering
- Moderne desktop-app bygget med Tauri + React

**Teknologi:** TypeScript monorepo, Tauri, React, Sharp, 95% testdekning, CI/CD med GitHub Actions

GitHub: https://github.com/Marentius/FileConverter

### Portefølje-chatbot (dette prosjektet)

En RAG-basert chatbot for porteføljesiden marentius.no. Besøkende kan stille spørsmål om Vetle — erfaring, prosjekter, ferdigheter og kontaktinfo.

**Teknologi:** FastAPI, ChromaDB, sentence-transformers, Groq (Llama 3.3 70B), React, Docker Compose

## Porteføljesiden

Porteføljesiden marentius.no er bygget med Next.js og React, med animerte komponenter fra React Bits-biblioteket. Inkluderer Aurora-bakgrunner, gradient-tekst, typing-animasjoner, spotlight-kort, pixel-transisjoner og tilted cards. Siden er responsiv og optimalisert for både desktop og mobil.
