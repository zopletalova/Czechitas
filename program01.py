baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

cislo = 'cislo'
cislo = input("Zadej číslo balíku: ")
if (cislo in baliky) and (baliky[cislo] == True):
    print("Balík byl předán kurýrovi.")
else:
    if (cislo in baliky) and (baliky[cislo] == False):
        print("Balík zatím nebyl předán kurýrovi.")
    else:
        print("Bohužel, takový balík neexistuje.")

"""Dotaz - lze v Pythonu pouzit nejake to elseif, abych nemusela vnorit podminku? 
Chtela jsem osetrit situaci, kdy balik zadaneho cisla neexistuje"""