class Money:
    def __init__(self,dollars=0,cents=0):
        self.dollars=dollars
        self.cents=cents
    def __repr__(self):
        return self.dollar_cent
    def __add__(self, other):
        cent = other.cents / 100
        self.dollar_cent = self.dollars + cent
        self.euro = float(self.dollar_cent) * 0.91
        self.inr = float(self.dollar_cent) * 70.89
        self.yen = float(self.dollar_cent) * 107.69
        return self.dollar_cent
    def getEuro(self):
        return self.euro
    def getInr(self):
        return self.inr
    def getYen(self):
        return self.yen
money1=Money(dollars=25)
money2=Money(cents=55)
money3=money1+money2
print('$'+money3.__repr__())
print("Dollars to Euro : ",money1.getEuro())
print("Dollars to Yen : ",money1.getYen())
print("Dollars to Inr : ",money1.getInr())
