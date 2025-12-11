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


class ZeroTraceGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Basis-Fenster
        self.title("Zero Trace – Lokaler Sicherheits-Scanner (MVP)")
        self.geometry("1100x650")
        self.minsize(980, 580)
        self.configure(bg=BG_APP)

        self._progress_win: tk.Toplevel | None = None

        self._init_style()
        self._build_layout()

    # --------------------------------------------------
    # Styling
    # --------------------------------------------------
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

    # --------------------------------------------------
    # Layout
    # --------------------------------------------------
    def _build_layout(self):
        root_frame = ttk.Frame(self, style="TFrame")
        root_frame.pack(fill="both", expand=True)
        root_frame.columnconfigure(0, weight=0)  # Sidebar
        root_frame.columnconfigure(1, weight=1)  # Main
        root_frame.rowconfigure(1, weight=1)

        # ---------- Sidebar ----------
        sidebar = tk.Frame(root_frame, bg=BG_SIDEBAR, width=210)
        sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew")
        sidebar.grid_propagate(False)

        ttk.Label(sidebar, text="Zero Trace", style="SidebarTitle.TLabel").pack(
            anchor="w", padx=20, pady=(18, 10)
        )

        frame_dash = tk.Frame(sidebar, bg=BG_SIDEBAR)
        frame_dash.pack(fill="x", pady=2)
        tk.Frame(frame_dash, bg=ACCENT, width=3, height=24).pack(side="left")
        ttk.Label(
            frame_dash, text="Dashboard", style="SidebarItemActive.TLabel"
        ).pack(side="left", padx=14, pady=4)

        # ---------- Header ----------
        header = tk.Frame(root_frame, bg=BG_HEADER, height=64)
        header.grid(row=0, column=1, sticky="nsew")
        header.grid_propagate(False)

        header_inner = ttk.Frame(header, style="TFrame")
        header_inner.pack(fill="both", expand=True, padx=20, pady=10)
        header_inner.columnconfigure(0, weight=1)
        header_inner.columnconfigure(1, weight=0)

        title_frame = ttk.Frame(header_inner, style="TFrame")
        title_frame.grid(row=0, column=0, sticky="w")
        ttk.Label(
            title_frame,
            text="Zero Trace – Lokale Sicherheitsanalyse",
            style="HeaderTitle.TLabel",
        ).pack(anchor="w")
        ttk.Label(
            title_frame,
            text="Führe lokale Port- und Netzwerkscans aus, ohne Daten an die Cloud zu senden.",
            style="HeaderSub.TLabel",
        ).pack(anchor="w", pady=(2, 0))

        badge = ttk.Label(
            header_inner,
            text="MVP – Local Only",
            style="HeaderSub.TLabel",
            padding=(10, 4),
        )
        badge.configure(
            background=ACCENT_SOFT,
            foreground=ACCENT,
        )
        badge.grid(row=0, column=1, sticky="e")

        # ---------- Main-Bereich ----------
        main_frame = ttk.Frame(root_frame, style="TFrame", padding=16)
        main_frame.grid(row=1, column=1, sticky="nsew")
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # ---- Konfiguration (links) ----
        config = ttk.LabelFrame(
            main_frame, text="Scan-Konfiguration", style="Card.TLabelframe", padding=12
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

        # Scan-Modi (beide links untereinander)
        self.scan_network_var = tk.BooleanVar(value=True)
        self.scan_port_var = tk.BooleanVar(value=False)

        ttk.Checkbutton(
            config,
            text="Netzwerkscan",
            variable=self.scan_network_var,
            command=self._update_scan_button_state,
        ).grid(row=3, column=0, columnspan=2, sticky="w", pady=(2, 2))

        ttk.Checkbutton(
            config,
            text="Port-Scan",
            variable=self.scan_port_var,
            command=self._update_scan_button_state,
        ).grid(row=4, column=0, columnspan=2, sticky="w", pady=(2, 2))

        # Hinweistext links
        ttk.Label(
            config,
            text="Hinweis: Zero Trace führt alle Analysen ausschliesslich lokal aus.\n"
                 "Es werden keine Scan-Daten an eine Cloud gesendet.",
            style="Card.TLabel",
            foreground=TEXT_MUTED,
        ).grid(row=5, column=0, sticky="w", pady=(4, 4))

        # DSG-Checkbox rechts (über PDF-Button)
        self.dsg_confirm = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            config,
            text="Scan gemäss DSG (SR 235.1) und Berechtigung bestätigt",
            variable=self.dsg_confirm,
            command=self._update_scan_button_state,
        ).grid(row=5, column=1, sticky="e", pady=(4, 4))

        # Button-Leiste
        btn_frame = ttk.Frame(config)
        btn_frame.grid(row=6, column=0, columnspan=2, sticky="we", pady=(8, 0))
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)

        self.btn_scan = ttk.Button(
            btn_frame,
            text="Netzwerkscan starten",
            style="Primary.TButton",
            command=self._run_scan,
            state="disabled",
        )
        self.btn_scan.grid(row=0, column=0, sticky="we", padx=(0, 5))

        self.btn_pdf = ttk.Button(
            btn_frame,
            text="PDF-Report erstellen",
            style="Secondary.TButton",
            command=self._export_pdf,
        )
        self.btn_pdf.grid(row=0, column=1, sticky="we", padx=(5, 0))

        # ---- Scan-Ergebnisse ----
        results = ttk.LabelFrame(
            main_frame, text="Scan-Ergebnisse", style="Card.TLabelframe", padding=8
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
        self.tree.column("ports", width=200, anchor="w")
        self.tree.column("comment", width=260, anchor="w")

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

        self._update_scan_button_state()

    # --------------------------------------------------
    # Hilfsfunktionen
    # --------------------------------------------------
    def _add_example_rows(self):
        rows = [
            ("192.168.10.10", "fileserver", "22, 80, 443", "Server online"),
            ("192.168.10.21", "drucker01", "80", "Gerät erreichbar"),
            ("192.168.10.42", "client42", "135, 445", "Client im Netzwerk"),
        ]
        for row in rows:
            self.tree.insert("", "end", values=row)

    def _set_results(self, results: list[ScanResult]):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for r in results:
            self.tree.insert("", "end", values=(r.ip, r.hostname, r.open_ports, r.comment))

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
                    "Bitte bestätigen, dass der Scan gemäss DSG (SR 235.1) erfolgt und du berechtigt bist."
                )
            else:
                self.status_var.set(status_hint)

    # --------------------------------------------------
    # Scan-Logik
    # --------------------------------------------------
    def _open_progress(self, message: str):
        """Kleines Popup, das zeigt, dass der Scan läuft."""
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

        ttk.Label(win, text=message, padding=(20, 15)).pack()
        ttk.Label(
            win,
            text="Bitte warten – der Scan wird lokal mit Nmap ausgeführt.",
            style="Card.TLabel",
        ).pack(padx=20, pady=(0, 10))

        # Einfacher Progress-Balken (optisch, ohne echten Fortschritt)
        pb = ttk.Progressbar(win, mode="indeterminate", length=260)
        pb.pack(padx=20, pady=(0, 15))
        pb.start(10)

        self._progress_win = win
        self.update_idletasks()

    def _close_progress(self):
        if self._progress_win is not None:
            try:
                self._progress_win.destroy()
            except tk.TclError:
                pass
            self._progress_win = None

    def _run_scan(self):
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

        try:
            net_results: list[ScanResult] = []
            port_results: list[ScanResult] = []

            if net:
                net_results = run_network_scan(network, only_up=self.only_active_var.get())
            if port:
                port_results = run_port_scan(network, ports)

            merged = self._merge_results(net_results, port_results)
            self._set_results(merged)

            if merged:
                summary = f"{len(merged)} Host(s) im Ergebnis."
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
            messagebox.showinfo("Scan abgeschlossen", msg)

        except NmapError as exc:
            self.status_var.set("Fehler beim Scan (Nmap).")
            messagebox.showerror("Fehler beim Scan (Nmap)", str(exc))

        except Exception as exc:
            self.status_var.set("Unbekannter Fehler beim Scan.")
            messagebox.showerror("Fehler beim Scan", str(exc))

        finally:
            self._close_progress()
            self.btn_scan.configure(state="normal")
            self.btn_pdf.configure(state="normal")

    # --------------------------------------------------
    # PDF-Export
    # --------------------------------------------------
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
        default_name = f"{scan_title}_{ts}.pdf"

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
                scan_type=scan_type_label,  # wird im PDF als Text angezeigt
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
