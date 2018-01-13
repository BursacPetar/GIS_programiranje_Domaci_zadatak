# Kodiranje skripta
# -*- coding: utf-8 -*-

### Zadatak br. 3

# Klasa Tacka
import random
import math

class Tacka:
    def __init__(self, *atributi):
        self.br_tacke = random.randint(0,100)
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)
        self.z = random.randint(0,100)

    def __str__(self):
        return 'Broj tacke: {} \n x: {} \n y: {} \n z: {}'.format(self.br_tacke, self.x, self.y, self.z)

    def daj_x(self):
        return self.x

    def daj_y(self):
        return self.y

    def daj_z(self):
        return self.z

    def rastojanje(self, t):
        dx = self.x - t.x
        dy = self.y - t.y
        return math.sqrt(dx*dx+dy*dy)



class Povrs(Tacka):
    def __init__(self, skup_tacaka = [], *atributi):
        Tacka.__init__(self, *atributi)
        self.ko = input('Unesite ko analizira povrs:')
        self.boj_tacaka = input('Unesite broj tacaka povrsi')
        self.skup_tacaka = skup_tacaka

    def dodaj_tacke(self):
        i = 0
        while i < self.boj_tacaka:
            self.skup_tacaka.append(Tacka())
            i += 1
        return self.skup_tacaka

    def print_tacke(self):
        for i in self.skup_tacaka:
            print i


    def sr_vrednost(self):
        sum_z = 0
        for t in self.skup_tacaka:
            if isinstance(t, Tacka):
                sum_z += t.daj_z()
        return sum_z/float(len(self.skup_tacaka))

    def min_obuhvatni_pravougaonik(self):
        min_x = 101
        min_y = 101
        max_x = 0
        max_y = 0
        for m in self.skup_tacaka:
            if isinstance(m, Tacka):
                x = m.daj_x()
                if x < min_x:
                    min_x = x
                if x > max_x:
                    max_x = x
                y = m.daj_y()
                if y < min_y:
                    min_y = y
                if y > max_y:
                    max_y = y

        print " Min x: {0:d} " \
               "\n Min y: {1:d} " \
               "\n Minimalni obuhvatni pravougaonik: " \
               "\n Donje levo teme: ({2:d}, {3:d}) " \
               "\n Donje desno teme: ({4:d}, {5:d}) " \
               "\n Gornje levo teme: ({6:d}, {7:d}) " \
               "\n Gornje desno teme: ({8:d}, {9:d})".format(min_x, min_y, min_x, min_y, max_x, min_y, min_x, max_y, max_x, max_y)

    def najbliza_tacka(self, t):
        najbliza = 100000
        tac = Tacka
        if isinstance(t, Tacka):
            for i in self.skup_tacaka:
                if isinstance(i, Tacka):
                    if t.rastojanje(i) < najbliza:
                        najbliza = t.rastojanje(i)
                        tac = i
        return tac.br_tacke

    def interpolacija(self, t1, t2):
        if isinstance(t1, Tacka):
            if isinstance(t2, Tacka):
                dt1t2 = t1.rastojanje(t2)
                dz12 = t1.z - t2.z
                print 'd12 = ', dt1t2
                print 'dz12 = ', dz12
                dd = input('Unesite vrednost izmedju 0 i d12, kako bi ste dobili vrednost visine na tom rastojanju')
                z1a = (dd*dz12)/dt1t2
                if t2.z > t1.z:
                    z1aa = z1a + t1.z
                else:
                    z1aa = t2.z + z1a
                print 'Vrednost visine na rastojanju koje ste uneli iznosi:', z1aa

# Glavni program

p = Povrs()
p.dodaj_tacke()
p.print_tacke()
p.sr_vrednost()
p.min_obuhvatni_pravougaonik()

t = Tacka()
print t
p.najbliza_tacka(t)

t1 = Tacka()
print t1
t2 = Tacka()
print t2
p.interpolacija(t1, t2)

