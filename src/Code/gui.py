import threading
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime

from backend import (
    run_network_scan,
    run_port_scan,
    export_results_to_pdf,
    ScanResult,
    NmapError,
)

# Farben – moderne, flache Optik
BG_APP = "#f3f4f6"   # Gesamt-Hintergrund
BG_SIDEBAR = "#111827"
BG_HEADER = "#ffffff"
BG_CARD = "#ffffff"
BG_STATUS = "#f9fafb"
ACCENT = "#2563eb"
ACCENT_SOFT = "#dbeafe"
TEXT_DARK = "#111827"
TEXT_MUTED = "#6b7280"
TEXT_LIGHT = "#f9fafb"
BORDER = "#e5e7eb"

# Risiko-Klassifizierung für Ports
CRITICAL_PORTS = {
    21,   # FTP
    22,   # SSH
    23,   # Telnet
    25,   # SMTP
    135,  # MS RPC
    139,  # NetBIOS
    445,  # SMB
    1433, # MS SQL
    3306, # MySQL
    3389, # RDP
    5900, # VNC
}

MID_PORTS = {
    53,   # DNS
    80,   # HTTP
    110,  # POP3
    143,  # IMAP
    993,  # IMAPS
    995,  # POP3S
    8080, # HTTP-Proxy / Alt-HTTP
}

# Risiko-Symbole
SYM_CRIT = "■"
SYM_MID  = "▣"
SYM_LOW  = "□"

# einfache Dienstnamen für Port-Definitionen
PORT_SERVICE_NAMES = {
    21: "FTP – Dateiübertragung (unverschlüsselt)",
    22: "SSH – Sicherer Fernzugriff",
    23: "Telnet – Fernzugriff (unverschlüsselt)",
    25: "SMTP – E-Mail Versand",
    53: "DNS – Namensauflösung",
    80: "HTTP – Webserver",
    110: "POP3 – Posteingang (unverschlüsselt)",
    143: "IMAP – Posteingang",
    135: "MS RPC – Windows-RPC-Dienst",
    139: "NetBIOS – Dateifreigaben (alt)",
    445: "SMB – Windows-Dateifreigaben",
    993: "IMAPS – Posteingang (verschlüsselt)",
    995: "POP3S – Posteingang (verschlüsselt)",
    1433: "MS SQL – Datenbank",
    3306: "MySQL – Datenbank",
    3389: "RDP – Remote Desktop",
    5900: "VNC – Fernsteuerung",
    8080: "HTTP-Proxy / Webdienst",
}


class ZeroTraceGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Basis-Fenster
        self.title("Zero Trace – Lokaler Sicherheits-Scanner (MVP)")
        # gewünschte Standardgröße
        self.geometry("1100x650")
        self.minsize(980, 580)
        self.configure(bg=BG_APP)

        # Fenster nach dem Setzen der Größe in die Mitte verschieben
        self.update_idletasks()
        w, h = 1100, 650
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")

        self._progress_win: tk.Toplevel | None = None
        self._scan_cancelled: bool = False

        self._init_style()
        self._build_layout()


    # Styling
    def _init_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        # Basis
        style.configure(
            ".",
            background=BG_APP,
            foreground=TEXT_DARK,
            fieldbackground="white",
            font=("Segoe UI", 10),
        )

        # Rahmen & Labels
        style.configure("TFrame", background=BG_APP)
        style.configure("Card.TFrame", background=BG_CARD, relief="flat")
        style.configure(
            "Card.TLabelframe",
            background=BG_CARD,
            relief="flat",
            borderwidth=1,
            bordercolor=BORDER,
            padding=12,
        )
        style.configure(
            "Card.TLabelframe.Label",
            background=BG_CARD,
            foreground=TEXT_MUTED,
            font=("Segoe UI Semibold", 10),
        )
        style.configure(
            "Card.TLabel",
            background=BG_CARD,
            foreground=TEXT_DARK,
            font=("Segoe UI", 10),
        )

        # Entry
        style.configure(
            "TEntry",
            padding=6,
            borderwidth=1,
            relief="solid",
        )
        style.map(
            "TEntry",
            bordercolor=[("focus", ACCENT)],
        )

        # Checkbox
        style.configure(
            "TCheckbutton",
            background=BG_CARD,
            foreground=TEXT_DARK,
            font=("Segoe UI", 9),
        )

        # Primär-Button
        style.configure(
            "Primary.TButton",
            background=ACCENT,
            foreground="white",
            borderwidth=0,
            padding=(10, 6),
            font=("Segoe UI Semibold", 10),
        )
        style.map(
            "Primary.TButton",
            background=[
                ("active", "#1d4ed8"),
                ("disabled", "#9ca3af"),
            ],
            foreground=[
                ("disabled", "#f3f4f6"),
            ]
        )

        # Sekundär-Button
        style.configure(
            "Secondary.TButton",
            background=BG_CARD,
            foreground=ACCENT,
            borderwidth=1,
            padding=(10, 6),
            font=("Segoe UI", 10),
        )
        style.map(
            "Secondary.TButton",
            background=[("active", ACCENT_SOFT)],
            foreground=[("disabled", "#9ca3af")],
        )

        # Sidebar
        style.configure(
            "Sidebar.TLabel",
            background=BG_SIDEBAR,
            foreground=TEXT_MUTED,
            font=("Segoe UI", 10),
        )
        style.configure(
            "SidebarTitle.TLabel",
            background=BG_SIDEBAR,
            foreground=TEXT_LIGHT,
            font=("Segoe UI Semibold", 14),
        )
        style.configure(
            "SidebarItemActive.TLabel",
            background=BG_SIDEBAR,
            foreground=TEXT_LIGHT,
            font=("Segoe UI", 10),
        )

        # Header
        style.configure(
            "HeaderTitle.TLabel",
            background=BG_HEADER,
            foreground=TEXT_DARK,
            font=("Segoe UI Semibold", 18),
        )
        style.configure(
            "HeaderSub.TLabel",
            background=BG_HEADER,
            foreground=TEXT_MUTED,
            font=("Segoe UI", 9),
        )
        # eigener Frame-Style für Header: komplett weiss
        style.configure(
            "Header.TFrame",
            background=BG_HEADER,
        )

        # Sidebar-Trenner
        style.configure("Sidebar.TSeparator", background="#374151")

        # Treeview
        style.configure(
            "Treeview",
            background="white",
            foreground=TEXT_DARK,
            rowheight=24,
            fieldbackground="white",
            borderwidth=0,
            font=("Segoe UI", 9),
        )
        style.configure(
            "Treeview.Heading",
            background="#f3f4f6",
            foreground=TEXT_MUTED,
            relief="flat",
            font=("Segoe UI Semibold", 9),
        )
        style.map("Treeview.Heading", background=[("active", "#e5e7eb")])

        # Statusbar
        style.configure(
            "Status.TLabel",
            background=BG_STATUS,
            foreground=TEXT_MUTED,
            font=("Segoe UI", 9),
        )

        # Scrollbar
        style.configure(
            "Modern.Vertical.TScrollbar",
            gripcount=0,
            background="#e5e7eb",
            darkcolor="#e5e7eb",
            lightcolor="#e5e7eb",
            troughcolor="#f9fafb",
            bordercolor="#f9fafb",
            arrowcolor="#6b7280",
        )

    # Layout mit Seiten (Dashboard / Port-Definitionen)
    def _build_layout(self):
        root_frame = ttk.Frame(self, style="TFrame")
        root_frame.pack(fill="both", expand=True)
        root_frame.columnconfigure(0, weight=0)  # Sidebar
        root_frame.columnconfigure(1, weight=1)  # Main
        root_frame.rowconfigure(1, weight=1)

        # ---------- Sidebar ----------
        sidebar = tk.Frame(root_frame, bg=BG_SIDEBAR, width=210)
        sidebar.grid(row=0, column=0, rowspan=3, sticky="nsew")
        sidebar.grid_propagate(False)

        ttk.Label(sidebar, text="Zero Trace", style="SidebarTitle.TLabel").pack(
            anchor="w", padx=20, pady=(18, 10)
        )

        # Dashboard-Navigation
        frame_dash = tk.Frame(sidebar, bg=BG_SIDEBAR)
        frame_dash.pack(fill="x", pady=(2, 0))
        tk.Frame(frame_dash, bg=ACCENT, width=3, height=24).pack(side="left")
        self.nav_dashboard = ttk.Label(
            frame_dash, text="Dashboard", style="SidebarItemActive.TLabel"
        )
        self.nav_dashboard.pack(side="left", padx=14, pady=4)
        self.nav_dashboard.bind("<Button-1>", lambda e: self._show_page("dashboard"))

        # Port-Definitionen Navigation
        frame_ports = tk.Frame(sidebar, bg=BG_SIDEBAR)
        frame_ports.pack(fill="x", pady=(2, 0))
        tk.Frame(frame_ports, bg=BG_SIDEBAR, width=3, height=24).pack(side="left")
        self.nav_ports = ttk.Label(
            frame_ports, text="Port-Definitionen", style="Sidebar.TLabel"
        )
        self.nav_ports.pack(side="left", padx=14, pady=4)
        self.nav_ports.bind("<Button-1>", lambda e: self._show_page("ports"))

        # ---------- Header ----------
        header = tk.Frame(root_frame, bg=BG_HEADER, height=64)
        header.grid(row=0, column=1, sticky="nsew")
        header.grid_propagate(False)

        header_inner = ttk.Frame(header, style="Header.TFrame")
        header_inner.pack(fill="both", expand=True, padx=20, pady=10)
        header_inner.columnconfigure(0, weight=1)
        header_inner.columnconfigure(1, weight=0)

        title_frame = ttk.Frame(header_inner, style="Header.TFrame")
        title_frame.grid(row=0, column=0, sticky="w")
        ttk.Label(
            title_frame,
            text="Zero Trace – Lokale Sicherheitsanalyse",
            style="HeaderTitle.TLabel",
        ).pack(anchor="w")
        ttk.Label(
            title_frame,
            text="Führt lokale Port- und Netzwerkscans aus.",
            style="HeaderSub.TLabel",
        ).pack(anchor="w", pady=(2, 0))

        badge = ttk.Label(
            header_inner,
            text="MVP – Local",
            style="HeaderSub.TLabel",
            padding=(10, 4),
        )
        badge.configure(
            background=ACCENT_SOFT,
            foreground=ACCENT,
        )
        badge.grid(row=0, column=1, sticky="e")

        #Seiten (Dashboard & Ports)
        self.page_dashboard = ttk.Frame(root_frame, style="TFrame", padding=16)
        self.page_ports = ttk.Frame(root_frame, style="TFrame", padding=16)

        self.page_dashboard.grid(row=1, column=1, sticky="nsew")
        self.page_ports.grid(row=1, column=1, sticky="nsew")

        # Dashboard-Inhalt aufbauen
        self._build_dashboard_page(self.page_dashboard)
        # Ports-Definitionen-Seite aufbauen
        self._build_ports_page(self.page_ports)

        # ---- Statusleiste ----
        status_frame = tk.Frame(self, bg=BG_STATUS, height=24)
        status_frame.pack(fill="x", side="bottom")
        self.status_var = tk.StringVar(
            value="Bitte Scan-Modus wählen und bestätigen, dass der Scan gemäss DSG (SR 235.1) erfolgt."
        )
        ttk.Label(
            status_frame,
            textvariable=self.status_var,
            style="Status.TLabel",
            anchor="w",
            padding=(10, 2),
        ).pack(fill="x")

        # standardmässig Dashboard anzeigen
        self._show_page("dashboard")
        self._update_scan_button_state()

    def _build_dashboard_page(self, parent: ttk.Frame):
        parent.columnconfigure(0, weight=1)
        parent.columnconfigure(1, weight=1)
        parent.rowconfigure(1, weight=1)  # Ergebnisse wachsen

        # ---- Konfiguration (links oben) ----
        config = ttk.LabelFrame(
            parent, text="Scan-Konfiguration", style="Card.TLabelframe", padding=12
        )
        config.grid(row=0, column=0, sticky="nsew", padx=(0, 8), pady=(0, 8))
        config.columnconfigure(1, weight=1)

        # Netzwerk (CIDR)
        ttk.Label(config, text="Netzwerk (CIDR):", style="Card.TLabel").grid(
            row=0, column=0, sticky="w", pady=(4, 4)
        )
        self.entry_network = ttk.Entry(config)
        self.entry_network.insert(0, "192.168.10.0/24")
        self.entry_network.grid(
            row=0, column=1, sticky="we", pady=(4, 4), padx=(4, 0)
        )

        # Port-Bereich
        ttk.Label(config, text="Port-Bereich:", style="Card.TLabel").grid(
            row=1, column=0, sticky="w", pady=(4, 4)
        )
        self.entry_ports = ttk.Entry(config)
        self.entry_ports.insert(0, "1-65535")
        self.entry_ports.grid(
            row=1, column=1, sticky="we", pady=(4, 4), padx=(4, 0)
        )

        # Nur aktive Hosts
        self.only_active_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            config,
            text="Nur aktive Hosts anzeigen",
            variable=self.only_active_var,
            command=self._update_scan_button_state,
        ).grid(row=2, column=0, columnspan=2, sticky="w", pady=(6, 4))

        # Scan-Modi
        self.scan_network_var = tk.BooleanVar(value=True)
        self.scan_port_var = tk.BooleanVar(value=False)

        ttk.Checkbutton(
            config,
            text="Netzwerkscan",
            variable=self.scan_network_var,
            command=self._on_scan_mode_change,
        ).grid(row=3, column=0, columnspan=2, sticky="w", pady=(2, 2))

        ttk.Checkbutton(
            config,
            text="Port-Scan",
            variable=self.scan_port_var,
            command=self._on_scan_mode_change,
        ).grid(row=4, column=0, columnspan=2, sticky="w", pady=(2, 2))

        # Hinweis + Risiko-Legende
        ttk.Label(
            config,
            text=(
                "Hinweis: Zero Trace führt alle Analysen ausschliesslich lokal aus.\n"
                "\n"
                "Risikostufen (Portscan):\n"
                f"  {SYM_CRIT} Critical  – stark angreifbare Dienste\n"
                f"  {SYM_MID} Mid       – typische Internet-Dienste\n"
                f"  {SYM_LOW} Low       – sonstige offene Ports"
            ),
            style="Card.TLabel",
            foreground=TEXT_MUTED,
            justify="left",
        ).grid(row=5, column=0, sticky="w", pady=(4, 4))

        # DSG-Checkbox rechts
        self.dsg_confirm = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            config,
            text="Scan gemäss DSG (SR 235.1) und Berechtigung bestätigt",
            variable=self.dsg_confirm,
            command=self._on_dsg_change,
        ).grid(row=5, column=1, sticky="e", pady=(4, 4))

        # Scan-Button
        btn_frame = ttk.Frame(config)
        btn_frame.grid(row=6, column=0, columnspan=2, sticky="we", pady=(8, 0))
        btn_frame.columnconfigure(0, weight=1)

        self.btn_scan = ttk.Button(
            btn_frame,
            text="Netzwerkscan starten",
            style="Primary.TButton",
            command=self._run_scan,
            state="disabled",
        )
        self.btn_scan.grid(row=0, column=0, sticky="we")

        # ---- Scan-Ergebnisse ----
        results = ttk.LabelFrame(
            parent, text="Scan-Ergebnisse", style="Card.TLabelframe", padding=8
        )
        results.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(8, 0))
        results.columnconfigure(0, weight=1)
        results.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(
            results,
            columns=("ip", "hostname", "ports", "comment"),
            show="headings",
            style="Treeview",
            selectmode="browse",
        )
        self.tree.heading("ip", text="IP-Adresse")
        self.tree.heading("hostname", text="Hostname")
        self.tree.heading("ports", text="Offene Ports")
        self.tree.heading("comment", text="Kommentar")

        self.tree.column("ip", width=150, anchor="w")
        self.tree.column("hostname", width=180, anchor="w")
        self.tree.column("ports", width=260, anchor="w")
        self.tree.column("comment", width=220, anchor="w")

        scroll = ttk.Scrollbar(
            results,
            orient="vertical",
            command=self.tree.yview,
            style="Modern.Vertical.TScrollbar",
        )
        self.tree.configure(yscrollcommand=scroll.set)

        self.tree.grid(row=0, column=0, sticky="nsew", padx=(0, 4), pady=(4, 0))
        scroll.grid(row=0, column=1, sticky="ns", pady=(4, 0))

        self._add_example_rows()

        # ---- PDF-Button unterhalb der Ergebnisse ----
        export_frame = ttk.Frame(parent, style="TFrame")
        export_frame.grid(row=2, column=0, columnspan=2, sticky="e", pady=(10, 0))
        self.btn_pdf = ttk.Button(
            export_frame,
            text="PDF-Report erstellen",
            style="Primary.TButton",
            command=self._export_pdf,
        )
        self.btn_pdf.grid(row=0, column=0, sticky="e")

    def _build_ports_page(self, parent: ttk.Frame):
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(1, weight=1)

        intro = ttk.LabelFrame(
            parent, text="Port-Definitionen", style="Card.TLabelframe", padding=12
        )
        intro.grid(row=0, column=0, sticky="we", pady=(0, 8))
        ttk.Label(
            intro,
            text=(
                "Diese Übersicht zeigt die im Tool hinterlegten Ports und ihre Risikokategorie.\n"
                "Sie hilft dabei, auch als Nicht-Sicherheitsexperte zu verstehen, warum gewisse "
                "Dienste besonders kritisch bewertet werden.\n\n"
                f"{SYM_CRIT} Critical  – Hohe Angriffsfläche, oft direkt für Angriffe missbraucht\n"
                f"{SYM_MID} Mid       – Häufig genutzte Internet-Dienste, sollten bewusst freigegeben werden\n"
                f"{SYM_LOW} Low       – Sonstige offene Ports, in der Regel weniger kritisch\n\n"
                "Alle Ports, die hier nicht explizit aufgeführt sind, werden im Tool standardmässig als "
                "Low eingestuft."
            ),
            style="Card.TLabel",
            justify="left",
            foreground=TEXT_MUTED,
        ).pack(anchor="w")

        # Tabelle der Ports
        table_frame = ttk.Frame(parent, style="Card.TFrame", padding=8)
        table_frame.grid(row=1, column=0, sticky="nsew")
        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)

        self.ports_tree = ttk.Treeview(
            table_frame,
            columns=("port", "risk", "desc"),
            show="headings",
            style="Treeview",
            selectmode="none",
        )
        self.ports_tree.heading("port", text="Port")
        self.ports_tree.heading("risk", text="Risikostufe")
        self.ports_tree.heading("desc", text="Erläuterung")

        self.ports_tree.column("port", width=80, anchor="w")
        self.ports_tree.column("risk", width=120, anchor="w")
        self.ports_tree.column("desc", width=480, anchor="w")

        scroll_ports = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.ports_tree.yview,
            style="Modern.Vertical.TScrollbar",
        )
        self.ports_tree.configure(yscrollcommand=scroll_ports.set)

        self.ports_tree.grid(row=0, column=0, sticky="nsew", padx=(0, 4), pady=(4, 0))
        scroll_ports.grid(row=0, column=1, sticky="ns", pady=(4, 0))

        self._fill_ports_table()

    def _fill_ports_table(self):
        # Union aller bekannten Ports
        all_ports = sorted(CRITICAL_PORTS.union(MID_PORTS))
        for p in all_ports:
            if p in CRITICAL_PORTS:
                risk = f"{SYM_CRIT} Critical"
                desc = "Kritischer Dienst – sollte nur bewusst und gut abgesichert erreichbar sein."
            elif p in MID_PORTS:
                risk = f"{SYM_MID} Mid"
                desc = "Typischer Internet-Dienst – nur freigeben, wenn der Dienst wirklich genutzt wird."
            else:
                risk = f"{SYM_LOW} Low"
                desc = "Weniger kritischer Port."

            name = PORT_SERVICE_NAMES.get(p, f"Port {p}")
            full_desc = f"{name}. {desc}"
            self.ports_tree.insert(
                "", "end",
                values=(p, risk, full_desc),
            )


    # Seiten-Navigation
    def _show_page(self, which: str):
        if which == "dashboard":
            self.page_dashboard.tkraise()
            self.nav_dashboard.configure(style="SidebarItemActive.TLabel")
            self.nav_ports.configure(style="Sidebar.TLabel")
        elif which == "ports":
            self.page_ports.tkraise()
            self.nav_ports.configure(style="SidebarItemActive.TLabel")
            self.nav_dashboard.configure(style="Sidebar.TLabel")

       # Hilfsfunktionen

    def _decorate_ports(self, ports_str: str) -> str:
        if not ports_str or ports_str == "Keine offenen Ports":
            return ports_str

        decorated: list[str] = []

        for token in ports_str.split(","):
            token = token.strip()
            if not token:
                continue

            try:
                port_nr = int(token.split("/")[0])
            except ValueError:
                decorated.append(f"{SYM_LOW} {token}")
                continue

            if port_nr in CRITICAL_PORTS:
                decorated.append(f"{SYM_CRIT} {token}")
            elif port_nr in MID_PORTS:
                decorated.append(f"{SYM_MID} {token}")
            else:
                decorated.append(f"{SYM_LOW} {token}")

        return ", ".join(decorated) if decorated else "Keine offenen Ports"

    def _add_example_rows(self):
        rows = [
            ("192.168.10.10", "fileserver", "22/tcp, 80/tcp, 443/tcp", "Server online"),
            ("192.168.10.21", "Drucker01", "80/tcp", "Gerät erreichbar"),
            ("192.168.10.42", "Client-435", "135/tcp, 445/tcp", "Client im Netzwerk"),
        ]
        for ip, host, ports, comment in rows:
            decorated_ports = self._decorate_ports(ports)
            self.tree.insert(
                "", "end",
                values=(ip, host, decorated_ports, comment),
            )

    def _set_results(self, results: list[ScanResult]):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for r in results:
            decorated_ports = self._decorate_ports(r.open_ports)
            self.tree.insert(
                "",
                "end",
                values=(r.ip, r.hostname, decorated_ports, r.comment),
            )

    def _merge_results(
        self,
        net_results: list[ScanResult],
        port_results: list[ScanResult],
    ) -> list[ScanResult]:
        if not net_results and not port_results:
            return []
        if net_results and not port_results:
            return net_results
        if port_results and not net_results:
            return port_results

        merged: dict[str, ScanResult] = {}
        for r in net_results:
            merged[r.ip] = ScanResult(
                ip=r.ip,
                hostname=r.hostname,
                open_ports=r.open_ports,
                comment=r.comment,
            )

        for p in port_results:
            if p.ip in merged:
                m = merged[p.ip]
                if p.hostname:
                    m.hostname = p.hostname
                if p.open_ports and p.open_ports != "Keine offenen Ports":
                    m.open_ports = p.open_ports
                if "Ports gescannt" not in (m.comment or ""):
                    if m.comment:
                        m.comment += "; Ports gescannt"
                    else:
                        m.comment = "Ports gescannt"
            else:
                merged[p.ip] = ScanResult(
                    ip=p.ip,
                    hostname=p.hostname,
                    open_ports=p.open_ports,
                    comment="Nur Port-Scan",
                )

        return list(merged.values())

    # State-Updates
    def _on_scan_mode_change(self):
        self.dsg_confirm.set(False)
        self._update_scan_button_state()

    def _on_dsg_change(self):
        self._update_scan_button_state()

    def _update_scan_button_state(self):
        net = self.scan_network_var.get()
        port = self.scan_port_var.get()
        dsg_ok = self.dsg_confirm.get()

        if net and port:
            btn_text = "Benutzerdefinierten Scan starten"
            status_hint = "Netzwerk- und Port-Scan (benutzerdefiniert)."
        elif net:
            btn_text = "Netzwerkscan starten"
            status_hint = "Nur Netzwerkscan."
        elif port:
            btn_text = "Port-Scan starten"
            status_hint = "Nur Port-Scan."
        else:
            btn_text = "Scan starten"
            status_hint = "Bitte mindestens einen Scan-Typ auswählen."

        self.btn_scan.configure(text=btn_text)

        self.entry_network.configure(state="normal" if net or port else "disabled")
        self.entry_ports.configure(state="normal" if port else "disabled")

        if dsg_ok and (net or port):
            self.btn_scan.configure(state="normal")
            self.status_var.set(f"Berechtigung bestätigt – {status_hint}")
        else:
            self.btn_scan.configure(state="disabled")
            if not dsg_ok:
                self.status_var.set(
                    "Bitte bestätigen, dass der Scan gemäss DSG (SR 235.1) erfolgt und Sie berechtigt sind."
                )
            else:
                self.status_var.set(status_hint)

    # Scan-Logik (mit Hintergrund-Thread)
    def _open_progress(self, message: str):
        if self._progress_win is not None:
            try:
                self._progress_win.destroy()
            except tk.TclError:
                pass
            self._progress_win = None

        win = tk.Toplevel(self)
        win.title("Scan läuft ...")
        win.transient(self)
        win.grab_set()
        win.resizable(False, False)
        win.configure(bg=BG_APP)

        # Inhalt im ZeroTrace-Style
        frame = ttk.Frame(win, style="Card.TFrame", padding=16)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text=message, style="Card.TLabel").pack(anchor="w")
        ttk.Label(
            frame,
            text="Bitte warten – der Scan wird lokal mit Nmap ausgeführt.",
            style="Card.TLabel",
            foreground=TEXT_MUTED,
        ).pack(anchor="w", pady=(4, 10))

        pb = ttk.Progressbar(frame, mode="indeterminate", length=260)
        pb.pack(pady=(0, 5))
        pb.start(10)

        self._progress_win = win

        # X-Button (Fenster schließen) abfangen → Abbruch-Dialog
        win.protocol("WM_DELETE_WINDOW", self._on_progress_close_request)

        # mittig auf dem Bildschirm platzieren
        win.update_idletasks()
        w = win.winfo_width()
        h = win.winfo_height()
        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        win.geometry(f"{w}x{h}+{x}+{y}")

        self.update_idletasks()

    def _on_progress_close_request(self):
        """Benutzer klickt auf X im Scan-Dialog – logischer Abbruch."""
        if messagebox.askyesno(
            "Scan abbrechen",
            "Möchten Sie den laufenden Scan wirklich abbrechen?\n\n"
            "Die bereits gestartete Analyse wird im Hintergrund beendet,\n"
            "die Ergebnisse werden jedoch verworfen."
        ):
            self._scan_cancelled = True
            self._close_progress()
            self.btn_scan.configure(state="normal")
            self.btn_pdf.configure(state="normal")
            self.status_var.set("Scan abgebrochen.")

    def _close_progress(self):
        if self._progress_win is not None:
            try:
                self._progress_win.destroy()
            except tk.TclError:
                pass
            self._progress_win = None

    def _run_scan(self):
        """Startet den Scan in einem Hintergrund-Thread."""
        network = self.entry_network.get().strip()
        ports = self.entry_ports.get().strip()
        net = self.scan_network_var.get()
        port = self.scan_port_var.get()

        if not (net or port):
            messagebox.showwarning("Keine Auswahl", "Bitte Netzwerkscan, Port-Scan oder beides auswählen.")
            return

        if (net or port) and not network:
            messagebox.showwarning("Fehlende Eingabe", "Bitte ein Netzwerk oder Ziel (CIDR/IP) angeben.")
            return

        if port and not ports:
            messagebox.showwarning("Fehlende Eingabe", "Bitte einen Port-Bereich für den Port-Scan angeben.")
            return

        # neuer Scan → Abbruch-Flag zurücksetzen
        self._scan_cancelled = False

        # Buttons sperren & Popup anzeigen
        self.btn_scan.configure(state="disabled")
        self.btn_pdf.configure(state="disabled")

        if net and port:
            self.status_var.set(f"Starte benutzerdefinierten Scan (Netzwerk + Ports) für {network} ...")
            progress_msg = "Benutzerdefinierter Scan läuft (Netzwerk + Ports) ..."
        elif net:
            self.status_var.set(f"Starte Netzwerkscan für {network} ...")
            progress_msg = "Netzwerkscan läuft ..."
        else:
            self.status_var.set(f"Starte Port-Scan für {network} mit Ports {ports} ...")
            progress_msg = "Port-Scan läuft ..."

        self._open_progress(progress_msg)

        thread = threading.Thread(
            target=self._run_scan_worker,
            args=(network, ports, net, port, self.only_active_var.get()),
            daemon=True,
        )
        thread.start()

    def _run_scan_worker(self, network: str, ports: str, net: bool, port: bool, only_active: bool):
        try:
            net_results: list[ScanResult] = []
            port_results: list[ScanResult] = []

            if net:
                net_results = run_network_scan(network, only_active)
            if port:
                port_results = run_port_scan(network, ports)

            merged = self._merge_results(net_results, port_results)
            self.after(0, self._on_scan_success, merged, net, port)

        except NmapError as exc:
            self.after(0, self._on_scan_error, "Fehler beim Scan (Nmap)", str(exc))
        except Exception as exc:
            self.after(0, self._on_scan_error, "Unbekannter Fehler beim Scan", str(exc))

    def _on_scan_success(self, results: list[ScanResult], net: bool, port: bool):
        """Wird im UI-Thread aufgerufen, wenn der Scan fertig ist."""
        if self._scan_cancelled:
            # Nutzer hat abgebrochen → keine UI-Updates mehr
            return

        self._set_results(results)

        if results:
            summary = f"{len(results)} Host(s) im Ergebnis."
        else:
            summary = "Keine passenden Hosts gefunden."

        if net and port:
            title = "Benutzerdefinierter Scan abgeschlossen"
        elif net:
            title = "Netzwerkscan abgeschlossen"
        else:
            title = "Port-Scan abgeschlossen"

        msg = f"{title}.\n{summary}"
        self.status_var.set(msg)

        self._close_progress()
        self.btn_scan.configure(state="normal")
        self.btn_pdf.configure(state="normal")

        want_pdf = messagebox.askyesno(
            "Scan abgeschlossen",
            msg + "\n\nMöchten Sie jetzt einen PDF-Report speichern?"
        )
        if want_pdf:
            self._export_pdf()

    def _on_scan_error(self, title: str, error_msg: str):
        """Wird im UI-Thread aufgerufen, wenn der Scan fehlschlägt."""
        if self._scan_cancelled:
            # Wenn bereits abgebrochen wurde, Fehlermeldung unterdrücken
            return

        self._close_progress()
        self.btn_scan.configure(state="normal")
        self.btn_pdf.configure(state="normal")
        self.status_var.set(title)
        messagebox.showerror(title, error_msg)

    # PDF-Export
    def _export_pdf(self):
        items = self.tree.get_children()
        if not items:
            messagebox.showinfo("Keine Daten", "Es sind keine Scan-Ergebnisse vorhanden.")
            return

        results: list[ScanResult] = []
        for item_id in items:
            ip, host, ports, comment = self.tree.item(item_id, "values")
            results.append(
                ScanResult(
                    ip=str(ip),
                    hostname=str(host),
                    open_ports=str(ports),
                    comment=str(comment),
                )
            )

        net = self.scan_network_var.get()
        port = self.scan_port_var.get()

        if net and port:
            scan_title = "Benutzerdefinierter_Scan"
            scan_type_label = "Benutzerdefinierter Scan"
        elif net:
            scan_title = "Netzwerkscan"
            scan_type_label = "Netzwerkscan"
        else:
            scan_title = "Port-Scan"
            scan_type_label = "Port-Scan"

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        default_name = f"ZeroTrace_{scan_title}_{ts}.pdf"

        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF-Datei", "*.pdf")],
            title="PDF-Report speichern unter ...",
            initialfile=default_name,
        )
        if not file_path:
            return

        try:
            self.status_var.set("Erstelle PDF-Report ...")
            self.update_idletasks()

            from pathlib import Path
            pdf_path = export_results_to_pdf(
                results=results,
                output_path=Path(file_path),
                scan_type=scan_type_label,
                meta_network=self.entry_network.get().strip(),
                meta_ports=self.entry_ports.get().strip(),
            )

            self.status_var.set(f"PDF-Report gespeichert: {pdf_path}")
            messagebox.showinfo(
                "PDF erstellt", f"Report erfolgreich gespeichert:\n{pdf_path}"
            )

        except Exception as exc:
            self.status_var.set("Fehler beim PDF-Export.")
            messagebox.showerror("Fehler beim PDF-Export", str(exc))


if __name__ == "__main__":
    app = ZeroTraceGUI()
    app.mainloop()
