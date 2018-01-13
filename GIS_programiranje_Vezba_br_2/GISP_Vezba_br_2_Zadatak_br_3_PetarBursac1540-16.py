# Kodiranje skripta
# -*- coding: utf-8 -*-


### Zadatak br. 3

# niz2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# napisati program koji racuna proizvod elemenata niza
niz2 = input("Unesite niz u obliku: [x,x1,x2,...]: ")
suma_pr = niz2[0]
for i in niz2[1:len(niz2)]:
    suma_pr = suma_pr * i
print "Proizvod elemenata niza je jednak: ", suma_pr