# Kodiranje skripta
# -*- coding: utf-8 -*-


######## Zadatak br. 8

# Igra "Pogodi broj"
import random

slucajan_broj = random.randint(0,100)
#print slucajan_broj

ime = raw_input("Unesite korisnicko ime i zapocnite igru: ")
broj = input("Igra je zapoceta, unesite broj u intervalu [0,100]: ")
i=1
while broj != slucajan_broj:
    broj = broj
    if broj < slucajan_broj:
        broj = input("Uneli ste broj koji je MANJI od slucajno generisanog broja, unesite ponovo broj: ")
        i = i + 1
    else:
        broj = input("Uneli ste broj koji je VECI od slucajno generisanog broja, unesite ponovo broj: ")
        i = i + 1
else:
    print "Uneli ste tacan broj! \n" \
          "Korisnik",ime,"pogodio je iz",i,"pokusaja."

