"""Creaţi un program care va prelua de la utilizator 5 numere diferite intre ele şi care la ieşire va scrie mesajul pentru fiecare dacă numărul este par sau impar."""

nr_introduse = []

while len(nr_introduse) < 5:
    nr = input("Introduceti un numar ")
    nr = int(nr)

    if nr not in nr_introduse:
        nr_introduse.append(nr)

    print("Nr introduse:", nr_introduse)

    if nr % 2 == 0:
        print("Numar par")
    else:
        print("Numar impar")