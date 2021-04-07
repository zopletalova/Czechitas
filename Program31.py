#import wget
import pandas as pd
import matplotlib.pyplot as plt

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

#print(platy.min())
#print(platy.max())

# Základní řešení
platy.hist(["plat"], bins=[30000, 35000, 40000, 45000, 50000, 55000, 60000], color="Red")
plt.title('Platy zaměstnanců ve všech městech')
plt.xlabel('Platy')
plt.ylabel('Počty')
plt.show()

# Doplněk
zamestnanci = pd.concat([zam_praha, zam_plzen, zam_liberec])
zamestnanci_platy = pd.merge(zamestnanci, platy, how="left", on="cislo_zamestnance")
zamestnanci_platy = zamestnanci_platy.set_index("cislo_zamestnance")

# Vyhodím ty, kteří nemají uvedený plat
zamestnanci_unor = zamestnanci_platy.dropna(subset=["plat"])

# Tady nevím, jak vložit do grafu info, o které město se jedná...
grouped = zamestnanci_unor.groupby("mesto")
grouped.hist(["plat"], bins=[30000, 35000, 40000, 45000, 50000, 55000, 60000])
plt.show()

# ...a tak jsem vyrobila aspoň toto: :-)
for mesto in zamestnanci_unor["mesto"].unique():
    zamestnanci_unor[zamestnanci_unor["mesto"] == mesto].hist(["plat"], bins=[30000, 35000, 40000, 45000, 50000, 55000, 60000])
    plt.title(f'Platy zaměstnanců ve městě {mesto}')
    plt.xlabel('Platy')
    plt.ylabel('Počty')
    plt.show()