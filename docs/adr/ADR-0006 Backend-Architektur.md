# Backend-Architektur

## Status
*Status:* Accepted  
*Datum:* 03.12.2025  
*Autor:* Team  
*Betroffene Bereiche:* Scann Engine

## 1. Ausgangslage
Für das geplante System wird eine Engine benötigt, die flexibel erweiterbar, gut wartbar und für Automatisierungs- sowie spätere Security-/Pentesting-Funktionen geeignet ist.
Das Team verfügt über vorhandenes Wissen oder Lernfortschritt in Python, und viele der angestrebten Funktionen (Bots, Automatisierung, Datenverarbeitung, API-Schnittstellen) lassen sich mit diesem Ökosystem sehr gut abbilden.

## Begründung
- Python bietet eine grosse Menge an stabilen und gut dokumentierten Libraries für Automatisierung, Systeminteraktion, Security-Tools und Webentwicklung.
- Durch leichte Lesbarkeit ist das System langfristig einfacher wartbar.
- Die Entwicklungszeit wird reduziert, da Python für Prototyping und MVPs besonders effizient ist.
- Das Ökosystem (FastAPI, Flask, asyncio, uvicorn etc.) ermöglicht performante und moderne Web-APIs.
- Python ist ideal geeignet für lokale Bots, Skripting, Dateiverarbeitung, Machine Learning, Security-Scans und API-basierte Systeme.
- Beste Lern- und Erweiterungsmöglichkeiten für zukünftige Features (z. B. Bots, Worker, KI-Funktionen).

## 2. Entscheidung
Die Scann Engine wird in Python programmiert

[Siehe Begründung ADR-0002](Begründung-ADR.md#adr-0002)