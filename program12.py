class Auto:

  def get_info(self):
    return f"Auto SPZ: {self.spz} je typu: {self.zn_typ}."

  def pujc_auto(self):
      if self.volne:
          self.volne = False
          return ("Potvrzuji zapůjčení vozidla")
      else:
          return ("Vozidlo není k dispozici")

  def __init__(self, spz, zn_typ, najeto):
    self.spz = spz
    self.zn_typ = zn_typ
    self.najeto = najeto
    self.volne = True

auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)
auto3 = Auto("2M1 8429", "Hyundai i30", 105765)

print("Zadejte značku auta, které si chcete půjčit.")
auto = input("Peugeot, Škoda nebo Hyundai: ")
if auto in auto1.zn_typ:
    print(auto1.get_info())
    print(auto1.pujc_auto())
elif auto in auto2.zn_typ:
    print(auto2.get_info())
    print(auto2.pujc_auto())
elif auto in auto3.zn_typ:
    print(auto3.get_info())
    print(auto3.pujc_auto())
else:
    print("Zadali jste neznámý typ auta.")

# A ještě jednou pro ověření, že půjčené je fakt půjčené:
print("Zadejte značku auta, které si chcete půjčit.")
auto = input("Peugeot, Škoda nebo Hyundai: ")
if auto in auto1.zn_typ:
    print(auto1.get_info())
    print(auto1.pujc_auto())
elif auto in auto2.zn_typ:
    print(auto2.get_info())
    print(auto2.pujc_auto())
elif auto in auto3.zn_typ:
    print(auto3.get_info())
    print(auto3.pujc_auto())
else:
    print("Zadali jste neznámý typ auta.")