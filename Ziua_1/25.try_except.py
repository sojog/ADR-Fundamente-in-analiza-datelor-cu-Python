

while True:
    x = input("Introdu de la tastatura\n")
    try:
        x = int(x)
        print("Ai introdus o valoarea corecta!")
    except:
        print("X nu este intreg")

