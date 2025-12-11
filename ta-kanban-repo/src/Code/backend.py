"""
backend.py - Lokales Backend für ZeroTrace

Funktionen:
- Netzwerkscan mit Nmap (-sn)
- Portscan mit Nmap (-sT -p)
- Export von Scan-Ergebnissen als PDF

Voraussetzungen:
- Nmap installiert (
- Python 3.8+
- Für PDF-Export: pip install reportlab
"""


from __future__ import annotations

import logging
import shutil
import subprocess
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Literal, Optional

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# -------------------------------------------------------------------
# Datenmodell
# -------------------------------------------------------------------


@dataclass
class ScanResult:
    """Repräsentiert ein einzelnes Scan-Ergebnis (eine Zeile im GUI)."""

    ip: str
    hostname: str
    open_ports: str
    comment: str


class NmapError(Exception):
    """Spezifischer Fehler für Nmap-Probleme."""
    pass


ScanType = Literal["network", "port"]


# -------------------------------------------------------------------
# Nmap finden & ausführen
# -------------------------------------------------------------------

def _find_nmap() -> str:
    """
    Sucht die Nmap-Executable.

    Reihenfolge:
    1. Falls Umgebungsvariable ZERO_TRACE_NMAP gesetzt ist → nehmen
    2. PATH (shutil.which("nmap"))
    3. Typische Windows-Pfade

    Falls nichts gefunden wird → NmapError.
    """

    # 1) Benutzerdefinierter Pfad (optional)
    env_path = Path.cwd().joinpath("nmap.exe")  # z.B. im Projektordner
    if env_path.is_file():
        logger.info("Using nmap from project folder: %s", env_path)
        return str(env_path)

    # 2) PATH
    exe = shutil.which("nmap")
    if exe:
        logger.info("Using nmap from PATH: %s", exe)
        return exe

    # 3) Typische Windows-Pfade
    common_paths = [
        r"C:\Program Files (x86)\Nmap\nmap.exe",
        r"C:\Program Files\Nmap\nmap.exe",
    ]
    for p in common_paths:
        if Path(p).is_file():
            logger.info("Using nmap from common path: %s", p)
            return p

    # Wenn wir hier sind → nichts gefunden
    raise NmapError(
        "Nmap wurde nicht gefunden.\n\n"
        "Bitte prüfe folgendes:\n"
        "  • Ist Nmap installiert?\n"
        "  • Liegt nmap.exe z. B. unter:\n"
        "        C:\\Program Files (x86)\\Nmap\\nmap.exe\n"
        "        C:\\Program Files\\Nmap\\nmap.exe\n"
        "  • Alternativ: Füge den Nmap-Ordner zur PATH-Umgebungsvariablen hinzu.\n"
    )


def _run_nmap(args: list[str]) -> str:
    """
    Führt Nmap mit den gegebenen Argumenten aus und gibt die XML-Ausgabe zurück.
    Alles läuft lokal, es wird keine Shell verwendet.
    """
    nmap_exe = _find_nmap()
    cmd = [nmap_exe] + args + ["-oX", "-"]  # -oX - -> XML auf stdout

    logger.info("Running nmap: %s", " ".join(cmd))

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except FileNotFoundError as e:
        # Falls nmap_exe doch nicht existiert
        raise NmapError(
            f"Nmap konnte nicht gestartet werden ({nmap_exe}).\n"
            f"Systemfehler: {e}"
        ) from e

    if proc.returncode != 0:
        stderr = (proc.stderr or "").strip()
        raise NmapError(stderr or "Nmap ist mit einem Fehlercode beendet worden.")

    return proc.stdout

# Netzwerkscan

