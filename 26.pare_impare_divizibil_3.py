"""Creaţi un program care va prelua de la utilizator 5 numere şi care la ieşire va scrie mesajul pentru fiecare dacă numărul este par, impar și/sau divizibil cu 3. Adăugați-le în trei liste (pare, impare, divizibile cu 3). Comparați lungimea celor 3 liste."""

pare = []
impare = []
divizibile_cu_3 = []


for i in range(5):
    nr = input("Introduceti numarul \n")
    nr = int(nr)
    
    if nr % 2 == 0:
        pare.append(nr)
    else:
        impare.append(nr)
    
    if nr % 3 == 0:
        divizibile_cu_3.append(nr)

print("Numere pare", pare)
print("Numere impare", impare)
print("Numere divizibile cu 3", divizibile_cu_3)

print(len(pare), len(impare), len(divizibile_cu_3))

lungime_maxima = max(len(pare), len(impare), len(divizibile_cu_3))
print("Lungimea maxima:", lungime_maxima)

for i in [pare, impare, divizibile_cu_3]:
    if len(i) == lungime_maxima:
        print("Lista cu lungime maxima este:", i)

