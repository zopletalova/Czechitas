from datetime import datetime, timedelta
prvni_open = datetime(2021, 7, 1)
prvni_closed = datetime(2021, 8, 10)
druhy_open = datetime(2021, 8, 11)
druhy_closed = datetime(2021, 8, 31)

navsteva = input("Zadejte datum, na které chcete lístky (ve středoev.formátu): ")
navsteva = datetime.strptime(navsteva, "%d. %m. %Y")

if navsteva < prvni_open or navsteva > druhy_closed:
    print("Kino je ve vámi zadaný den zavřeno. Otevřeno je pouze o prázdninách.")
else:
    osoby = int(input("Pro kolik osob chcete lístky? "))
    if navsteva >= prvni_open and navsteva <= prvni_closed:
        print(f"První část prázdnin - počet osob: {osoby}, cena proto je {osoby * 250} Kč.")
    else:
        print(f"Druhá část prázdnin - počet osob: {osoby}, cena proto je {osoby * 180} Kč.")