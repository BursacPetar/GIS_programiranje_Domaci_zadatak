# Kodiranje skripta
# -*- coding: utf-8 -*-

## Zadatak br. 2


import math
class Tacka:

    # definisanje konstruktora
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def pomeraj_Tacke(self, x_pomeraj, y_pomeraj):
        self.x = self.x + x_pomeraj
        self.y = self.y + y_pomeraj

    # ispisvanje koordinata tacaka
    def koordinate(self):
        print ('({:<f}, {:<f})'.format(self.x, self.y))

    # metod za racunanje rastojanja do zadate tacke
    def rastojanje_do(self, t):
        dx = self.x - t.x
        dy = self.y - t.y
        return math.sqrt(dx ** 2 + dy ** 2)

    #
    def __str__(self):
         return 'Koordinate: ({:<f}, {:<f})'.format(self.x, self.y)

    def daj_x_Koordinatu(self):
        return self.x

    def daj_y_Koordinatu(self):
        return self.y
# test
# t1 = Tacka(1,1)
# t1.pomeraj_Tacke(0.5,0.5)
# t1.koordinate()
# print t1
# print t1.rastojanje_do(Tacka(2,2))

class Duz:

    def __init__(self, t1, t2):
        self.t1 = Tacka(t1.daj_x_Koordinatu(), t1.daj_y_Koordinatu())
        self.t2 = Tacka(t2.daj_x_Koordinatu(), t2.daj_y_Koordinatu())

    def __str__(self):
        return "Objekat klase Duz, se sastoji iz tacaka: \n" \
               "t1: {}\n" \
               "t2: {}".format(str(self.t1),str(self.t2))

    def kreiranje_duzi_na_osnovu_Koordinata(self, x1, y1, x2, y2):
        self.t1 = Tacka(x1, y1)
        self.t2 = Tacka(x2, y2)

    def racunanje_Duzine(self):
        print "Duzina duzi je jednaka: ", self.t1.rastojanje_do(self.t2)

# test
# t1 = Tacka(1,1)
# t2 = Tacka(2,2)
# d1 = Duz(t1,t2)
# print d1
# d1.racunanje_Duzine()
# d1.kreiranje_duzi_na_osnovu_Koordinata(1, 16, 3, 3)
# print d1
# d1.racunanje_Duzine()

# Modul TestGeometrija

x_poc = input("Unesite x koordinatu pocetne tacke: ")
y_poc = input("Unesite y koordinatu pocetne tacke: ")
x_zav = input("Unesite x koordinatu krajnje tacke: ")
y_zav = input("Unesite y koordinatu krajnje tacke: ")

t1 = Tacka(x_poc,y_poc)
t2 = Tacka(x_zav,y_zav)

duz1 = Duz(t1, t2)
print duz1
print duz1.racunanje_Duzine()

x_pom = input("Unesite vrednost pomeraja krajnje tacke po x koordinati: ")
y_pom = input("Unesite vrednost pomeraja krajnje tacke po y koordinati: ")

t3_pom = Tacka((x_zav + x_pom),(y_zav + y_pom))

duz_pomerena = Duz(t1, t3_pom)
print "Duz pomerena po krajnjoj tacki je: \n",duz_pomerena
duz_pomerena.racunanje_Duzine()

x11,y11,x22,y22 = input("Unesite koordinate pocetne i krajnje tacke za kreiranje druge duzi: ")
t3 = Tacka(0, 0)
t4 = Tacka(0, 0)
duz_s = Duz(t3, t4)
duz_s.kreiranje_duzi_na_osnovu_Koordinata(x11,y11,x22,y22)
print duz_s
duz_s.racunanje_Duzine()



