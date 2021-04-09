import pandas as pd
import matplotlib.pyplot as plt
import pytemperature
#import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
teploty = pd.read_csv("temperature.csv", index_col="Day")
teploty = teploty.rename(columns={"Unnamed: 0": "id", "AvgTemperature": "Avg_Fahrenheit"})
teploty["Avg_Celsia"] = pytemperature.f2c(teploty["Avg_Fahrenheit"])
#print(teploty.info)

#teploty = teploty[teploty["Avg_Fahrenheit"] != -99]

Miami = teploty[teploty["City"] == "Miami Beach"]
podklad = Miami["Avg_Celsia"].to_frame(name="Miami Beach")
podklad.plot( kind='box', whis=[5, 95], title="První město - teploty listopad 2017")
plt.show()

podklad2 = teploty[teploty["City"] == "Helsinki"]["Avg_Celsia"].to_frame(name="Helsinki")
podklad2.plot( kind='box', whis=[5, 95], title="Druhé město - teploty listopad 2017")
plt.show()

podklad3 = teploty[teploty["City"] == "Tokyo"]["Avg_Celsia"].to_frame(name="Tokyo")
podklad3.plot( kind='box', whis=[5, 95], title="Třetí město - teploty listopad 2017")
plt.show()

# Spojím to
podklad["Helsinki"] = podklad2
podklad["Tokyo"] = podklad3
print(podklad)

# Všechny tři dohromady
podklad.plot( kind='box', whis=[5, 95], title="Přehled teplot tří měst")
plt.show()
