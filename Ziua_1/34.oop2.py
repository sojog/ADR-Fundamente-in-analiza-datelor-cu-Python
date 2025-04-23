## Definirea clasei
class Cont:
    ## Functie speciala de initializare - functie magica
    def __init__(self, detinator):
        self.detinator = detinator
        self.suma = 0

    ## Functie speciala folosita la print - functie magica
    def __str__(self):
        return f"Contul detinut de {self.detinator} are {self.suma} lei"
    
    ## Functie normala (metoda)
    def adauga_bani(self, valoare):
        if type(valoare) == int and valoare > 0:
            self.suma += valoare
    
    ## Functie normala (metoda)
    def retrage_bani(self, valoare):
         if type(valoare) == int and valoare <= self.suma:
             self.suma -= valoare
         else:
             print("Nu aveti suficienti bani pentru retragere !!!")

## Un nou obiect de tip Cont este creat
cont  = Cont("George")
print(cont)

## Un nou obiect de tip Cont este creat
cont2 = Cont("Iulia")
print(cont2)

# cont.suma -= 100
cont.adauga_bani(100)
print(cont)

cont.retrage_bani(50)
print(cont)


cont.retrage_bani(150)
print(cont)

cont2.adauga_bani(100)
print(cont2)