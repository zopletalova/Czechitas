from faker import Faker
generator_falesnych_dat = Faker("cs_CZ")
generator_falosnych_dat = Faker("sk_SK")

class Balik:
  def get_info(self):
    print(f"Příjemce balíku: {self.name}")
    print(f"Balík doručte na adresu:")
    return self.address

  def __init__(self, name, address):
    self.name = name
    self.address = address

jmeno1 = generator_falesnych_dat.name()
prijmeni1 = generator_falesnych_dat.address()
balik1 = Balik(jmeno1, prijmeni1)
print(balik1.get_info())
print()

jmeno2 = generator_falosnych_dat.name()
prijmeni2 = generator_falosnych_dat.address()
balik2 = Balik(jmeno2, prijmeni2)
print(balik2.get_info())