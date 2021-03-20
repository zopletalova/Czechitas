import pandas as pd
import pytemperature
#import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
teploty = pd.read_csv("temperature.csv")
teploty = teploty.rename(columns={"Unnamed: 0": "id", "AvgTemperature": "Avg_Fahrenheit"})
teploty["Avg_Celsia"] = pytemperature.f2c(teploty["Avg_Fahrenheit"])
print(teploty.info)

# Teplota z 13. listopadu
den_13 = teploty[teploty["Day"] == 13]
print("Teploty ze 13. listopadu:")
print(den_13)

# Teplota z 13. listopadu v US
den_13_US = teploty[(teploty["Day"] == 13) & (teploty["Country"] == "US")]
print("Teploty 13. listopadu v US:")
print(den_13_US)

# Teplota z 13. listopadu v US - Washington a Philadelphia
den_13_US_mesta = den_13_US[den_13_US["City"].isin(["Washington", "Philadelphia"])]
print("Teploty 13. listopadu v US - Washington a Philadelphia:")
print(den_13_US_mesta[["id", "City", "Avg_Fahrenheit", "Avg_Celsia"]])
print()

# BONUS
# Průměrná teplota v listopadu v US
prumer_US_13 = round(den_13_US["Avg_Celsia"].mean(), 2)
print(f"Průměrná teplota 13. listopadu v US: {prumer_US_13} C")
print()

# Medián - hodnota, která rozděluje seřazený soubor na dvě stejně početné části
median_US_13 = round(den_13_US["Avg_Celsia"].median(), 2)
print(f"Jedna polovina naměřených teplot byla 13. listopadu v US stejná nebo nižší, "
      f"druhá polovina stejná nebo vyšší než: {median_US_13} C")
print()

# Rozptyl a směrodatná odchylka
var_US_13 = round(den_13_US["Avg_Celsia"].var(), 4)
print(f"Rozptyl hodnot výběru je {var_US_13}, směrodatná odchylka: {round(var_US_13**(1/2),2)}")

