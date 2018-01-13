# Kodiranje skripta
# -*- coding: utf-8 -*-


##### Zadatak br. 6

import numpy as np

br_tacaka = input("Unesite zeljeni broj tacaka kroz koji se vrsi fitovanje polinoma proizvoljnog stepena: ")

i = 0
x = []
y = []
while i < br_tacaka:
    x.append( input("Unesite x koordinatu: "))
    y.append( input("Unesite y koordinatu: "))
    i= i+1
print "Koordinate unetih tacaka su sledece: \n" \
      "[X] i [Y] koordinate: ",x,y

stepen_polinoma = input("Unesite zeljeni stepen polinoma: ")

# koef = np.polynomial.polynomial.polyfit(x,y,stepen_polinoma) # vraca u drugom poretku koeficijente polinoma  A+Bx+Cx2...
# ffit = np.poly1d(koef)
koef1 = np.polyfit(x,y,stepen_polinoma) # koeficijenti polinoma u poretku Ax^n+Bx^n-1...
ffit1 = np.poly1d(koef1)


print "Koeficijenti ocenjenog polinoma su sledeci: \n",koef1
print "Formula polinoma sa ocenjenima koeficijentima, stepena",stepen_polinoma,"je sledeca: \n",ffit1
