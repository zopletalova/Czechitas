class Auto:

  def get_info(self):
    return f"Auto SPZ: {self.spz} je typu: {self.zn_typ}."

  def pujc_auto(self):
      if self.volne:
          self.volne = False
          return ("Potvrzuji zapůjčení vozidla")
      else:
          return ("Vozidlo není k dispozici")

  def vrat_auto(self, km_ujel, dny):
      self.najeto += km_ujel
      self.volne = True
      if dny < 7:
          cena = dny * 400
      else:
          cena = dny * 300
      return f"Cena za půjčení je {cena} Kč"

  def __init__(self, spz, zn_typ, najeto):
    self.spz = spz
    self.zn_typ = zn_typ
    self.najeto = najeto
    self.volne = True

auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)
auto3 = Auto("2M1 8429", "Hyundai i30", 105765)

print("Zadejte značku auta, které si chcete půjčit.")
auto_p = input("Peugeot, Škoda, nebo Hyundai: ")

# Proč mi prosím nefungovalo
# if auto_p not in auto1.zn_typ or auto2.zn_typ or auto3.zn_typ:
# nebo tak něco?

if auto_p not in {"Peugeot", "Škoda", "Hyundai"}:
    print("Zadali jste neznámý typ auta.")
else:
    if auto_p in auto1.zn_typ:
        auto_o = auto1
    elif auto_p in auto2.zn_typ:
        auto_o = auto2
    elif auto_p in auto3.zn_typ:
        auto_o = auto3

    print(auto_o.get_info())
    print(auto_o.pujc_auto())
    print()
    print("A teď auto vracíte.")
    km_ujel = int(input("Zadejte počet ujetých kilometrů: "))
    dny = int(input("Zadejte počet dnů zápůjčky: "))
    print(auto_o.vrat_auto(km_ujel, dny))
