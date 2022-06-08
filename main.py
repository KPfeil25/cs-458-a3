import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gdpData = pd.read_csv('gdps.csv')
gdpData = pd.DataFrame(gdpData)
# print(data)

gdp_countries = gdpData['GEO'].values.tolist()
gdps = gdpData['Value'].values.tolist()
for gdp in gdps:
    gdp = float(gdp)
# print(gdps)

gdpPerCapitaData = pd.read_csv('gdp-per-capitas.csv')
gdpPerCapitaData = pd.DataFrame(gdpPerCapitaData)
# print(gpdPerCapitaData)

gdp_per_capita_countries = gdpPerCapitaData['GEO'].values.tolist()
gdpPerCapitas = gdpPerCapitaData['value'].values.tolist()

# GDP Bar Chart
# plt.bar(countries, gdps)
# plt.title('GDPs of countries')
# plt.xlabel('Country')
# plt.xticks(rotation=90)
# plt.ticklabel_format(axis='y', style='plain', useOffset=False)
# plt.ylabel('GDP')
# plt.show()

# GDP Per Capita Bar Chart
# plt.bar(gdp_per_capita_countries, gdpPerCapitas)
# plt.title('GDP Per Capita, by country')
# plt.xlabel('Country')
# plt.xticks(rotation=90)
# plt.ticklabel_format(axis='y', style='plain', useOffset=False)
# plt.ylabel('GDP Per Capitas')
# plt.show()

# Pie chart for belguims wealth
# goals = np.array([total_home_goals, total_away_goals])
# xG = np.array([total_home_xg, total_away_xg])
labels = np.array(['Top 1%', 'Top 2-5%', 'Top 6-10%', 'Lower 90%'])
values = np.array([12, 19, 13, 56])

plt.style.use('fivethirtyeight')
plt.title("How Belguim's wealth is distributed")
colors = ["#F98866", "#FF420E", "#80BD9E", "#89DA59"]
plt.pie(values, labels=labels, startangle=90, colors=colors)
plt.show()