# TMS Fakten-Lernen Simulation

Ein interaktives Kommandozeilen-Tool zur Simulation des Untertests **"Fakten lernen"** im TMS (Test für Medizinische Studiengänge). Dieses Skript hilft, die notwendigen Mnemotechniken unter realistischen Zeit- und Strukturvorgaben zu trainieren.

> **Hinweis:** Dieses Tool ist ein privates Projekt und steht in keiner offiziellen Verbindung zu den Testentwicklern des TMS.

## 📌 Über das Projekt

Der Untertest "Fakten lernen" ist eine der größten Herausforderungen im TMS, da er eine hohe Konzentrationsspanne und präzises Abspeichern von Informationen erfordert. Dieses Programm automatisiert die Erstellung von Übungsmaterialien.

### Kernfunktionen:

* **Dynamische Generierung:** Erstellt jedes Mal neue, zufällige Patientenprofile.
* **TMS-Konforme Struktur:** 5 Altersgruppen mit jeweils 3 Patienten, wie im TMS.
* **Realistische Variablen:** Zufällige Kombinationen aus Namen, Berufen, Eigenschaften und medizinischen Diagnosen. Automatisierte Ähnlichkeit bei Namen und Berufen, wie beim TMS, zur Steigerung des Schwierigkeitsgrads.
* **Simulierte Reproduktionsphase:** Erstellung von 20 Single-Choice-Fragen (1 aus 5) nach dem offiziellen Schema.

---

## 🚀 Installation & Start

**Repository klonen:**

```bash
git clone https://github.com/LuisHoentsch/tms-fakten-lernen-simulation.git
cd tms-fakten-lernen-simulation

```

**Skript ausführen:**

```bash
python main.py

```

---

## 📖 Ablauf der Simulation

1. **Einprägephase (6 Min):** Das Programm zeigt 15 Patientensteckbriefe. Versuche, dir die Verknüpfungen (z.B. "Der 40-jährige Architekt mit Asthma in der Notaufnahme") einzuprägen.
2. **Ablenkungsphase:** Das Programm pausiert, um die im TMS übliche 60-minütige Lücke zu simulieren.
3. **Reproduktionsphase (7 Min):** Du wirst mit 20 zufällig generierten Fragen konfrontiert.
4. **Auswertung:** Lass Dir die korrekten Lösungen anzeigen, um Deinen Fortschritt zu messen.

---

## 📂 Dateistruktur

* **main.py:** Interkation / Programmablauf.
* **data_generator.py:** Logik zur Erstellung der Patienten (Namen-Pools, Berufe, Diagnosen).
* **questions.py:** Algorithmus zur Generierung von Fragen und validen Distraktoren (falsche Antwortmöglichkeiten).

---

## 🤝 Mitwirken

Beiträge zur Erweiterung des Namenspools, zur automatischen Auswertung der Reproduktionsphase oder zur Implementierung einer grafischen Benutzeroberfläche sind herzlich willkommen!
