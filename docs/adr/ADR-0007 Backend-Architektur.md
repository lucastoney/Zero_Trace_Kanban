# Architecture Decision Record: Backend wird in Python entwickelt

## Status
Accepted

## Kontext
Für das geplante System wird ein Backend benötigt, das flexibel erweiterbar, gut wartbar und für Automatisierungs- sowie spätere Security-/Pentesting-Funktionen geeignet ist.
Das Team verfügt über vorhandenes Wissen oder Lernfortschritt in Python, und viele der angestrebten Funktionen (Bots, Automatisierung, Datenverarbeitung, API-Schnittstellen) lassen sich mit diesem Ökosystem sehr gut abbilden.

## Entscheidung
Das Backend wird in Python implementiert.

## Begründung
- Python bietet eine große Menge an stabilen und gut dokumentierten Libraries für Automatisierung, Systeminteraktion, Security-Tools und Webentwicklung.
- Durch leichte Lesbarkeit ist das System langfristig einfacher wartbar.
- Die Entwicklungszeit wird reduziert, da Python für Prototyping und MVPs besonders effizient ist.
- Das Ökosystem (FastAPI, Flask, asyncio, uvicorn etc.) ermöglicht performante und moderne Web-APIs.
- Python ist ideal geeignet für lokale Bots, Skripting, Dateiverarbeitung, Machine Learning, Security-Scans und API-basierte Systeme.
- Beste Lern- und Erweiterungsmöglichkeiten für zukünftige Features (z. B. Bots, Worker, KI-Funktionen).


### Positive
- Schnelle Entwicklungszyklen, ideal für MVP und spätere Erweiterungen.
- Enorme Bibliotheksauswahl für geplante Automations- und Security-Features.
- Gute Lesbarkeit und Wartbarkeit.
- Perfekt für Cross-Platform-Bots, lokale Systeminteraktion und API-Strukturen.

### Negative
- Höhere RAM- und CPU-Anforderungen als kompilierten Sprachen (z. B. Go oder Rust).
- Performance bei extrem hohen Lasten geringer; erfordert ggf. Worker- oder Microservice-Ansätze.
- Threading begrenzt durch GIL (aber lösbar über Multiprocessing oder Async).