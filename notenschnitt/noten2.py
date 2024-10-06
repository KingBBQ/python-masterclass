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

print("Deine Noten sind: ")
print(noten)

