# Kodiranje skripta
# -*- coding: utf-8 -*-


### Zadatak br. 3
import math
# Unosenje dva pravca u obliku stepeni:minuti:sekunde
pravac_levi = raw_input("Unesite levi pravac u obliku stepeni:minuti:sekunde").split(':')
pravac_desni = raw_input("Unesite desni pravac u obliku stepeni:minuti:sekunde").split(':')
# split funkcija kojom se razdvaja unos na ulazu

#print pravac_levi, pravac_desni

#type(pravac_levi)
#type(pravac_desni)
###################################################################################################
# potrebno da se izvrsi konverzija svakog clana liste u float iz str
### konverzija u float iz razloga int/int je isto int (ceo broj) ili da se izvrsi konverzija u int a da se deli sa float npr 60.0 i 3600.0
stepeni1, minuti1, sekunde1 = float(pravac_levi[0]), float(pravac_levi[1]), float(pravac_levi[2])

# ispitivanje da li je pravac veci od 0 i manji od 360
# sa if, nastaje problem sa ponvnim unosom koji opet moze biti pogresan

#if stepeni1 < 0.0:
#   stepeni1 = raw_input("Unesite ponovo stepene za prvi pravac, koji su veci od nule: ")
#    stepeni1 = float(stepeni1)
#elif stepeni1 > 360.0:
#    stepeni1 = raw_input("Unesite ponovo stepene za prvi pravac, koji su manji od 360: ")
#    stepeni1 = float(stepeni1)

# ispitivanje sa while petljom (opet nastaje problem jer ispituje samo jednom, drugi put je vec opet moguce pogresno uneti???)
while 0.0 <= stepeni1 < 360.0:
    break
else:
    stepeni1 = raw_input("Unesite ponovo stepene za prvi pravac: ")
    stepeni1 = float(stepeni1)

while 0.0 <= minuti1 < 60.0:
    break
else:
    minuti1 = raw_input("Unesite ponovo minute za prvi pravac: ")
    minuti1 = float(minuti1)

while 0.0 <= sekunde1 < 60.0:
    break
else:
    sekunde1 = raw_input("Unesite ponovo sekunde za prvi pravac: ")
    sekunde1 = float(sekunde1)

#print stepeni1,minuti1, sekunde1
#type(stepeni1) # provera
###################################################################################################
stepeni2, minuti2, sekunde2 = float(pravac_desni[0]), float(pravac_desni[1]), float(pravac_desni[2])

while 0.0 <= stepeni2 < 360.0:
    break
else:
    stepeni2 = raw_input("Unesite ponovo stepene za drugi pravac: ")
    stepeni2 = float(stepeni2)

while 0.0 <= minuti2 < 60.0:
    break
else:
    minuti2 = raw_input("Unesite ponovo minute za drugi pravac: ")
    minuti2 = float(minuti2)

while 0.0 <= sekunde2 < 60.0:
    break
else:
    sekunde2 = raw_input("Unesite ponovo sekunde za drugi pravac: ")
    sekunde2 = float(sekunde2)
###################################################################################################
# pravci u decimalnom zapisu
dec1 = stepeni1 + (minuti1/60) + (sekunde1/3600)
dec2 = stepeni2 + (minuti2/60) + (sekunde2/3600)
#print dec1
print "Prvi pravac u decimalnom zapisu: {0:f}\n" \
      "Drugi pravac u decimalnom zapisu: {1:f}".format(round(dec1,4), round(dec2,4))

ugao = dec2 - dec1
#print ugao
if ugao > 0:
    print "Ugao je jednak: {0:f}".format(round(ugao,4))
elif ugao < 0:
    ugao = ugao + 360
    print "Ugao je jednak: {0:f}".format(round(ugao,4))