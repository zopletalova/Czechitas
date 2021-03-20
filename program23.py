import pandas as pd

#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")
DataFrame = pd.read_csv("country_vaccinations.csv")
# print(DataFrame.info)

# Dotaz na vakcinaci v konkrétní den
print("Vakcinace za 10. 3.:")
vakcinace_den = DataFrame[DataFrame["date"] == "2021-03-10"]
print(vakcinace_den[["country", "total_vaccinations"]])

# Dotaz na vakcinaci v konkrétní den - kde víc než mil
print("Kde byla vakcinace 10. 3. vyšší nez milion:")
vakcinace_den_mil = DataFrame[(DataFrame["date"] == "2021-03-10") & (DataFrame["total_vaccinations"] > 1_000_000)]
print(vakcinace_den_mil[["country", "total_vaccinations"]])

# Dotaz na vice nez 100 tis lidi za den
print("Vakcinace za den vyšší nez 100 tisíc:")
vsto_k_den = DataFrame[DataFrame["daily_vaccinations"] > 100_000]
print(vsto_k_den[["country", "daily_vaccinations"]])

# Dotaz na mene nez 100 tis lidi za den
print("Vakcinace za den mensi nez 100 tisic:")
msto_k_den = DataFrame[DataFrame["daily_vaccinations"] < 100_000]
print(msto_k_den[["country", "daily_vaccinations"]])

# BONUS:
# Dotaz na dva dny ve třech státech
dva_dny_staty = DataFrame[(DataFrame["country"].isin(["United Kingdom", "Finland", "Italy"]))
                          & (DataFrame["date"].isin(["2021-03-10", "2021-03-11"]))]
print("Vakcinace za dva dny a dva staty: ")
print(dva_dny_staty[["date", "country", "daily_vaccinations"]])

# Dotaz na týden v Japonsku
dny_japan = DataFrame[(DataFrame["country"] == "Japan")
                      & (DataFrame["date"] >= "2021-03-03") & (DataFrame["date"] <= "2021-03-09")]
print("Denní vakcinace v průběhu týdne - Japonsko: ")
print(dny_japan[["date", "daily_vaccinations"]])
