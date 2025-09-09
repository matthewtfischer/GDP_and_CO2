import pandas as pd
import matplotlib.pyplot as plt
table = pd.read_csv("wdi_small_tidy_2015.csv")
mortality_rate = table["Mortality rate, infant (per 1,000 live births)"]
gdp_per_cap = table["GDP per capita (constant 2010 US$)"]
country_name = table["Country Name"]

plt.plot(mortality_rate, gdp_per_cap)
plt.show()