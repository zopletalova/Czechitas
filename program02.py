sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

soucastka = 'xxx'
mnozstvi = 0
print("Dobrý den, vážený zákazníku či zákaznice.")
soucastka = input("Zadejte prosím kód součástky: ")

if (soucastka in sklad):
    mnozstvi = int(input("Zadejte prosím požadované množství: "))
    if sklad[soucastka] >= mnozstvi:
        sklad[soucastka] = sklad[soucastka] - mnozstvi
        print("Dobrá zpráva! Těchto součástek máme ve skladu dostatek. Posíláme na výdej.")
        print(f"Nyní nám ve skladu zbývá: {sklad[soucastka]}")
    else:
        print(f"Tuto součástku sice máme, ale jen omezené množství, konkrétně: {sklad[soucastka]} ")
        sklad[soucastka] = sklad[soucastka] - sklad[soucastka]
        print(f"Na výdej vám proto posíláme vše, co máme, a aktuálně jsme ve skladu na {sklad[soucastka]}.")
else:
    print("Bohužel, tato součástka buď neexistuje, nebo není skladem.")