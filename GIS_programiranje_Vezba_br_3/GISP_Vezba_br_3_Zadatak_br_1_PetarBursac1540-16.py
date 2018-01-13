# Kodiranje skripta
# -*- coding: utf-8 -*-

# Zadatak br. 1


import math
class Sfera():

    broj = 0

    @staticmethod
    def broj_Sfera():
        print "Broj kreiranih objekata klase Sfera je: {0:d}".format(Sfera.broj)

    def __init__(self, xCentar = 0, yCentar = 0, zCentar = 0, r = 1): # r - poluprecnik
        self.xCentar = xCentar
        self.yCentar = yCentar
        self.zCentar = zCentar
        self.r = r
        Sfera.broj += 1

    def __str__(self):
        return '({:<f}, {:<f}, {:<f}, {:<f})'.format(self.xCentar, self.yCentar,self.zCentar,self.r)

    def izracunaj_Zapreminu(self):
        return "Zapremina objekta klase Sfera je: " , ((4*(self.r ** 3)*math.pi)/3)






#s = Sfera()
#print s
#s1 = Sfera(0,0,0,3)
#print Sfera.izracunaj_Zapreminu(s1)
#Sfera.broj_Sfera()

# Написати у модулу TestSfera главни програм такав да се у њему извршава:
# Испис броја објеката који су формирани (позивом одговарајућег метода) пре него што је формиран иједан објекат;
# Креирање објеката:
# sfera – објекат у координатном почетку, полупречника 4.0;
# globus (12, 1.0, 1.0, 1.0);
# bilijarska_lopta (10.0, 10.0, 0.0);
# jedinicna_sfera – објекат у координатном почетку, полупречника 1.0;
# Испис броја објеката који су формирани;
# Испис запремине сваког претходно креираног објекта.

#from GISP_Vezba_br_3_Petar_Bursac_modul_Sfera import Sfera

# Modul testSfera

Sfera.broj_Sfera()
sfera = Sfera(0, 0, 0, 4)
globus = Sfera(12, 1, 1, 1)
bilijarska_lopta = Sfera(10, 10, 0)
jedinicna_sfera = Sfera(0, 0, 0, 1)
Sfera.broj_Sfera()

print Sfera.izracunaj_Zapreminu(sfera), "objekat: sfera;"
print Sfera.izracunaj_Zapreminu(globus), "objekat: globus;"
print Sfera.izracunaj_Zapreminu(bilijarska_lopta), "objekat: bilijarska_lopta;"
print Sfera.izracunaj_Zapreminu(jedinicna_sfera), "objekat: jedinicna_sfera;"

