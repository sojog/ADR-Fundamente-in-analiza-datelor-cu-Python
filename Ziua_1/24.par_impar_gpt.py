# Inițializăm o listă pentru a stoca cele 5 numere
numere = []

print("Introduceți 5 numere diferite între ele:")

while len(numere) < 5:
    try:
        numar = int(input(f"Numărul {len(numere) + 1}: "))
        if numar in numere:
            print("Numărul a fost deja introdus. Vă rugăm să introduceți un număr diferit.")
        else:
            numere.append(numar)
    except ValueError:
        print("Vă rugăm să introduceți un număr întreg valid.")

print("\nRezultate:")
for numar in numere:
    if numar % 2 == 0:
        print(f"{numar} este număr PAR.")
    else:
        print(f"{numar} este număr IMPAR.")
