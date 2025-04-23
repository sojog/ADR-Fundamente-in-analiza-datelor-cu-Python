
# citire legacy
filereader = open("Ziua_2/1.exemplu.txt", "r")
continut = filereader.read()
filereader.close()
print(continut)


# citire nou
with open("Ziua_2/1.exemplu.txt", "r") as filereader:
    continut = filereader.read()
    print(continut)

with open("Ziua_2/1.exemplu.txt", "r") as filereader:
    linii_fisier = filereader.readlines()
    print(linii_fisier)
