# Schritt 2: Noten eingeben
noten = []
gewichtung = []

while True:
    note = input("Bitte geben Sie eine Note ein (oder 'q' zum Beenden): ")
    if note.lower() == 'q':
        break
    try:
        schulaufgabe = input("war das eine schulaufgabe? (j/n)")
        if schulaufgabe == "j":
            gewichtung.append(2)
        else:
            gewichtung.append(1)

        note = float(note)
        noten.append(note)
    except:
        print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")



print("Deine Noten sind: ")
print(noten)

durchschnitt = sum(noten) / len(noten)
print(f"Dein Notenschnitt ist: {durchschnitt:.2f}")
