class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

class Uchazec(Kontakt):
  def __init__(self, jmeno, email, datum_pohovoru):
    super().__init__(jmeno, email)
    self.datum_pohovoru = datum_pohovoru
    self.zapis_z_pohovoru = ""

  def uloz_zapis(self, zapis):
    if self.datum_pohovoru > datetime.now():
        return "Chyba, zadáváte zápis z pohovoru konaného v budoucnu."
    else:
        self.zapis_z_pohovoru = zapis
        return "Datum ok. Uložil jsem zápis do záznamů."

from datetime import datetime, timedelta
uchazec1 = Uchazec("Karel Novák", "novak@email.com", datetime(2021, 7, 1))
uchazec2 = Uchazec("Jan Nový", "novy@gmail.com", datetime(2021, 3, 6))

zapis = input(f"Uchazeč 1 - Zadejte zápis z pohovoru: ")
print("Uchazeč 1 - datum pohovoru 1. 7. 2021:")
print(uchazec1.uloz_zapis(zapis))
print()

zapis = input(f"Uchazeč 2 - Zadejte zápis z pohovoru: ")
print("Uchazeč 2 - datum pohovoru 6. 3. 2021:")
print(uchazec2.uloz_zapis(zapis))