def run_network_scan(cidr: str, only_up: bool = True) -> List[ScanResult]:
    """
    Führt einen Netzwerkscan (Host-Discovery) über ein CIDR-Netz aus.

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
                open_ports="",   # Netzwerkscan: keine Portinfos
                comment=comment,
            )
        )

    return results

# Portscan

def run_port_scan(target: str, ports: str) -> List[ScanResult]:
    """
    Führt einen Portscan auf einem Ziel durch.

        nmap -sT -p <ports> <target> -oX -

    Args:
        target: IP oder Hostname, z.B. "192.168.10.10"
        ports: Nmap-Portangabe, z.B. "1-1024" oder "22,80,443"

    Returns:
        Liste von ScanResult. Meist nur ein Eintrag (1 Host),
        aber Nmap erlaubt mehrere Ziele.
    """
    xml_text = _run_nmap(["-sT", "-p", ports, target])
    root = ET.fromstring(xml_text)
    results: List[ScanResult] = []

    for host in root.findall("host"):
        status_el = host.find("status")
        state = status_el.get("state") if status_el is not None else "unknown"
        if state != "up":
            continue

        # IP
        ip = ""
        addr = host.find("address")
        if addr is not None and addr.get("addrtype") in ("ipv4", "ipv6"):
            ip = addr.get("addr", "")

        # Hostname
        hostname = ""
        hostnames = host.find("hostnames")
        if hostnames is not None:
            for hn in hostnames.findall("hostname"):
                name = hn.get("name")
                if name:
                    hostname = name
                    break

        # Ports
        open_ports: list[str] = []
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
    scan_type: str,
    meta_network: Optional[str] = None,
    meta_ports: Optional[str] = None,
) -> Path:
    """
    Erstellt einen einfachen PDF-Report aus einer Liste von ScanResult.

    Args:
        results: Die Daten, z.B. aus dem Treeview übernommen.
        output_path: Ziel-Dateipfad (muss nicht existieren).
        scan_type: Text für den Scan-Typ (z.B. 'Netzwerkscan', 'Port-Scan', 'Benutzerdefinierter Scan').
        meta_network: Optionale Info (z.B. eingegebenes CIDR).
        meta_ports: Optionale Info (z.B. eingegebener Portbereich).

    Returns:
        Der Pfad zur erzeugten PDF-Datei.
    """
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.units import mm
        from reportlab.pdfgen import canvas
    except ImportError as e:
        # Schöne, verständliche Fehlermeldung
        raise RuntimeError(
            "Report-Export benötigt das Python-Paket 'reportlab'.\n\n"
            "Bitte im Projekt-Umfeld installieren:\n"
            "    python -m pip install reportlab"
        ) from e

    output_path = output_path.with_suffix(".pdf")
    c = canvas.Canvas(str(output_path), pagesize=A4)
    width, height = A4

    margin = 20 * mm
    y = height - margin

    # Kopf
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

    # Risiko-Legende (Portscan)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin, y, "Risikostufen (Portscan):")
    y -= 5 * mm

    c.setFont("Helvetica", 9)
    c.drawString(margin + 5 * mm, y, "■ Critical  – stark angreifbare Dienste")
    y -= 5 * mm
    c.drawString(margin + 5 * mm, y, "▣ Mid       – typische Internet-/Mail-Dienste")
    y -= 5 * mm
    c.drawString(margin + 5 * mm, y, "□ Low       – sonstige offene Ports")
    y -= 8 * mm

    # Tabellen-Header – an GUI angepasst
    c.setFont("Helvetica-Bold", 9)
    col_ip = margin
    col_host = margin + 40 * mm
    col_ports = margin + 90 * mm
    col_comment = margin + 140 * mm

    c.drawString(col_ip, y, "IP-Adresse")
    c.drawString(col_host, y, "Hostname")
    c.drawString(col_ports, y, "Offene Ports")
    c.drawString(col_comment, y, "Kommentar")
    y -= 4 * mm
    c.line(margin, y, width - margin, y)
    y -= 6 * mm

    # Zeilen
    c.setFont("Helvetica", 8)
    line_height = 5 * mm

    for r in results:
        if y < margin + 20 * mm:
            c.showPage()
            y = height - margin
            c.setFont("Helvetica-Bold", 9)
            c.drawString(col_ip, y, "IP-Adresse")
            c.drawString(col_host, y, "Hostname")
            c.drawString(col_ports, y, "Offene Ports")
            c.drawString(col_comment, y, "Kommentar")
            y -= 4 * mm
            c.line(margin, y, width - margin, y)
            y -= 6 * mm
            c.setFont("Helvetica", 8)

        # open_ports kommt bereits dekoriert (z.B. '■ 22/tcp, ▣ 80/tcp')
        c.drawString(col_ip, y, r.ip)
        c.drawString(col_host, y, (r.hostname or "")[:20])
        c.drawString(col_ports, y, (r.open_ports or "")[:45])
        c.drawString(col_comment, y, (r.comment or "")[:40])
        y -= line_height

    c.showPage()
    c.save()
    return output_path
