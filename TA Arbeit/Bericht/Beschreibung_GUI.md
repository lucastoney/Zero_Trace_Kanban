# **Beschreibung der grafischen Benutzeroberfläche**

Zero Trace bietet eine grafische Benutzeroberfläche, über die sich Netzwerkscans konfigurieren und darstellen lassen.

Die gesamte Aufbau ist übersichtlich, und sie ist in mehrere klar getrennte Bereiche gegliedert.

# **Aufbau der GUI**

## Sidebar (links):

Die Sidebar zeigt den Namen des Tools "Zero Trace" sowie den Menüpunkt "Dashboard". Weitere Menüpunkte sind bewusst weggelassen, um die Bedienung einfach zu halten.

## Header (oben):

Im Header wird der Titel "Zero Trace" sowie eine kurze Beschreibung des Tools angezeigt. Dies dient der Orientierung des Benutzers.

## Dashboard-Karten:

Im oberen Bereich befinden sich drei Informationskarten:
* Hosts im Netzwerk
* Gefundene offene Ports
* Erstellte Reports

Diese Karten geben einen schnellen Überblick über den Scan-Status.

## **Scan-Konfiguration (links):**

Hier kann der Benutzer:

* das Zielnetzwerk im CIDR-Format eingeben,
* den zu scannenden Port-Bereich festlegen,
* optional nur aktive Hosts anzeigen lassen.

Zusätzlich muss der Benutzer bestätigen, dass der Scan gemäss DSG (SR 235.1) erfolgt und er dazu berechtigt ist.

Erst nach dieser Bestätigung wird der Button „Netzwerk scannen“ aktiviert.

## **Scan-Ergebnisse (rechts):**

Die Ergebnisse werden tabellarisch dargestellt. Angezeigt werden:
* IP-Adresse
* Hostname
* Offene Ports
* Bemerkung

## **Statusleiste (unten):**

Die Statusleiste informiert den Benutzer über den aktuellen Zustand wie z. B. ob die DSG-Bestätigung noch fehlt oder der Scan gestartet wurde.