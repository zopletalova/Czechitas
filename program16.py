class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

    def get_info(self):
        return f"{self.nazev} je žánr {self.zanr}."

class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
      super().__init__(nazev, zanr)
      self.delka = delka

    def get_info(self):
        return f"{super().get_info()} Zároveň je to typ film. Jeho délka: {self.delka} min."

class Serial(Polozka):
    def __init__(self, nazev, zanr, p_epizod, d_epizody):
      super().__init__(nazev, zanr)
      self.p_epizod = p_epizod
      self.d_epizody = d_epizody

    def get_info(self):
        return f"{super().get_info()} Zároveň je to typ seriál. Počet epizod: {self.p_epizod}. Délka jedné: {self.d_epizody} min."

film1 = Film("Ať žijí duchové", "pohádka", 112)
serial1 = Serial("Star Trek", "sci-fi", 87, 45)

print(film1.get_info())
print(serial1.get_info())