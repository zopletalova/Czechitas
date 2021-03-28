#import wget
import pandas as pd

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

vykazy = pd.read_csv("vykazy.csv")
#načítám to, co jsem si v minulém programu uložila do csv - v únoru pracující zaměstnanci
zamestnanci = pd.read_csv("zamestnanci.csv", index_col="cislo_zamestnance")
vykazy = vykazy.rename(columns={"date": "datum", "hours": "hodin", "project": "projekt", "emloyee_id": "cislo_zamestnance"})
vykazy = vykazy.set_index("cislo_zamestnance")
#print(vykazy.info)

print("Celkový počet hodin za jednotlivé projekty:")
print(vykazy.groupby("projekt")["hodin"].sum())

#DOPLNĚK
zamestnanci_vykazy = pd.merge(zamestnanci, vykazy, how="left", on="cislo_zamestnance")
#print(zamestnanci_vykazy.head())
#print(zamestnanci_vykazy.columns)

print()
print(f"Rozměry tabulky vykazy: {vykazy.shape}")
print(f"Rozměry spojené tabulky zamestnanci_vykazy: {zamestnanci_vykazy.shape}")
print()

#Podívám se na zaměstnance, kteří neměli projekt, nebo u něj neměli odpracované hodiny
zam_bez_projekt = zamestnanci_vykazy[(zamestnanci_vykazy["projekt"].isnull()) | (zamestnanci_vykazy["hodin"].isnull())]
#print(zam_bez_projekt)
print(f"Zaměstnanců bez odpracovaných hodin na projektu bylo: {zam_bez_projekt.shape[0]}")
print()

print("Počet hodin - přes kanceláře a projekty: ")
print(zamestnanci_vykazy.groupby(["mesto", "projekt"])["hodin"].sum())
print()
print("Počet hodin - přes projekty a kanceláře: ")
print(zamestnanci_vykazy.groupby(["projekt", "mesto"])["hodin"].sum())