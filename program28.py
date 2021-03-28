#import wget
import pandas as pd

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")

staty = pd.read_json("staty.json")
gdp = pd.read_csv("gdp.csv")

#print(staty.head)
print(staty.columns)
#print(gdp.info)
print(gdp.columns)
print()

evropa = staty[staty["region"] == "Europe"]
print("Státy, které leží v Evropě:")
print(evropa)
print()

print("Počty států v subregionech Evropy:")
print(evropa.groupby("subregion")["subregion"].count())
print()

print("Počty obyvatel v subregionech Evropy:")
print(evropa.groupby(["subregion"])["population"].sum())
print()

#ROZŠÍŘENÍ
#Řádky s chybějícími údaji v tabulce GDP:
chybejici = gdp[(gdp["2017"].isnull())|(gdp["2018"].isnull())|(gdp["2019"].isnull())]
print(f"Údaje o HDP chybí u chybí u {chybejici.shape[0]} států.")
print(f"Původní počet řádků tabulky GDP: {gdp.shape[0]}.")
gdp = gdp.dropna()
print(f"Počet řádků tabulky GDP po dropnutí řádků s NaN: {gdp.shape[0]}.")
print()

#Spojení tabulek - zúžím to jen na státy, které mají všechny hodnoty HDP:
gdp = gdp.rename(columns={"Country Code":"alpha3Code", "2017": "gdp2017","2018":"gdp2018","2019":"gdp2019"})
staty_gdp = pd.merge(staty, gdp[["gdp2017","gdp2018","gdp2019","alpha3Code"]], how="inner", on="alpha3Code")
print("Spojená tabulka info:")
print(staty_gdp.info)
print()

#Sumy HDP a populace za subregiony, přidání sloupce s HDP na hlavu
#FutureWarning:
#Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
#To mi napsal na ten následující řádek, i když to teda spočítal. Jak bych to měla napsat jinak?
subregiony = staty_gdp.groupby(["subregion"])["population", "gdp2019"].sum()
subregiony["gdp_head2019"] = subregiony["gdp2019"]/subregiony["population"]
print(subregiony)

