# Kodiranje skripta
# -*- coding: utf-8 -*-


#### Zadatak br. 4

n1 = input("Unesite prvi niz u obliku: [x,x1,x2,...]")
n2 = input("Unesite drugi niz u obliku: [x,x1,x2,...]")
n3 = []
opcija = raw_input("Unesite nacin kreiranja niza:\n "
                   "[el11,el12] - opcija -p \n"
                   " [el12,el11] - opcija -d")

from itertools import chain

if opcija == "-p":
    n3 = list(chain(*zip(n1,n2)))
elif opcija == "-d":
    n3 = list(chain(*zip(n2, n1)))
else:
    pass

print "Elementi novo kreiranog niza, od uneta dva niza su sledeci: \n",n3
