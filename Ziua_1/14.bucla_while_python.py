
while True:
    nr = input("Introdu un numar ")
    if nr.isdigit():
        print("Numarul cu TVA", int(nr) * 1.19)
    elif nr == "":
        break
    



