
class CardSTB:
    def __init__(self, detinator = "Nenominal", calatorii = 0 , credit = 0):
        self.detinator = detinator
        self.calatorii = calatorii
        self.credit = credit

    def __str__(self):
        return f"{self.detinator} are {self.calatorii} calatorii si {self.credit} credit"

    def valideaza(self):
        if self.calatorii > 0:
            self.calatorii -= 1
        elif self.credit > 3:
            self.credit -= 3
        else:
            print("Credit insuficient")

    def incarca(self, credit=3, calatorii=0):
        if type(credit) == int and credit >= 3:
            self.credit += credit
        elif type(calatorii) == int and calatorii > 1:
            self.calatorii += calatorii


card1 = CardSTB()
print(card1)

card2 = CardSTB("George", 10, 3)
print(card2)

card1.incarca()
print(card1)

card1.incarca(calatorii=10, credit=0)
print(card1)


for i in range(12):
    card1.valideaza()
    print(card1)