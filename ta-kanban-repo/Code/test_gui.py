# test_gui.py
import Gui  # deine Gui.py (mit großem G)

from backend import ScanResult


def _create_app():
    """Hilfsfunktion: GUI-Fenster erstellen und am Ende wieder zerstören."""
    app = Gui.ZeroTraceGUI()
    app.update()  # einmal initial layouten
    return app


def test_update_scan_button_state_enables_button_for_network_scan():
    """Wenn Netzwerkscan + DSG angehakt sind, soll der Button aktiv sein
    und den richtigen Text anzeigen.
    """
    app = _create_app()
    try:
        app.scan_network_var.set(True)
        app.scan_port_var.set(False)
        app.dsg_confirm.set(True)

        app._update_scan_button_state()

        assert str(app.btn_scan["state"]) == "normal"
        assert "Netzwerkscan" in str(app.btn_scan["text"])
    finally:
        app.destroy()


def test_update_scan_button_state_custom_scan_text():
    """Wenn Netzwerk + Port ausgewählt sind, soll 'Benutzerdefiniert' im Button stehen."""
    app = _create_app()
    try:
        app.scan_network_var.set(True)
        app.scan_port_var.set(True)
        app.dsg_confirm.set(True)

        app._update_scan_button_state()

        text = str(app.btn_scan["text"])
        assert "Benutzerdefiniert" in text or "Benutzerdefinierter" in text
    finally:
        app.destroy()


def test_run_scan_calls_backend_functions(monkeypatch):
    """TDD-Stil:
    - Wir erwarten, dass bei aktivem Netzwerkscan unsere Fake-Funktion aufgerufen wird
    - Die GUI soll das Ergebnis in den Treeview schreiben.
    """
    app = _create_app()
    try:
        called = {"net": None, "port": None}

        def fake_run_network_scan(cidr, only_up):
            called["net"] = (cidr, only_up)
            return [
                ScanResult(
                    ip="192.168.10.10",
                    hostname="fileserver",
                    open_ports="",
                    comment="Host aktiv",
                )
            ]

        def fake_run_port_scan(target, ports):
            called["port"] = (target, ports)
            return [
                ScanResult(
                    ip="192.168.10.10",
                    hostname="fileserver",
                    open_ports="80/tcp",
                    comment="Ports gescannt",
                )
            ]

        # Backend-Funktionen im GUI-Modul ersetzen
        monkeypatch.setattr(Gui, "run_network_scan", fake_run_network_scan)
        monkeypatch.setattr(Gui, "run_port_scan", fake_run_port_scan)

        # Netzwerk + Port-Scan aktivieren → benutzerdefinierter Scan
        app.scan_network_var.set(True)
        app.scan_port_var.set(True)
        app.dsg_confirm.set(True)
        app.entry_network.delete(0, "end")
        app.entry_network.insert(0, "192.168.10.0/24")
        app.entry_ports.delete(0, "end")
        app.entry_ports.insert(0, "1-1024")

        app._update_scan_button_state()
        app._run_scan()

        # Erwartung: beide Fake-Funktionen wurden aufgerufen
        assert called["net"] == ("192.168.10.0/24", app.only_active_var.get())
        assert called["port"] == ("192.168.10.0/24", "1-1024")

        # Und im Treeview gibt es nun mindestens einen Eintrag
        items = app.tree.get_children()
        assert len(items) >= 1

        values = app.tree.item(items[0], "values")
        assert values[0] == "192.168.10.10"   # IP
        assert "fileserver" in values[1]      # Hostname
    finally:
        app.destroy()
