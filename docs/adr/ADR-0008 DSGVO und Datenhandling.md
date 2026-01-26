# ADR-0008 Einhaltung von DSGVO und DSG

*Status:* Accepted  
*Datum:* 15.12.2025  
*Autor:* Team  
*Betroffene Bereiche:* Datenspeicherung  

---

## 1. Ausgangslage
- Der Schwachstellen‑Portscanner wird lokal auf den Systemen der Nutzer betrieben und analysiert deren Netzwerke auf Sicherheitslücken.  
- Da er lokal ausgeführt wird, werden keine Scan‑Daten in die Cloud übertragen. Dennoch können personenbezogene Daten wie IP‑Adressen oder Hostinformationen verarbeitet werden.  
- Da das System in der Schweiz eingesetzt wird, unterliegt es sowohl der Datenschutz-Grundverordnung (DSGVO, EU) als auch dem Schweizer Datenschutzgesetz (DSG, SR 235.1).

## Begründung
- IP‑Adressen und Systemkennungen gelten als personenbezogene Daten, sofern sie Rückschlüsse auf natürliche Personen zulassen.  
- Der Scanner verarbeitet Daten ausschließlich zum Zweck der IT‑Sicherheit, was sowohl nach Art. 6 Abs. 1 lit. f DSGVO als auch nach Art. 4 DSG zulässig ist.  
- Die lokale Ausführung reduziert das Risiko unbefugter Datenübertragungen an Dritte.  
- Datenschutz‑by‑Design und Datenschutz‑by‑Default werden durch die Architektur gewährleistet: nur notwendige Daten werden erfasst, gespeichert und verarbeitet.  
- Einhaltung von Datensparsamkeit, Zugriffskontrolle und zeitlich begrenzter Speicherung schützt die Rechte betroffener Personen.  

---

## 2. Entscheidung
Der Schwachstellen‑Portscanner wird so entwickelt, dass er DSGVO- und DSG-konform arbeitet und ausschließlich lokal betrieben wird.

[Siehe Begründung ADR-0008](Begründung-ADR.md#adr-0008)  