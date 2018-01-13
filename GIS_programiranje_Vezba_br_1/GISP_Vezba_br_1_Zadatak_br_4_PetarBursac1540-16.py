# Kodiranje skripta
# -*- coding: utf-8 -*-



#### Zadatak br. 4

#   Unosenje prvog i drugog cetvorocifrenog broja
prvi_br = raw_input("Unesite PRVI cetvorocifreni broj: ")
# Ispitivanje da li je broj cetvorocifren
while len(prvi_br) != 4:
    prvi_br = raw_input("Unesite ponovo PRVI broj, ali sa tacno cetri cifre! : ")



drugi_br = raw_input("Unesite DRUGI cetvorocifreni broj: ")
# Ispitivanje da li je broj cetvorocifren
while len(drugi_br) != 4:
    drugi_br = raw_input("Unesite ponovo DRUGI broj, ali sa tacno cetri cifre! : ")


#suma1 = int(prvi_br[0]) + int(prvi_br[1]) + int(prvi_br[2]) + int(prvi_br[3])
#print "Suma cifara prvog cetvorocifrenog broja je jednaka: ", suma1

### moze i sa for
suma11 = 0
for i in prvi_br:
    suma11 = suma11 + int(i)

print "Suma cifara PRVOG cetvorocifrenog broja je jednaka: ",suma11

#suma2 = int(drugi_br[0]) + int(drugi_br[1]) + int(drugi_br[2]) + int(drugi_br[3])
#print "Suma cifara drugog cetvorocifrenog broja je jednaka: ",suma2

suma22 = 0
for ii in drugi_br:
    suma22 = suma22 + int(ii)
print "Suma cifara DRUGOG cetvorocifrenog broja je jednaka: ",suma22

zbir_parnih1 = int(prvi_br[1]) + int(prvi_br[3])
zbir_neparnih1 = int(prvi_br[0]) + int(prvi_br[2])
razlika1 = zbir_parnih1 - zbir_neparnih1
print "Razlika zbira cifara na parnim i neparnim pozicijama PRVOG broja je jednaka: ",razlika1

zbir_parnih2 = int(drugi_br[1]) + int(drugi_br[3])
zbir_neparnih2 = int(drugi_br[0]) + int(drugi_br[2])
razlika2 = zbir_parnih2 - zbir_neparnih2
print "Razlika zbira cifara na parnim i neparnim pozicijama DRUGOG broja je jednaka: ",razlika2
