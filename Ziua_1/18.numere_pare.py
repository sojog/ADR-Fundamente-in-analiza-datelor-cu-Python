"""Creaţi un program care va prelua de la utilizator 5 numere şi care la ieşire va scrie mesajul pentru fiecare dacă numărul este par sau impar."""

contor = 0
while contor < 5:
    nr = input("Introduceti un numar ")
    nr = int(nr)

    if nr % 2 == 0:
        print("Numar par")
    else:
        print("Numar impar")
    contor += 1