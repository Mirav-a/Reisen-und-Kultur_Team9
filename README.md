# Reisen-und-Kultur_Team9
# Travel Assistant – Smart Packing & Green Routes (mit LocalLens-AI)

## 1. Executive Summary
Der Travel Assistant ist eine schlanke, containerisierte API-Lösung für Reiseplanung ohne grafische Oberfläche. Sie umfasst drei Kernfunktionen: (1) Smart Packing Assistant erzeugt personalisierte Packlisten auf Basis von Reisedauer, Ziel und Aktivitäten unter Nutzung eines deterministischen Dummy-Wetters. (2) Green Routes plant emissionsärmere Routen mit geschätzter CO₂-Einsparung gegenüber Autofahrten (Dummy-Routen). (3) LocalLens liefert knappe Insider-Snippets zu Städten (optional via AI-API; ohne Key sicherer Fallback „weiß ich nicht“). Die Architektur nutzt zwei Microservices (travel-api, ai-service) auf FastAPI, ist via Docker/Compose lokal startbar und via Kubernetes (kind) deploybar. Ziel ist eine robuste, prüfbare Basis mit klaren Endpunkten und geringer Halluzinationsrate.

## 2. Ziele des Projekts
Das Projekt adressiert vier häufige Reiseprobleme: unsichere Packentscheidungen, unklare Nachhaltigkeitsvorteile von Alternativrouten, begrenzte lokale Insights und Budgetaufteilung. Ziel ist eine zuverlässige, reproduzierbare API mit realistischen, aber erklärten Dummy-Daten. Die Lösung priorisiert Verlässlichkeit („weiß ich nicht“ statt erfinden), klare Schnittstellen und containerisierte Ausführung. Sie demonstriert, wie KI defensiv eingebettet wird, ohne kritische Pfade zu blockieren. Dadurch entsteht ein didaktisch wertvolles, auditierbares System für Lehre, Prototypen und spätere Skalierung.

## 3. Anwendung und Nutzung
Hauptnutzer:innen sind Studierende, Entwickler:innen und Reisende, die programmatisch Packlisten, grüne Routen und lokale Snippets abrufen wollen. Nutzung per HTTP-POST an die Endpunkte der travel-api; optional liefert ai-service AI-gestützte LocalLens-Inhalte. Beispiel: POST /v1/packlist mit {destination, days, activities}. Die API eignet sich für Backends, Bots oder Integrationen. Code-Repository: <REPO_LINK_EINFÜGEN>. Pitch (Audio bevorzugt): <PITCH_LINK_EINFÜGEN>. Für AI-Funktionen einen OPENAI_API_KEY als Secret setzen; ohne Key greift ein sicherer Fallback.

## 4. Entwicklungsstand
Der aktuelle Stand ist ein funktionsfähiger **Prototyp** mit produktionsnaher Struktur: zwei getrennte Services, definierte Models/Schemas, defensive AI-Integration, Dockerfiles, docker-compose und Kubernetes-Manifeste (kind). Die Endpunkte sind stabil und deterministisch; Validierung erfolgt via Pydantic. Observability kann durch Logs und Health-Checks erweitert werden. Ein Wechsel zu realen Wetter-/Routing-APIs ist vorgesehen, aber hier explizit durch Dummy-Logiken ersetzt, um die Prüfungsanforderung (lokal, offline-fähig) zu erfüllen.

## 5. Projektdetails
Kernfunktionen: (a) Packlisten-Generierung aus Ziel, Dauer, Aktivitäten, Reiseprofil; wetterbasiert (warm/mild/cool) mit nachvollziehbaren Begründungen je Item. (b) Green Routes: einfache Distanzschätzung, Zeit und CO₂-Vergleich zu „car“ mit klarer Erläuterung als Dummy. (c) Budget Planner: skaliert Tagesbudgets je Profil (thrifty/balanced/comfort) auf ein Gesamtbudget und gibt rationale Hinweise. (d) LocalLens: bis zu 3 kurze Insider-Snippets per AI-Service; bei Unsicherheit bewusstes „weiß ich nicht“. Alle Endpunkte sind idempotent, validiert und dokumentierbar (OpenAPI durch FastAPI).

