import pandas as pd
import pytemperature
#import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
teploty = pd.read_csv("temperature.csv")
teploty = teploty.rename(columns={"Unnamed: 0": "id", "AvgTemperature": "Avg_Fahrenheit"})
teploty["Avg_Celsia"] = pytemperature.f2c(teploty["Avg_Fahrenheit"])
#print(teploty.info)

#Teploty z 13. listopadu:
den_13 = teploty[teploty["Day"] == 13]
print("Teploty ze 13. listopadu:")
print(den_13)
print()

print("Teploty z 13. listopadu - chybějící měření - pro info:")
print(den_13[den_13["Avg_Fahrenheit"] == -99])
print()

# Teploty z 13. listopadu - měření ok
# Existuje i nějaký podobný příkaz dropna - tedy vymaž řádky obsahující určité hodnoty?
den_13 = den_13[den_13["Avg_Fahrenheit"] != -99]
print("Teploty z 13. listopadu - pouze platná měření:")
print(den_13.info)
print()

print("Počet měření 13. listopadu za jednotlivé regiony: ")
print(den_13.groupby(["Region"])["Avg_Fahrenheit"].count())
print()

print("Průměrná teplota ve stupních Celsia 13. listopadu za jednotlivé regiony: ")
print(round(den_13.groupby(["Region"])["Avg_Celsia"].mean(), 2))
print()

# Podobný problém jako v předchozím příkladu - nevím, jak to napsat jednodušeji, abych dostala min a max
# do jednoho výstupu. Tak jsem vyrobila dvě tabulky a pak je spojila :-)
print("Minimální a maximální teplota 13. listopadu v rámci regionů:")
min_C_reg = den_13.groupby(["Region"])["Avg_Celsia"].min()
max_C_reg = den_13.groupby(["Region"])["Avg_Celsia"].max()
min_max = pd.merge(min_C_reg, max_C_reg, on="Region")
min_max = min_max.rename(columns={"Avg_Celsia_x":"min_Celsia", "Avg_Celsia_y":"max_Celsia"})
print(min_max)
print()
