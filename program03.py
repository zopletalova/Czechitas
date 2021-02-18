volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}

hodina = 0
hodina = int(input("Zadejte hodinu, od které potřebujete zasedačku: "))
if hodina in volnePokoje:
    print(f"Počet volných zasedaček: {len(volnePokoje[hodina])} ")
else:
    print(f"O volných kapacitách na tuto hodinu nemáme informace.")