## 6. Innovation
Die Innovation liegt in der **defensiven KI-Orchestrierung**: KI ist optional, transparent gekapselt und darf nie unsichere Antworten erzwingen. Das System priorisiert Reproduzierbarkeit (deterministische Dummys), klare Erklärungen (Reason-Felder) und modulare Erweiterbarkeit. Green-Scoring, Budget-Skalierung und Profil-Heuristiken sind einfach, aber bewusst nachvollziehbar gehalten. So entsteht ein didaktisch starker Bauplan, der sich schnell mit echten Datenquellen oder Modellen austauschen lässt.

## 7. Wirkung (Impact)
Kurzfristig: beschleunigte Reisevorbereitung, geringere Pack-Fehler, Sichtbarmachung des CO₂-Vorteils alternativer Verkehrsmittel, Budgetklarheit. Mittelfristig: bessere Nachhaltigkeitsentscheidungen, leichtere Integration in Uni-Projekte, Chatbots oder Sprachassistenten. Langfristig: Grundlage für datengetriebene Städte-/Mobilitätsberatung, inkl. Barrierefreiheits- und Halal/Diät-Filter. Der Impact entsteht durch niedrigschwellige APIs, die in Lern- und Produktkontexte passen.

## 8. Technische Exzellenz
Tech: Python 3.11, FastAPI, Pydantic v2, httpx (Service-to-Service), Uvicorn. Containerisierung: Docker, docker-compose. Orchestrierung: Kubernetes (kind), je ein Deployment + Service pro Microservice, Namespace/Secrets für AI-Key. Daten/Algorithmen: deterministische Wetter-/Distanz-Heuristiken, einfache CO₂-Faktoren (Dummy), Budget-Skalierung per Profil-Gewichten. KI via OpenAI-Chat-API (konservativ: Temp 0.3, kurze Snippets); Fallback ohne Key. Health-Checks verfügbar, klare Umgebungsvariablen.

## 9. Ethik, Transparenz und Inklusion
Transparenz: Dummy-Daten sind explizit gekennzeichnet; CO₂- und Routenwerte sind Schätzungen. Sicherheit: KI antwortet defensiv („weiß ich nicht“ bei Unsicherheit oder fehlendem Key). Fairness/Inklusion: Sprache konfigurierbar; Inhalte kurz und barrierearm; keine diskriminierenden Heuristiken. Datenschutz: keine personenbezogenen Daten; keine Persistenz. Erweiterbar um Bedürfnisse (z. B. Halal, Laktosefrei, Barrierefreiheit) über optionale Profile/Filter.

## 10. Zukunftsvision
In 5–10 Jahren ist der Assistant ein Echtzeit-Ökosystem: echte Wetter- und Fahrplandaten, CO₂-Modelle auf Streckenniveau, personalisierte Nachhaltigkeitsziele, multimodale Empfehlungen (Text/Sprache/Bild), inklusive Orts-AR-Overlays. KI läuft lokal-hybrid (Edge + Cloud) mit Privacy-Wahrung. Offene Standards (TOMP, GBFS) integrieren Sharing/ÖPNV. Ein Marktplatz ermöglicht lokale Anbieter-Snippets mit Verifizierung. Alle Entscheidungen sind erklärbar, versioniert und auditierbar.



# Packliste
curl -X POST localhost:8000/v1/packlist -H "content-type: application/json" \
  -d '{"destination":"Porto","days":4,"activities":["beach"]}'

# Green Routes
curl -X POST localhost:8000/v1/green-routes -H "content-type: application/json" \
  -d '{"origin":"Leipzig","destination":"Dresden","mode":"bus"}'

# Budget
curl -X POST localhost:8000/v1/budget-plan -H "content-type: application/json" \
  -d '{"destination":"Paris","days":3,"budget_eur":300,"style":"balanced"}'

# LocalLens (AI)
curl -X POST localhost:8000/v1/local-lens -H "content-type: application/json" \
  -d '{"city":"Hamburg","themes":["Hafencafés","Musik"],"language":"de"}'
