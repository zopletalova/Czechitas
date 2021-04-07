import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas
import matplotlib.pyplot as plt

twilio = pandas.read_csv("twlo.csv")

print(twilio.head())

# Pro jistotu seřadím podle "data"
twilio = twilio.sort_values(["Date"], ascending=True)

twilio.plot("Date", "Close", color="green")
plt.show()

# Převod na skutečné datum
twilio["Date"] = pandas.to_datetime(twilio["Date"])
# ...a osa x vypadá lépe
twilio.plot("Date", "Close", color="red")
plt.show()

ax = twilio.plot("Date", "Close", color="orange")
ax.set_title("Zavírací cena akcie Twilio v čase")
ax.set_xlabel("Den obchodování na burze")
ax.set_ylabel("Cena v dolarech")
plt.show()