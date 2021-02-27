def getSance(odvetvi, obrat, zeme, konf=False, news=False):
  sance = "malá"
  body = 0

  if odvetvi == "automotive":
    body += 3
  elif odvetvi == "retail":
    body += 2

  if obrat in range(10, 1001, 1):
    body += 3
  elif obrat >= 1001:
    body += 1

  if zeme in {"Česko", "Slovensko"}:
    body += 3
  elif zeme in {"Německo", "Francie"}:
    body += 2

  print("Zúčastnil se zákazník konference? Pokud ano, zadejte 'y'.")
  konfS = input("Jinak dejte třeba jen enter: ")
  if konfS == "y":
    konf = True
    body += 1

  print("Odebírá zákazník newsletter? Pak zadejte písmeno 'y'.")
  newsS = input("Jinak dejte třeba jen enter: ")
  if newsS == "y":
    news = True
    body += 1

  if body in {6, 7, 8}:
    sance = "střední"
  elif body in {9, 10}:
    sance = "vysoká"

  return sance

odvetvi = input("Zadejte odvětví: ")
obrat = int(input("Zadejte obrat v (celých) mil. Eur: "))
zeme = input("Zadejte zemi: ")
sance = getSance(odvetvi, obrat, zeme)
print(f"Šance na získání zakázky je: {sance}")
