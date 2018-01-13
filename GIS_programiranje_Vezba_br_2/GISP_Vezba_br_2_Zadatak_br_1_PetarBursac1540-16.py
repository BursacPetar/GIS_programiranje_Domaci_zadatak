# Kodiranje skripta
# -*- coding: utf-8 -*-


# Zadatak br. 1
# niz = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# napisati program koji racuna sumu parnih elemenata niza

niz = input("Unesite niz u obliku: [x,x1,x2,...]")
suma_parnih = 0
for i in niz:
    if i % 2 == 0:
        suma_parnih = suma_parnih + i
print "Suma parnih elemenata niza je jednaka: ", suma_parnih
