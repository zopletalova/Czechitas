import pandas as pd
import pytemperature
#import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
teploty = pd.read_csv("temperature.csv")
teploty = teploty.rename(columns={"Unnamed: 0": "id", "AvgTemperature": "Avg_Fahrenheit"})
teploty["Avg_Celsia"] = pytemperature.f2c(teploty["Avg_Fahrenheit"])
print(teploty.info)

# Vyšší než 30 C
mereni_30 = teploty[teploty["Avg_Celsia"] > 30]
print("Více než 30 C:")
print(mereni_30)

# Vyšší než 15 C a v Evropě
mereni_15_E = teploty[(teploty["Avg_Celsia"] > 15) & (teploty["Region"] == "Europe")]
print("Více než 15 C a v Evropě:")
print(mereni_15_E)

# Vyšší než 30 C a nižší než -10
mereni_ext = teploty[(teploty["Avg_Celsia"] > 30) | (teploty["Avg_Fahrenheit"] < -10)]
print("Extrémy: více než 30 C a méně než -10 C:")
print(mereni_ext)

# Vypiš podezřelé -72.78 (zřejmě nezadány)
mereni_sus = teploty[teploty["Avg_Celsia"] == -72.78]
print("Podezřelé: hodnota -72.78 C")
print(mereni_sus)
print(f"Našla jsem {mereni_sus.shape[0]} podezřelých hodnot (zřejmě nezadány).")