#import wget
import pandas as pd

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

zam_praha = pd.read_csv('zam_praha.csv')
zam_praha["mesto"] = "Praha"
zam_plzen = pd.read_csv('zam_plzeň.csv')
zam_plzen["mesto"] = "Plzeň"
zam_liberec = pd.read_csv('zam_liberec.csv')
zam_liberec["mesto"] = "Liberec"
platy = pd.read_csv("platy_2021_02.csv")

zamestnanci = pd.concat([zam_praha, zam_plzen, zam_liberec])
#print(zamestnanci.info)

#print(platy.info)

zamestnanci_platy = pd.merge(zamestnanci, platy, how="left", on="cislo_zamestnance")
zamestnanci_platy = zamestnanci_platy.set_index("cislo_zamestnance")
#print(zamestnanci_platy.info)

print(f"Tabulka zamestnanci měla rozměry {zamestnanci.shape} a tabulka platy rozměry {platy.shape}.")
print(f"Spojená tabulka zamestnanci_platy má rozměry {zamestnanci_platy.shape}.")
print(f"Vypadá to, že {zamestnanci.shape[0] - platy.shape[0]} zaměstnanců zřejmě nemá uveden plat.")

#DOPLNĚK1
pocet_nepracujicich = zamestnanci_platy[zamestnanci_platy["plat"].isnull()].shape[0]
print(f"Ověření pomocí isnull (jestli left joinem neodpadl nějaký řádek z platy):"
      f" - plat nemá uvedeno {pocet_nepracujicich} zaměstnanců.")
print("Je to zároveň počet nepracujících.")
print()
#Konec DOPLŇKU1

print("Půměrný plat na kancelář (město):")
print(zamestnanci_platy.groupby("mesto")["plat"].mean())

#Nebyla jsem si jistá, co Python udělá při počítání průměru s chybějícími hodnotami
#Zkusila jsem ty řádky pro jistotu dropnout, ale je vidět, že je ignoruje - průměry vyšly stejně:
#zamestnanci_unor = zamestnanci_platy.dropna(subset=["plat"])
#print(zamestnanci_unor.groupby("mesto")["plat"].mean())
#A ještě jsem si v únoru zaměstnané jako zdroj pro příklad 27 poslala do csv
#zamestnanci_unor.to_csv("zamestnanci.csv", index="cislo_zamestnance")

#DOPLNĚK2
nepracujici = zamestnanci_platy[zamestnanci_platy["plat"].isnull()]
print(nepracujici)
#nepracujici.to_csv("nepracujici.csv", index="cislo_zamestnance")