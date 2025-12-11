# Damalige zweite Version des Backends welche aber funktionierte

"""
Funktionen:
- Netzwerkscan mit Nmap (-sn)
- Portscan mit Nmap (-sT -p)
- Export von Scan-Ergebnissen als PDF

Voraussetzungen:
- Nmap installiert
"""

from __future__ import annotations

import subprocess
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Literal

# Falls wir logging wollen
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Datenmodell

@dataclass
class ScanResult:
    """Repräsentiert ein einzelnes Scan-Ergebnis."""

    ip: str
    hostname: str
    open_ports: str
    comment: str


class NmapError(Exception):
    """Spezifischer Fehler für Nmap-Probleme."""
    pass


ScanType = Literal["network", "port"]


# Nmap-Aufrufe Lokal


def _run_nmap(args: list[str]) -> str:
    """
    Führt Nmap mit den gegebenen Argumenten aus und gibt die XML-Ausgabe zurück.

    Es wird KEINE Shell verwendet (sicherer), alles läuft lokal.
    """
    cmd = ["nmap"] + args + ["-oX", "-"]  # -oX - → XML auf stdout

    logger.info("Running nmap: %s", " ".join(cmd))

    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if proc.returncode != 0:
        stderr = proc.stderr.strip()
        raise NmapError(stderr or "Nmap failed with unknown error")
    return proc.stdout


def run_network_scan(cidr: str, only_up: bool = True) -> List[ScanResult]:
    """
    Führt einen Netzwerkscan (Host-Discovery) über ein CIDR-Netz aus.

    Verwendet:
      nmap -sn <cidr> -oX -

    Args:
     cidr: z.B. "192.168.10.0/24"
     only_up: Wenn True, nur Hosts mit Status "up" ausgeben.

    Returns:
      Liste von ScanResult, die direkt ins Treeview übernommen werden kann.
    """
    xml_text = _run_nmap(["-sn", cidr])
    root = ET.fromstring(xml_text)
    results: List[ScanResult] = []

    for host in root.findall("host"):
        status_el = host.find("status")
        state = status_el.get("state") if status_el is not None else "unknown"
        if only_up and state != "up":
            continue

        # IP-Adresse
        ip = ""
        addr = host.find("address")
        if addr is not None and addr.get("addrtype") in ("ipv4", "ipv6"):
            ip = addr.get("addr", "")

        # Hostname (falls vorhanden)
        hostname = ""
        hostnames = host.find("hostnames")
        if hostnames is not None:
            for hn in hostnames.findall("hostname"):
                name = hn.get("name")
                if name:
                    hostname = name
                    break

        comment = "Host aktiv" if state == "up" else f"Status: {state}"
        results.append(
            ScanResult(
                ip=ip or "(unbekannt)",
                hostname=hostname,
                open_ports="",  # Netzwerkscan prüft hier nur Erreichbarkeit
                comment=comment,
            )
        )

    return results


def run_port_scan(target: str, ports: str) -> List[ScanResult]:
    """
    Führt einen Portscan auf dem Ziel durch.

    Verwendet:
     nmap -sT -p <ports> <target> -oX -

    Args:
    target: IP oder Hostname, z.B. "192.168.10.10"
    ports: Nmap-Portangabe, z.B. "1-1024" oder "22,80,443"

    Returns:
    Liste von ScanResult.
    Nmap erlaubt mehrere Ziele.
    """
    xml_text = _run_nmap(["-sT", "-p", ports, target])
    root = ET.fromstring(xml_text)
    results: List[ScanResult] = []

    for host in root.findall("host"):
        status_el = host.find("status")
        state = status_el.get("state") if status_el is not None else "unknown"
        if state != "up":
            # Nicht erreichbare Hosts ignorieren
            continue

        # IP-Adresse
        ip = ""
        addr = host.find("address")
        if addr is not None and addr.get("addrtype") in ("ipv4", "ipv6"):
            ip = addr.get("addr", "")

        # Hostname (falls vorhanden)
        hostname = ""
        hostnames = host.find("hostnames")
        if hostnames is not None:
            for hn in hostnames.findall("hostname"):
                name = hn.get("name")
                if name:
                    hostname = name
                    break

        # Ports sammeln
        open_ports = []
        ports_el = host.find("ports")
        if ports_el is not None:
            for port_el in ports_el.findall("port"):
                state_el = port_el.find("state")
                if state_el is None:
                    continue
                if state_el.get("state") != "open":
                    continue
                portid = port_el.get("portid", "?")
                proto = port_el.get("protocol", "tcp")
                open_ports.append(f"{portid}/{proto}")

        ports_str = ", ".join(open_ports) if open_ports else "Keine offenen Ports"
        comment = "Portscan abgeschlossen"

        results.append(
            ScanResult(
                ip=ip or "(unbekannt)",
                hostname=hostname,
                open_ports=ports_str,
                comment=comment,
            )
        )

    return results



