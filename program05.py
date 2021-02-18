prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Já jsem nový klíč": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}

"""Klíč musí být unikátní, že? Přejmenovala jsem to."""

kniha = ''
pocet = 0

kniha = input("Zadejte název knihy: ")

if (kniha in prodeje2019):
    print(f"V roce 2019 se této knihy prodalo: {prodeje2019[kniha]}")
    pocet = pocet + prodeje2019[kniha]
else:
    print("Tuto knihu jsem v seznamu prodaných knih v roce 2019 nenašel.")

if (kniha in prodeje2020):
    print(f"V roce 2020 se této knihy prodalo: {prodeje2020[kniha]}")
    pocet = pocet + prodeje2020[kniha]
else:
    print("Tuto knihu jsem v seznamu prodaných knih v roce 2020 nenašel.")

print("Počet prodaných knih " + kniha + " v letech 2019 a 2020 dohromady byl: " + str(pocet))