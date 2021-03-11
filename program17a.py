class Uzivatel:
    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = 0

    def pripocti_zhlednuti(self, delka):
        self.delka_sledovani += delka
        return(f"Celkem divák {self.uzivatelske_jmeno} proseděl u televize: {self.delka_sledovani} min.")

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

print(f"1>>> Divák {divak1.uzivatelske_jmeno} se díval na:")
print(film1.get_info())
delka = film1.get_celkova_delka()
print(divak1.pripocti_zhlednuti(delka))
print(f"2>>> Divák {divak1.uzivatelske_jmeno} se díval na:")
print(serial1.get_info())
delka = serial1.get_celkova_delka()
print(divak1.pripocti_zhlednuti(delka))
