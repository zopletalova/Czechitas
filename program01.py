baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

cislo = input("Zadej číslo balíku: ")
if cislo in baliky:
    if baliky[cislo]:
        print("Balík byl předán kurýrovi.")
    else:
        print("Balík zatím nebyl předán kurýrovi.")
else:
   print("Bohužel, takový balík neexistuje.")
