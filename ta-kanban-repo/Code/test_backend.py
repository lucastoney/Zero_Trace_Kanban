# test_backend.py
import textwrap
from pathlib import Path

import pytest

import backend
from backend import ScanResult


def test_run_network_scan_parses_single_up_host(monkeypatch):
    """TDD-Idee:
    RED: Test schreibt Erwartung an Parsing
    GREEN: run_network_scan implementieren
    REFACTOR: Code aufräumen, Tests bleiben grün.
    """

    # Fake-Nmap-XML mit einem aktiven Host
    xml = textwrap.dedent(
        """
        <nmaprun>
          <host>
            <status state="up"/>
            <address addr="192.168.10.10" addrtype="ipv4"/>
            <hostnames>
              <hostname name="fileserver"/>
            </hostnames>
          </host>
        </nmaprun>
        """
    )

    def fake_run_nmap(args):
        return xml

    monkeypatch.setattr(backend, "_run_nmap", fake_run_nmap)

    results = backend.run_network_scan("192.168.10.0/24", only_up=True)

    assert len(results) == 1
    r = results[0]
    assert r.ip == "192.168.10.10"
    assert r.hostname == "fileserver"
    assert r.open_ports == ""             # Netzwerkscan → keine Ports
    assert "Host" in r.comment            # Kommentar z.B. "Host aktiv"


def test_run_network_scan_filters_down_hosts(monkeypatch):
    """Hosts mit state='down' sollen bei only_up=True nicht zurück kommen."""
    xml = textwrap.dedent(
        """
        <nmaprun>
          <host>
            <status state="down"/>
            <address addr="192.168.10.20" addrtype="ipv4"/>
          </host>
        </nmaprun>
        """
    )

    monkeypatch.setattr(backend, "_run_nmap", lambda args: xml)

    results = backend.run_network_scan("192.168.10.0/24", only_up=True)
    assert results == []   # leer


def test_run_port_scan_collects_open_ports(monkeypatch):
    """Portscan soll offene Ports in einen String wie '80/tcp, 443/tcp' schreiben."""
    xml = textwrap.dedent(
        """
        <nmaprun>
          <host>
            <status state="up"/>
            <address addr="192.168.10.10" addrtype="ipv4"/>
            <hostnames>
              <hostname name="fileserver"/>
            </hostnames>
            <ports>
              <port protocol="tcp" portid="80">
                <state state="open"/>
              </port>
              <port protocol="tcp" portid="443">
                <state state="open"/>
              </port>
              <port protocol="tcp" portid="22">
                <state state="closed"/>
              </port>
            </ports>
          </host>
        </nmaprun>
        """
    )

    monkeypatch.setattr(backend, "_run_nmap", lambda args: xml)

    results = backend.run_port_scan("192.168.10.10", "1-65535")
    assert len(results) == 1
    r = results[0]
    assert r.ip == "192.168.10.10"
    assert r.hostname == "fileserver"
    assert r.open_ports in ("80/tcp, 443/tcp", "443/tcp, 80/tcp")  # Reihenfolge egal
    assert "Port" in r.comment


def test_export_results_to_pdf_creates_file(tmp_path: Path):
    """PDF-Export soll eine nicht-leere PDF-Datei erzeugen."""
    results = [
        ScanResult(
            ip="192.168.10.10",
            hostname="fileserver",
            open_ports="80/tcp, 443/tcp",
            comment="Server online; Ports gescannt",
        )
    ]

    out_file = tmp_path / "test_report.pdf"
    pdf_path = backend.export_results_to_pdf(
        results=results,
        output_path=out_file,
        scan_type="Netzwerkscan",
        meta_network="192.168.10.0/24",
        meta_ports="1-65535",
    )

    assert pdf_path.exists()
    assert pdf_path.stat().st_size > 0
