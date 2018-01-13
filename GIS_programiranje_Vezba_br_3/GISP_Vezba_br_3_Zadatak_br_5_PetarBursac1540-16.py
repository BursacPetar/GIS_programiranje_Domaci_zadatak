# Kodiranje skripta
# -*- coding: utf-8 -*-

##### Zadatak br. 5


class Osoba():
    '''Klasa osoba'''
    def __init__(self, *lista_atributa ):
        self._ime = input("Unesite ime ['Ime',str]: ")
        self._prezime = input("Unesite prezime ['Prezime',str]: ")
        self._datum_rodjenja = input("Unesite datum rodjenja ['xx.xx.xxxx',str]: ")
        self._adresa_stanovanja = input("Unesite adresu stanovanja ['Adresa',str]: ")

    def __str__(self):
        return "Osnovne informacije: \n" \
               "Ime: {0:s}\n" \
               "Prezime: {1:s}\n" \
               "Datum rodjenja: {2:s}\n" \
               "Adresa stanovanja: {3:s}\n".format(self._ime,  self._prezime, self._datum_rodjenja, self._adresa_stanovanja)

    def daj_Ime(self):
        return "Ime osobe: {0:s}".format(self._ime)

    def daj_Prezime(self):
        return "Prezime osobe: {0:s}".format(self._prezime)

    def daj_Datum_rodjenja(self):
        return "Datum rodjenja osobe: {0:s}".format(self._datum_rodjenja)

    def daj_Adresu(self):
        return "Adresa osobe: {0:s}".format(self._adresa_stanovanja)

    def postavi_Ime(self, ime):
        self._ime = ime

    def postavi_Prezime(self, pr):
        self._prezime = pr

    def postavi_Datum_rodjenja(self, dr):
        self._datum_rodjenja = dr

    def postavi_Adresu(self, adresa):
        self._adresa_stanovanja = adresa


# test
# o = Osoba()
# print o


class Djak(Osoba):
    '''Klasa Djak je izvedena klasa od klase Osoba'''

    def __init__(self, *lista_atributa):
        Osoba.__init__(self, *lista_atributa)
        self._naziv_skole = input("Unesite naziv skole djaka: ['Naziv',str]")
        self._odeljenje = input("Unesite naziv odeljenja djaka: ['XX-x',str]")
        self._god_upisa = input("Unesite godinu upisa skole djaka: [xxxx,int]")

    def __str__(self):
        return Osoba.__str__(self) + ("Naziv skole: {0:s} \nOdeljenje: {1:s} \nGodina upisa: {2:d}".format(self._naziv_skole,self._odeljenje,self._god_upisa))

    def daj_naziv_Skole(self):
        return "Naziv skole: {0:s}".format(self._naziv_skole)

    def daj_odeljenje(self):
        return "Odeljenje:{0:s}".format(self._odeljenje)

    def daj_godinu_upisa(self):
        return self._god_upisa

    def postavi_naziv_skole(self, nskole):
        self._naziv_skole = nskole

    def postavi_odeljenje(self, od):
        self._odeljenje = od

    def postavi_godinu_upisa(self, gu):
        self._god_upisa = gu

    def trenutni_razred_skole(self):
        raz = str(self.daj_odeljenje())
        raz1 = raz.split(":")
        raz2 = raz1[1]
        razr = raz2.split("-")
        return razr[0]

    def da_li_je_djak_obnovio_razred(self, *atr):
        p = input("Unesite vrednost tekuce godine: [xxxx]")
        recnik = {'I':7,'II':8,'III':9,'IV':10,'V':11,'VI':12,'VII':13,'VIII':14}
        godr = str(self.daj_Datum_rodjenja())
        godrodj = godr.split(".")
        godrodj1 = godrodj[2]
        a = int(self.daj_godinu_upisa()) - int(godrodj1)
        if a==7:
            a1 = int(p) - int(godrodj1)
            a2 = self.trenutni_razred_skole()
            a3 = recnik[a2]
            if a1 == a3:
                print "Djak nije ponavljao ni jedan razred do sada!"
            else:
                print "Djak je ponavljao!"
        else:
            "Proverite godinu upisa skole!"



