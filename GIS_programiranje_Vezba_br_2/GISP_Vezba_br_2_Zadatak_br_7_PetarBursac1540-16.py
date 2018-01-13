# Kodiranje skripta
# -*- coding: utf-8 -*-


###### Zadatak br. 7

#Написати програм који имплементира игру Ајнц са једним играчем. Игра се са
#шпилом од 52 карте. На почетку играч уноси своје име након чега рачунар дели две
#карте играчу и две карте себи. У свакој следећој итерацији рачунар дели по једну
#карту играчу и себи. Циљ игре је сакупити карте које у збиру имају 21 поен. Карте са
#бројевима носе онолико бодова колики је број, док жандар, дама, краљ носе 10
#бодова. Карта Ас може да носи 1 или 10 бодова, у зависности од тога како играчу
#одговара. Играч који сакупи 21 је победио. Уколико играч премаши 21 бод, победник
#је његов противник.



from random import randint


def talon_sa_kartama():
    # definisanje karata - vrednosti i tipa
    karta_vrednost = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Zandar', 'Dama', 'Kralj']
    karta_tip = ['Srce', 'Pik', 'Tref', 'Karo']
    talon = []
    # Na ovaj nacin se definise talon sa kombinacijom vrednosti i tipa karte
    for i in karta_tip:
        for j in karta_vrednost:
            talon.append(j + ' - ' + i)
    return talon


def vrednost_karte(karta):
    # odredjivanje vrednosti, citanje samo prvog karaktera
    if karta[:1] in ('Z', 'D', 'K', '1'):
        return int(10)
    elif karta[:1] in ('2', '3', '4', '5', '6', '7', '8', '9'):
        return int(karta[:1])
    elif karta[:1] == 'A':
        print ("\n" + str(karta))
        num = input("Da li zelite da karta As ima vrednost 1 ili 11?\n>")
        while num != '1' or num != '11':
            if num == '1':
                return int(1)
            elif num == '11':
                return int(11)
            else:
                num = input("Da li zelite da karta As ima vrednost 1 ili 11?\n>")


def nova_karta(talon):
    return talon[randint(0, len(talon)-1)]


def ukloni_kartu(talon, karta):
    return talon.remove(karta)


igraj_opet = ''
while igraj_opet != 'IZLAZ':
    ime = raw_input("Igra 'Blackjack' je zapoceta, unesite vase ime: ")
    novi_talon = talon_sa_kartama()
    karta1 = nova_karta(novi_talon)
    ukloni_kartu(novi_talon, karta1)
    karta2 = nova_karta(novi_talon)
    ukloni_kartu(novi_talon, karta2)
    print ("\n\n\n\n" + str(karta1) + " i " + str(karta2))
    vred1 = vrednost_karte(karta1)
    vred2 = vrednost_karte(karta2)
    ukupno = vred1 + vred2
    print("sa ukupnom vrednoscu karata: " + str(ukupno) )
    racunar_karta1 = nova_karta(novi_talon)
    ukloni_kartu(novi_talon, racunar_karta1)
    racunar_karta2 = nova_karta(novi_talon)
    ukloni_kartu(novi_talon, racunar_karta2)
    racunar_vred1 = vrednost_karte(racunar_karta1)
    racunar_vred2 = vrednost_karte(racunar_karta2)
    racunar_ukupno = racunar_vred1 + racunar_vred2
    print ('\n Racunar je igrao, jedna od njegovih karata je data a druga je okrenuta:\n')
    print ("Prva karta " + str(racunar_karta1) + " i druga karta je okrenuta.")

    if ukupno == 21:
        print("Blackjack! " + str(ime) + " Vi ste pobedili!")
    else:
        while ukupno < 21:
            odgovor = input("Da li zelite da nastavite ili cekate [nastavite - 'da', cekate - 'cekam']?\n> ")
            if odgovor.lower() == 'da':
                jos_karata = nova_karta(novi_talon)
                ukloni_kartu(novi_talon, jos_karata)
                jos_vrednosti = vrednost_karte(jos_karata)
                ukupno += int(jos_vrednosti)
                print (str(jos_karata) + " i ukupna vrednost karata je: " + str(ukupno))
                if ukupno > 21:
                    print(str(ime) + " Vi ste izgubili!")
                    igraj_opet = input("Da li zelite da nastavite? IZLAZ za napustanje igre!\n")
                elif racunar_ukupno == 21:
                    print("Blackjack!" + str(ime) + "Vi ste pobedili!")
                    play_again = input("Da li zelite da nastavite? IZLAZ za napustanje igre!\n")
                else:
                    continue
            elif odgovor.lower() == 'cekam':
                print("Racunar nastavlja sa igrom i njegova sledeca karta je: ")
                print(racunar_karta2 + " sa ukupnom vrednoscu karata: " + str(racunar_ukupno))
                if racunar_ukupno < 17:
                    print("Racunar nastavlja da igra!")
                    racunar_jos = nova_karta(novi_talon)
                    racunar_jos_vrednost = vrednost_karte(racunar_jos)
                    print("Karta je: " + str(racunar_jos))
                    racunar_ukupno += int(racunar_jos_vrednost)
                    if racunar_ukupno > 21 and ukupno <= 21:
                        print("Racunar je izgubio! " + str(ime) + " Vi ste pobedili!")
                    elif racunar_ukupno < 21 and racunar_ukupno > ukupno:
                        print("Vrednost karata racunara je: " + str(racunar_ukupno) + ", " + str(ime) + " Vi ste izgubili!")
                    else:
                        continue
                elif racunar_ukupno == ukupno:
                    print("Jednake vrednosti karata, nema pobednika!")
                elif racunar_ukupno < ukupno:
                    print(str(ime) + " Vi ste pobedili!")
                else:
                    print(str(ime) + " Vi ste izgubili!")
                igraj_opet = input("\nDa li zelite da nastavite? IZLAZ za napustanje igre!\n")
                break
print("Hvala na igri!")