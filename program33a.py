import wget
import pandas as pd
import matplotlib.pyplot as plt

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")

velikonoce = pd.read_csv("velikonoce.csv")

#print(velikonoce.head())

ax = velikonoce.plot(x ="Datum", kind="bar", color="green")
ax.set_title("Velikonoce 1600 až 2100")
ax.set_xlabel("Den v roce")
ax.set_ylabel("Počet dnů")
plt.show()