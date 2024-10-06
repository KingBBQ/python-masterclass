

### Schritt 1: Python-Skript erstellen
Erstelle eine neue Datei in deinem Arbeitsverzeichnis und nenne sie `durchschnittsnote.py`.

### Schritt 2: Noten eingeben
Wir beginnen damit, den Benutzer nach Noten zu fragen. Wir verwenden eine Schleife, um mehrere Noten einzugeben, bis der Benutzer entscheidet, keine weiteren Noten mehr einzugeben.

```python
# Schritt 2: Noten eingeben
noten = []

while True:
    note = input("Bitte geben Sie eine Note ein (oder 'q' zum Beenden): ")
    if note.lower() == 'q':
        break
    try:
        note = float(note)
        noten.append(note)
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
```

### Erklärung:
- Wir initialisieren eine leere Liste `noten`, um die eingegebenen Noten zu speichern.
- Eine `while`-Schleife fragt den Benutzer wiederholt nach einer Note.
- Wenn der Benutzer 'q' eingibt, wird die Schleife beendet.
- Wir versuchen, die Eingabe in eine Gleitkommazahl (`float`) umzuwandeln und zur Liste hinzuzufügen.
- Wenn die Eingabe keine Zahl ist, wird eine Fehlermeldung ausgegeben.

### Schritt 3: Durchschnittsnote berechnen
Nachdem alle Noten eingegeben wurden, berechnen wir den Durchschnitt.

```python
# Schritt 3: Durchschnittsnote berechnen
if noten:
    durchschnitt = sum(noten) / len(noten)
    print(f"Die Durchschnittsnote ist: {durchschnitt:.2f}")
else:
    print("Keine Noten eingegeben.")
```

### Erklärung:
- Wir prüfen, ob die Liste `noten` nicht leer ist.
- Wenn sie nicht leer ist, berechnen wir den Durchschnitt, indem wir die Summe der Noten durch die Anzahl der Noten teilen.
- Das Ergebnis wird mit zwei Dezimalstellen ausgegeben.
- Wenn keine Noten eingegeben wurden, wird eine entsprechende Nachricht ausgegeben.

### Gesamtes Skript
Hier ist das vollständige Skript:

```python
# Python

noten = []

while True:
    note = input("Bitte geben Sie eine Note ein (oder 'q' zum Beenden): ")
    if note.lower() == 'q':
        break
    try:
        note = float(note)
        noten.append(note)
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

if noten:
    durchschnitt = sum(noten) / len(noten)
    print(f"Die Durchschnittsnote ist: {durchschnitt:.2f}")
else:
    print("Keine Noten eingegeben.")
```

### Ausführen des Skripts
Speichere die Datei und führe sie im Terminal aus:

```bash
python3 durchschnittsnote.py
```

Das Skript wird dich nach Noten fragen und am Ende die Durchschnittsnote berechnen und ausgeben.