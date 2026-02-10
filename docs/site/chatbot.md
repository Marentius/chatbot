# Portfolio Chatbot

Kilde: https://marentius.no/projects/chatbot

# Portfolio Chatbot

En RAG-basert chatbot som lar besøkende stille spørsmål om min erfaring, prosjekter, ferdigheter og kontaktinformasjon. Chatboten henter relevant informasjon og genererer kontekstuelle svar.

## Dataflyt

## Nøkkelfunksjoner

### RAG-arkitektur

Retrieval-Augmented Generation som henter relevant kontekst fra portfolio-data for presise svar.

### Vektorsøk med ChromaDB

Portfolio-innhold embeddes og lagres i ChromaDB for semantisk søk og kontekstuell gjenfinning.

### Llama 3.3 70B via Groq

Bruker Groq API med Llama 3.3 70B for rask og intelligent generering av naturlig språk.

### Anti-jailbreak & guardrails

Kun spørsmål om portfolio aksepteres. Innebygd språkdeteksjon for norsk og engelsk.

## Teknisk Stack

### Backend

### AI & Vektordatabase

### Frontend & Deploy

Chatboten er designet med strenge guardrails - den svarer kun på spørsmål relatert til portfolioen. Innebygd anti-jailbreak beskyttelse og automatisk språkdeteksjon sikrer at samtaler forblir relevante og trygge.