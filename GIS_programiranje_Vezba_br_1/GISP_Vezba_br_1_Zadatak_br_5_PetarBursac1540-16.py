# Kodiranje skripta
# -*- coding: utf-8 -*-


##### Zadatak br. 5

br_pet = raw_input("Unesite petorocifreni broj: ")
# Ispitivanje da li je broj petocifren
while len(br_pet) != 5:
    br_pet = raw_input("Unesite ponovo broj, ali sa tacno pet cifara! : ")
i = 0
max = 0
for i in br_pet:
    if max < i:
        max = i

print "Najveca vrednost cifre zadatog petocifrenog broja je jednaka: ",max
