import pandas as pd

#import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")
DataFrame = pd.read_csv("character-deaths.csv", index_col="Name")

print(DataFrame.info)
print(DataFrame.columns)

d_hali = DataFrame.loc["Hali", "Death Year"]
print(f"Smrt Hali - rok: {int(d_hali)}")

print(DataFrame.loc["Gevin Harlaw":"Gillam"])
print()

print(DataFrame.loc["Gevin Harlaw":"Gillam","Death Year"])
print()

print(DataFrame.loc["Gevin Harlaw":"Gillam","GoT":"DwD"])