# PDF-Export


def export_results_to_pdf(
    results: List[ScanResult],
    output_path: Path,
    scan_type: ScanType,
    meta_network: Optional[str] = None,
    meta_ports: Optional[str] = None,
) -> Path:
    """
    Erstellt einen einfachen PDF-Report aus einer Liste von ScanResult.

    Args:
     results: Die Daten, z.B. aus dem Treeview übernommen.
     output_path: Ziel-Dateipfad (muss nicht existieren).
    scan_type: "network" oder "port".
     meta_network: Optionale Info (z.B. eingegebenes CIDR).
      meta_ports: Optionale Info (z.B. eingegebener Portbereich).

    Returns:
     Der Pfad zur erzeugten PDF-Datei.
    """
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas

    output_path = output_path.with_suffix(".pdf")
    c = canvas.Canvas(str(output_path), pagesize=A4)
    width, height = A4

    # Kopfbereich
    margin = 20 * mm
    y = height - margin

    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin, y, "ZeroTrace Scan-Report")
    y -= 10 * mm

    c.setFont("Helvetica", 10)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.drawString(margin, y, f"Erstellt am: {ts}")
    y -= 6 * mm

    c.drawString(margin, y, f"Scan-Typ: {scan_type}")
    y -= 6 * mm

    if meta_network:
        c.drawString(margin, y, f"Netzwerk: {meta_network}")
        y -= 6 * mm
    if meta_ports:
        c.drawString(margin, y, f"Port-Bereich: {meta_ports}")
        y -= 8 * mm

    # Tabellen-Header
    c.setFont("Helvetica-Bold", 9)
    col_ip = margin
    col_host = margin + 40 * mm
    col_ports = margin + 90 * mm
    col_comment = margin + 140 * mm

    c.drawString(col_ip, y, "IP")
    c.drawString(col_host, y, "Hostname")
    c.drawString(col_ports, y, "Offene Ports")
    c.drawString(col_comment, y, "Bemerkung")
    y -= 4 * mm
    c.line(margin, y, width - margin, y)
    y -= 6 * mm

    # Tabellen-Zeilen
    c.setFont("Helvetica", 8)
    line_height = 5 * mm

    for r in results:
        if y < margin + 20 * mm:
            c.showPage()
            y = height - margin
            c.setFont("Helvetica-Bold", 9)
            c.drawString(col_ip, y, "IP")
            c.drawString(col_host, y, "Hostname")
            c.drawString(col_ports, y, "Offene Ports")
            c.drawString(col_comment, y, "Bemerkung")
            y -= 4 * mm
            c.line(margin, y, width - margin, y)
            y -= 6 * mm
            c.setFont("Helvetica", 8)

        c.drawString(col_ip, y, r.ip)
        c.drawString(col_host, y, r.hostname[:20])
        c.drawString(col_ports, y, r.open_ports[:25])
        c.drawString(col_comment, y, r.comment[:30])
        y -= line_height

    c.showPage()
    c.save()
    return output_path
