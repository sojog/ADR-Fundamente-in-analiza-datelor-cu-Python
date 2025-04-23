# Pasul 1: verificarea vârstei și a genului
def verifica_acces(varsta, gen):
    if gen not in ("M", "F"):
        return "Acces interzis"
    if varsta > 70:
        return "Acces interzis"
    elif gen == "M" and varsta < 18:
        return "Acces interzis"
    elif gen == "F" and varsta < 16:
        return "Acces interzis"
    else:
        return "Acces permis"

while True:
    # Preluarea vârstei și a genului de la utilizator
    varsta = int(input("Introdu vârsta ta: "))
    gen = input("Introdu genul tău (M/F): ").upper()

    # Pasul 2: Valideaza acces
    mesaj = verifica_acces(varsta, gen)
    print(mesaj)

    # Pasul 3: Reia verificarea pentru persoana urmatoare
    continua = input("Vrei să verifici o altă persoană? (da/nu): ").lower()
    if continua != "da":
        break