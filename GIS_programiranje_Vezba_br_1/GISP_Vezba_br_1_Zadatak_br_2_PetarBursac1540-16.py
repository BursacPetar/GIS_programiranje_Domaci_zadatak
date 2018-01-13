# Kodiranje skripta
# -*- coding: utf-8 -*-


## Zadatak br. 2
# pretpostavlja se da je unos korektan
br1 = input("Unesite prvi ceo broj: ")
br2 = input("Unesite drugi ceo broj: ")
print "Uneti prvi ceo broj je: {0:d} \n" \
      "Uneti drugi ceo broj je: {1:d} \n" \
      "Zbir je jednak: {2:d} \n" \
      "Razlika je jednaka: {3:d} \n" \
      "Proizvod je jednak: {4:d} \n" \
      "Ceo deo pri deljenju prvog broja drugim brojem je jednak: {5:d} \n" \
      "Ostatak pri deljenju prvog broja drugim brojem je jednak: {6:d}" \
      "".format(br1, br2, br1+br2,br1-br2,br1*br2,br1//br2,br1%br2)
