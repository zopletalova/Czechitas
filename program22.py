import pandas as pd

#import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")
df = pd.read_csv("character-deaths.csv", index_col="Name")

print(df.info)
print(df.columns)

d_hali = df.loc["Hali", "Death Year"]
print(f"Smrt Hali - rok: {int(d_hali)}")

print(df.loc["Gevin Harlaw":"Gillam"])
print()

print(df.loc["Gevin Harlaw":"Gillam","Death Year"])
print()

print(df.loc["Gevin Harlaw":"Gillam","GoT":"DwD"])