# test
# dj = Djak()
# print dj
# dj.trenutni_razred_skole()
# dj.da_li_je_djak_obnovio_razred()

class Zaposlen(Osoba):

    '''Klasa Zaposlen je izvedena klasa od klase Osoba'''

    def __init__(self, lista_zakljucenja=[], lista_prekida=[], *lista_atributa):
        Osoba.__init__(self, *lista_atributa)
        self._naziv_kompanije = input("Unesite naziv kompanije: ")
        self._naziv_departmana = input("Unesite naziv departmana: ")
        self.lista_kompanija = []
        self.lista_kompanija.append((self._naziv_kompanije,self._naziv_departmana))
        self._lista_zakljucenja = lista_zakljucenja
        self._lista_prekida = lista_prekida

    def daj_listu_kompanija(self):
        for i in self.lista_kompanija:
            return "Lista kompanija: \n",i[0]

    def dodaj_kompaniju(self, komp):
        self.lista_kompanija[0].append(komp)

    def daj_listu_departmana(self):
        for i in self.lista_kompanija:
            return "Lista departmana: \n",i[1]

    def dodaj_departman(self, dep):
        self.lista_kompanija[1].append(dep)

    def dajListuZakljucenja(self):
        return self._lista_zakljucenja

    def dajListuPrekida(self):
        return self._lista_prekida

    def postaviListuZakljucenja(self, lista_zakljucenja):
        self._lista_zakljucenja = lista_zakljucenja

    def postaviListuPrekida(self, lista_prekida):
        self._lista_prekida = lista_prekida

    def lista_Kompanija_atr(self):
        for i in self.lista_kompanija:
            return "Kompanija: {0:s}\n" \
                   "Departman: {1:s}".format(i[0],i[1])

    def __str__(self):
        return Osoba.__str__(self) + str(self.lista_Kompanija_atr())

    def daj_radni_staz(self):
        broj_firmi = int(input("Unesite broj firmi u kojima je zaposleni do sada radio: "))
        i = 0
        lista_zak = []
        lista_prek = []
        while i < broj_firmi:
            datum_zakljucenja = raw_input("Unesite datum zakljucenja ugovora: [xx.xx.xxxx] ")
            datum_prekida = raw_input("Unesite datum prekida ugovora: [xx.xx.xxxx] ")
            lista_zak.append(datum_zakljucenja)
            lista_prek.append(datum_prekida)
            i += 1
        aa = raw_input("Da li zaposlen trenutno negde radi(DA ili NE)  ")
        if aa == "DA":
            datum_zakljucenja = raw_input("Unesite datum zakljucenja novog ugovora: [xx.xx.xxxx] ")
            datum_prekida = raw_input("Unesite danasnji datum: [xx.xx.xxxx] ")
            lista_zak.append(datum_zakljucenja)
            lista_prek.append(datum_prekida)
        self.postaviListuZakljucenja(lista_zak)
        self.postaviListuPrekida(lista_prek)

        listaz=self.dajListuZakljucenja()
        listap=self.dajListuPrekida()
        ii = 0
        brrd = 0
        while ii < len(listap):
            z = listaz[ii]
            p = listap[ii]
            z1 = z.split(".")
            p1 = p.split(".")
            d1 = int(z1[0])
            m1 = int(z1[1])
            g1 = int(z1[2])
            d2 = int(p1[0])
            m2 = int(p1[1])
            g2 = int(p1[2])
            if d1 <= d2:
                d = d2-d1
            else:
                d = d2-d1+30
                m2 = m2-1
            if m1 <= m2:
                m = m2-m1
            else:
                m = m2-m1+12
                g2 = g2-1
            g = g2-g1
            brm = m+g*12
            brrd = brrd+brm*30+d
            ii += 1
        return "Ukupan broj meseci radnog staza je: {0:d} i radnih dana: {1:d}".format(brrd/30,brrd%30)




# test
# z1 = Zaposlen()
# print z1
# z1.daj_radni_staz()

# Glavni program
o = Osoba()
print o

dj = Djak()
print dj
dj.trenutni_razred_skole()
dj.da_li_je_djak_obnovio_razred()

z1 = Zaposlen()
print z1
z1.daj_radni_staz()

