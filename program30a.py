#import wget
import pandas as pd
import openpyxl

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

vykazy = pd.read_csv("vykazy.csv")
zamestnanci = pd.read_csv("zamestnanci.csv", index_col="cislo_zamestnance")
vykazy = vykazy.rename(columns={"date": "datum", "hours": "hodin", "project": "projekt", "emloyee_id": "cislo_zamestnance"})
vykazy = vykazy.set_index("cislo_zamestnance")

zamestnanci_vykazy = pd.merge(zamestnanci, vykazy, how="left", on="cislo_zamestnance")
print(zamestnanci_vykazy.info)
print()

#Export do excelu:
#zamestnanci_vykazy.to_excel("C:/Users/Zuzana/Documents/Python/vykazy.xlsx")

#Načtení z excelu:
overeni = pd.read_excel("C:/Users/Zuzana/Documents/Python/vykazy.xlsx", index_col="cislo_zamestnance")
print(overeni.info)