# Portfolio Chatbot

RAG-basert chatbot for porteføljesiden marentius.no. Besøkende kan stille spørsmål om Vetle Marentius Nilsen — erfaring, prosjekter, ferdigheter og kontaktinfo.

**Tech stack:** FastAPI, ChromaDB, sentence-transformers, Groq (Llama 3.3 70B), React, Docker Compose

## Forutsetninger

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Python 3.10+](https://www.python.org/) (for scraping)
- En gratis API-nøkkel fra [Groq](https://console.groq.com)

## Oppsett

### 1. Konfigurer miljøvariabler

```bash
cp .env.example .env
```

Åpne `.env` og legg inn Groq API-nøkkelen din:

```
GROQ_API_KEY=gsk_din_nøkkel_her
```

### 2. Scrape porteføljesiden

Installer avhengigheter og kjør scraperen:

```bash
cd backend
pip install beautifulsoup4 requests
python -m scripts.scrape_website
```

Sidene lagres som `.md`-filer i `docs/site/`.

### 3. Start med Docker Compose

```bash
cd ..
docker compose up -d --build
```

Dette starter tre containere:

| Tjeneste | Port | Beskrivelse |
|----------|------|-------------|
| chromadb | 8000 | Vektor-database |
| backend | 8080 | FastAPI API-server |
| frontend | 3000 | React chat-grensesnitt |

### 4. Last dokumentasjon inn i ChromaDB

Vent til alle containere kjører (`docker compose ps` viser `healthy` på chromadb), deretter:

```bash
docker compose exec backend python -m scripts.ingest_docs
```

### 5. Test

Åpne [http://localhost:3000](http://localhost:3000) for å chatte direkte.

## Embed på en annen nettside

### Vanlig HTML

Legg til før `</body>`:

```html
<script>window.CHAT_URL = "http://localhost:3000";</script>
<script src="http://localhost:3000/embed.js"></script>
```

### Next.js

I `layout.tsx`:

```tsx
import Script from "next/script";

// Rett før </body>:
<Script id="chat-config" strategy="lazyOnload">
  {`window.CHAT_URL = "http://localhost:3000";`}
</Script>
<Script src="http://localhost:3000/embed.js" strategy="lazyOnload" />
```

### Produksjon

Bytt ut `http://localhost:3000` med den faktiske URL-en der chatboten er hostet.

## Oppdatere dokumentasjon

Når porteføljesiden oppdateres:

```bash
cd backend
python -m scripts.scrape_website
cd ..
docker compose exec backend python -m scripts.ingest_docs
```

ChromaDB bruker persistent storage (Docker volume), så data overlever restart. Bruk `docker compose down -v` kun hvis du vil slette alt og starte på nytt.

## Kjøre tester

```bash
docker compose exec backend pytest tests/ -v
```

## Arkitektur

```
Bruker → Chat-widget → FastAPI backend → [Embed spørsmål → ChromaDB søk → Relevanssjekk → Groq/Llama] → Streamet svar
```

- **Embedding:** all-MiniLM-L6-v2 (sentence-transformers)
- **Retrieval:** ChromaDB med cosine distance-terskel (0.35)
- **LLM:** Groq API (Llama 3.3 70B) — gratis tier
- **Guardrails:** Kun spørsmål om Vetle, anti-jailbreak, språkdeteksjon (norsk/engelsk)
