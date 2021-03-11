class Uzivatel:
    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.zhlednute_porady = []

    def zhledni_polozku(self, porad):
        self.zhlednute_porady.append(porad)
        return f"Skončil pořad {porad.nazev}. Uložila jsem ho divákovi do seznamu."

    def fdelka_sledovani(self):
        sled_celkem = 0
        for p in self.zhlednute_porady:
            sled_celkem += p.get_celkova_delka()
        return f"ZÁVĚR>>> Prošla jsem seznam pořadů. {self.uzivatelske_jmeno} proseděl u televize dohromady {sled_celkem} min."

class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

    def get_info(self):
        return f"{self.nazev}, což je žánr {self.zanr}."

class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = int(delka)

    def get_info(self):
        return f"{super().get_info()} Zároveň je to typ film. Jeho délka: {self.delka} min."

    def get_celkova_delka(self):
        return self.delka

class Serial(Polozka):
    def __init__(self, nazev, zanr, p_epizod, d_epizody):
        super().__init__(nazev, zanr)
        self.p_epizod = int(p_epizod)
        self.d_epizody = int(d_epizody)

    def get_info(self):
        return f"{super().get_info()} Zároveň je to typ seriál. Počet epizod: {self.p_epizod}. Délka jedné: {self.d_epizody} min."

    def get_celkova_delka(self):
        return (self.p_epizod * self.d_epizody)

divak1 = Uzivatel("Karel Novák")
film1 = Film("Ať žijí duchové", "pohádka", 112)
serial1 = Serial("Star Trek", "sci-fi", 10, 45)

print(f"1>>> Divák {divak1.uzivatelske_jmeno} právě sleduje:")
print(film1.get_info())
print(divak1.zhledni_polozku(film1))
print(f"2>>> Divák {divak1.uzivatelske_jmeno} právě sleduje:")
print(serial1.get_info())
print(divak1.zhledni_polozku(serial1))
print(divak1.fdelka_sledovani())