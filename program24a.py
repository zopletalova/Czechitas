import pandas as pd

#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
teploty = pd.read_csv("temperature.csv")

# Tohle jsem si pro zorientování se vyrobila dřív, než jsem se pročetla k pokročilejší variantě :-)
teploty = teploty.rename(columns={"Unnamed: 0": "id", "AvgTemperature": "Avg_Fahrenheit"})
teploty["Avg_Celsia"] = round(5*(teploty["Avg_Fahrenheit"]-32)/9, 1)
print(teploty.info)

# Praha
mereni_Praha = teploty[teploty["City"] == "Prague"]
print("Měření Praha:")
print(mereni_Praha)

# Vyšší než 80 F
mereni_80 = teploty[teploty["Avg_Fahrenheit"] > 80]
print("Více než 80 F:")
print(mereni_80)

# Vyšší než 60 F a v Evropě
mereni_60_E = teploty[(teploty["Avg_Fahrenheit"] > 60) & (teploty["Region"] == "Europe")]
print("Více než 60 F a v Evropě:")
print(mereni_60_E)

# Vyšší než 80 F a nižší než -20
mereni_ext = teploty[(teploty["Avg_Fahrenheit"] > 80) | (teploty["Avg_Fahrenheit"] < -20)]
print("Extrémy: více než 80 F a méně než -20 F:")
print(mereni_ext)