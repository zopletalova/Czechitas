from faker import Faker
generator_falesnych_dat = Faker("cs_CZ")

class Balik:
  def get_info(self):
    print(f"Příjemce balíku: {self.name}")
    print(f"Balík doručte na adresu:")
    return self.address

  def __init__(self, name, address):
    self.name = name
    self.address = address

jmeno = generator_falesnych_dat.name()
prijmeni = generator_falesnych_dat.address()
balik1 = Balik(jmeno, prijmeni)
print(balik1.get_info())