vysledky = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]

def ohodnot_studenta(znamky):
  hodnoceni = "Prospěl"
  prumer = sum(znamky)/len(znamky)

  if prumer <= 1.5 and max(znamky) < 3:
    hodnoceni = "Prospěl s vyznamenáním."
  if max(znamky) == 5:
    hodnoceni = "Neprospěl."

  return hodnoceni

znamky = []

for item in vysledky:
  znamky = item.values()
  znamky = list(znamky)
  znamky = znamky[1:]
  hodnoceni = ohodnot_studenta(znamky)
  jmeno = item["Jméno"]
  print(f"{jmeno}: {hodnoceni}")