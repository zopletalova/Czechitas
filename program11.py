class Auto:
  # toto jsem si dodala navíc:
  def get_info(self):
    return f"Auto SPZ: {self.spz} je typu: {self.zn_typ} a má najeto {self.najeto}"

  def __init__(self, spz, zn_typ, najeto):
    self.spz = spz
    self.zn_typ = zn_typ
    self.najeto = najeto
    self.volne = True

# v zadání bylo, že auta jsou tři ale byla tam jen dvě, tak jsem si jedno vymyslela :-)
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)
auto3 = Auto("2M1 8429", "Hyundai i30", 105765)

# toto je taky oproti zadání navíc
print(auto1.get_info())
print(auto2.get_info())
print(auto3.get_info())
