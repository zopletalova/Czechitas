from forex_python.bitcoin import BtcConverter
meny = ["USD", "CZK", "EUR", "GBP", "DKK"]
bprevodnik = BtcConverter()

puvodni_mena = input("Zadejte vaši měnu (umím USD, CZK, EUR, GBP, DKK): ")
if puvodni_mena in meny:
    pozadovano_bitcoinu = int(input(f"Zadejte, kolik Bitcoinů chcete: "))
    cena_za_bitcoiny = bprevodnik.get_latest_price(puvodni_mena) * pozadovano_bitcoinu
    print(f"Na {pozadovano_bitcoinu} Btc potřebujete {round(cena_za_bitcoiny,2)} {puvodni_mena}.")
else:
    print("Vámi zadanou měnu neumím nebo nechci převádět.")