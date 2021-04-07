<<<<<<< HEAD
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

# Teploty z 13. listopadu - měření ok
den_13 = den_13[den_13["Avg_Fahrenheit"] != -99]
print("Teploty z 13. listopadu - pouze platná měření:")
print(den_13.info)
print()

# Teploty z 13. listopadu - od největšího po nejmenší
den_13 = den_13.sort_values(["Avg_Celsia"], ascending=False)
# Prvních pět - nejvyšší
print(den_13.head())
print()
# Posledních pět - nejnižší
print(den_13.tail())
print()
=======
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

# Teploty z 13. listopadu - měření ok
den_13 = den_13[den_13["Avg_Fahrenheit"] != -99]
print("Teploty z 13. listopadu - pouze platná měření:")
print(den_13.info)
print()

# Teploty z 13. listopadu - od největšího po nejmenší
den_13 = den_13.sort_values(["Avg_Celsia"], ascending=False)
# Prvních pět - nejvyšší
print(den_13.head())
print()
# Posledních pět - nejnižší
print(den_13.tail())
print()
>>>>>>> origin/main
