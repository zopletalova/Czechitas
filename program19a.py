from forex_python.converter import CurrencyRates
meny = ["USD", "CZK", "EUR", "GBP", "DKK"]
prevodnik = CurrencyRates()

cilova_mena = input("Zadejte cílovou měnu (umím USD, CZK, EUR, GBP, DKK): ")
if cilova_mena in meny:
    pozadovano_v_cilove_mene = int(input(f"Zadejte, kolik {cilova_mena} chcete: "))
    cena_v_korunach = prevodnik.convert(cilova_mena, "CZK", pozadovano_v_cilove_mene)
    print(f"Na {pozadovano_v_cilove_mene} {cilova_mena} potřebujete {round(cena_v_korunach,2)} CZK.")
else:
    print("Vámi zadanou měnu neumím nebo nechci převádět.")