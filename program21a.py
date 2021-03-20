import pandas as pd
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

akcie = pd.read_csv("twlo.csv")

# tady jsem si udělala hezčí id od 1 :-)
akcie = akcie.rename(columns={"Unnamed: 0": "id"})


# prvnich pět a posledních pět řádků
# print(akcie.info)

# počet sloupců
print(f"Počet soupců je: {akcie.shape[1]}")

# poslení řádek
print("Poslední řádek:")
print(akcie.tail(1))

# prvních pět řádků
print("Prvních pět řádků:")
print(akcie.head(n=5))
print(akcie.iloc[:5])

# prvních pět řádků zase jinak :-)
print(akcie[akcie["id"]<6])