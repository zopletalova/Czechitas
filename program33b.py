import pandas
from dateutil import easter

data = []

for rok in range(1600, 2100):
  datum = easter.easter(rok)
  datum = datum.strftime("%m-%d")
  data.append(datum)

data = pandas.DataFrame(data, columns=["Datum"])
data = data.groupby("Datum").size()

print(data.head())