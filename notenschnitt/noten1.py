noten = []

while True:
    note = input("gib deine note ein du knecht!")
    if note == "q":
        break
    note = float(note)
    noten.append(note)
print("Deine Noten sind: ")
print(noten)
