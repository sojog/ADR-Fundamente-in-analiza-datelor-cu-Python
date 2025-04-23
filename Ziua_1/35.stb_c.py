
class STBCard:
    def __init__(self, nume_detinator="Nenominal", calatorii_disponibile=0, credit_disponibil=0):
        self.nume_detinator = nume_detinator
        self.calatorii_disponibile = calatorii_disponibile
        self.credit_disponibil = credit_disponibil
        self.valoare_calatorie = 3 # Valoarea unei călătorii validate cu credit

    def __str__(self):
        return f"{self.nume_detinator} {self.calatorii_disponibile} calatorii {self.credit_disponibil} lei"
    def valideaza_calatorie(self):
        if self.calatorii_disponibile > 0:
            self.calatorii_disponibile -= 1
            print("Călătorie validată. Călătorii disponibile:", self.calatorii_disponibile)
        else:
            print("Nu aveți călătorii disponibile.")

    def valideaza_credit(self):
        if self.credit_disponibil >= self.valoare_calatorie:
            self.credit_disponibil -= self.valoare_calatorie
            print("Călătorie validată cu credit. Credit disponibil:", self.credit_disponibil)
        else:
            print("Credit insuficient pentru validarea călătoriei.")

    def reincarca_credit(self, suma):
        self.credit_disponibil += suma
        print("Credit reîncărcat. Credit disponibil:", self.credit_disponibil)

    def reincarca_calatorii(self, numar_calatorii):
        self.calatorii_disponibile += numar_calatorii
        print("Călătorii reîncărcate. Călătorii disponibile:", self.calatorii_disponibile)

# Exemplu de utilizare
card = STBCard("Ion Popescu", 5, 10)
card.valideaza_calatorie()
card.valideaza_credit()
card.reincarca_credit(20)
card.reincarca_calatorii(3)
print(card)
