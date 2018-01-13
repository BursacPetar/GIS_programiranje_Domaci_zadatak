# Kodiranje skripta
# -*- coding: utf-8 -*-

#### Zadatak br. 4

class Inzenjer:
    '''Klasa Inzenjer'''
    def __init__(self, ime="None", prezime="None", jmbg=0, licenca=0):
        self._ime = ime
        self._prezime = prezime
        self._jmbg = int(jmbg)
        self._licenca = int(licenca)

    def __str__(self):  # Ispis informacija o inzenjeru
        return 'Informacije o inzenjeru: \n' \
               'Ime: {0:s}\n' \
               'Prezime: {1:s}\n' \
               'JMBG: {2:d}\n' \
               'Licenca: {3:d}'.format(self._ime, self._prezime, self._jmbg, self._licenca)

    def daj_Ime(self):
        return "Ime: {:s}".format(self._ime)

    def daj_Prezime(self):
        return "Prezime: {:s}".format(self._prezime)

    def daj_JMBG(self):
        return "JMBG: {:d}".format(self._jmbg)

    def daj_br_licence(self):
        return "Broj licence: {:d}".format(self._licenca)

    def postavi_ime(self, ime_novo):
        self._ime = ime_novo

    def postavi_prezime(self, prezime_novo):
        self._prezime = prezime_novo

    def postavi_jmbg(self, jmbg_novi):
        self._jmbg = jmbg_novi

    def postavi_licencu(self, licenca_nova):
        self._licenca = licenca_nova



# test
# inz1 = Inzenjer(ime="Nikola",prezime="Nikolic",licenca=1256)
# inz2 = Inzenjer()
# inz1.postavi_jmbg(123456789)
# inz2.postavi_ime("Marko")
# print inz1
# print inz2
# print inz1.daj_Ime()
# print inz1.daj_br_licence()
# print inz1.daj_JMBG()


class geodetskiInzenjer(Inzenjer):

    def __init__(self, ime="None", prezime = "None",  jmbg=0, licenca=0, staz=0):
        Inzenjer.__init__(self, ime, prezime, jmbg, licenca )
        self._staz = staz

    def __str__(self):
        return Inzenjer.__str__(self) + ("\nStaz: {0:d}".format(self._staz))

    def daj_br_godina_radnog_staza(self):
        return "Broj godina radnog staza: {0:d}".format(self._staz)

    def postavi_br_godina_Radnog_staza(self,br_godina):
        self._staz = br_godina

    def da_li_geodetski_Inzenjer_ima_Licencu(self):
        if self._licenca == 0:
            return "Inzenjer geodezije jos ne poseduje licencu!"
        else:
            return "Inzenjer geodezije poseduje licencu!\n" \
                   "{0:s}".format(self.daj_br_licence())


# test
# ing = geodetskiInzenjer()
# print ing
# print ing.da_li_geodetski_Inzenjer_ima_Licencu()
# ing.postavi_licencu(1112)
# ing.postavi_ime('Petar')

class elektrotehnickiInzenjer(Inzenjer):

    def __init__(self, ime = "None" , prezime="None",  jmbg=0, licenca=0, br_projekata=0):
        Inzenjer.__init__(self, ime, prezime, jmbg, licenca)
        self._br_projekata = br_projekata

    def daj_br_Projekata(self):
        return "Broj projekata: {0:d}".format(self._br_projekata)

    def postavi_br_Projekata(self, broj_pr):
        self._br_projekata = broj_pr

    def __str__(self):
        return Inzenjer.__str__(self) + ("\nBroj projekata: {0:d}".format(self._br_projekata))

    def da_li_elektrotehnicki_Inzenjer_ima_Licencu(self):
        if self._licenca == 0:
            return "Inzenjer elektrotehnike jos ne poseduje licencu!"
        else:
            return "Inzenjer elektrotehnike poseduje licencu!" \
                   "\n{0:s}".format(self.daj_br_licence())



# test
# ine = elektrotehnickiInzenjer()
# print ine
# ine.postavi_licencu(2222)
# print ine.da_li_elektrotehnicki_Inzenjer_ima_Licencu()





