import pandas as pd
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

akcie = pd.read_csv("twlo.csv")

pocet_radku = akcie.shape[0]
print(f"Pocet radku: {pocet_radku}")
print()

nejstarsi_close = akcie.iloc[0]["Close"]
nejnovejsi_close = akcie.iloc[pocet_radku-1]["Close"]

#first = df.iloc[0,-1] , kde prvni je index prvniho radku a pak staci -1
#pro posledni sloupec, obdobne pro posledni hodnotu posledniho sloupce -> last = df.iloc[-1,-1]

print(f"Nejstarsi Close: {round(nejstarsi_close,2)} // Nejnovejsi Close: {round(nejnovejsi_close,2)}")
print(f"Zmena v procentech je: {round((nejnovejsi_close/nejstarsi_close-1)*100,2)}")
print()


# Nevim, jestli jsem spravne pochopila, jak mam pouzit iloc
dno = min(akcie.iloc[:]["Low"])
strop = max(akcie.iloc[:]["High"])
print(f"Nejnizsi hodnota (s iloc): {dno}")
print(f"Nejvyssi hodnota (s iloc): {strop}")
print(f"Price-range (s iloc): {strop-dno}.")
print()

# Rikala jsem si,ze to musi jit i jinak a ono jo:
dno = akcie["Low"].min()
strop = akcie["High"].max()
print(f"Nejnizsi hodnota: {dno}")
print(f"Nejvyssi hodnota: {strop}")
print(f"Price-range: {strop-dno}.")