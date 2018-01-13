# Kodiranje skripta
# -*- coding: utf-8 -*-


###### Zadatak br. 6

pet_karaktera = raw_input("Unesite pet karaktera u obliku xxxxx: ")
while len(pet_karaktera) != 5:
    pet_karaktera = raw_input("Unesite ponovo, ali sa tacno pet karaktera! : ")

lista_cifara = [s for s in pet_karaktera if s.isdigit()]

#print pet_karaktera
#print lista_cifara
print "Ukupan broj pojavljivanja cifara je: ", len(lista_cifara)