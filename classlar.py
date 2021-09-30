class nuqta:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

        #bu metod nuqtadan (x, y) nuqtagacha bo'lgan masofani hisoblaydi
    def gacha_masofa(self, x, y): 
        a=((self.x - x)**2+(self.y - y)**2)**(1/2)         
        return a

class planeta:
    def __init__(self, x, y, r) -> None:
        self.markaz = nuqta(x, y)
        self.r = r

        #bu metod nuqta planeta ichida yoki ichida emasligini qaytaradi
    def ni_ichidami(self, nuqtacha:nuqta):  
        return self.markaz.gacha_masofa(nuqtacha.x, nuqtacha.y)<self.r

class shahzoda:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.start = nuqta(x1, y1)
        self.end = nuqta(x2, y2)

        #bu metod shahzoda kesi o'tish o'tmasligini qaytaradi
    def kesib_otadimi(self, nuqtacha:planeta):
        if nuqtacha.ni_ichidami(self.start)==True and nuqtacha.ni_ichidami(self.end)==False:
            a=True
        elif nuqtacha.ni_ichidami(self.start)==False and nuqtacha.ni_ichidami(self.end)==True:
            a=True
        else:
            a=False
        return a


