import matplotlib.pyplot as plt

# Sample data
years = [1990, 1995, 2000, 2005, 2010, 2015, 2016, 2017, 2018, 2019, 2020]
india_pop = [873.22, 963.92, 1056.57, 1285.39, 1234.28, 1310.15, 1324.57, 1338.67, 1352.64, 1366.41, 1380.00]
china_pop = [1176.88, 1240.92, 1290.55, 1330.76, 1368.48, 1406.22, 1414.04, 1421.02, 1427.64, 1433.78, 1439.32]
us_pop = [252.12, 265.16, 281.71, 294.99, 309.01, 320.87, 323.01, 325.08, 327.09, 329.06, 331.00]
brazil_pop = [149.00, 162.01, 174.79, 186.12, 195.71, 204.47, 206.16, 207.83, 209.46, 211.04, 212.59]
japan_pop = [124.50, 126.36, 127.52, 128.32, 128.54, 127.98, 127.76, 127.50, 127.20, 126.86, 126.47]

# Line plot
plt.plot(years, india_pop, label='India')
plt.plot(years, china_pop, label='China')
plt.plot(years, us_pop, label='United States')
plt.plot(years, brazil_pop, label='Brazil')
plt.plot(years, japan_pop, label='Japan')

# Add labels and legend
plt.xlabel('Year')
plt.ylabel('Population (in millions)')
plt.title('Population of Countries over Time')
plt.legend()

# Display plot
plt.show()

import matplotlib.pyplot as plt

# Sample data
years = [1990, 1995, 2000, 2005, 2010, 2015, 2016, 2017, 2018, 2019, 2020]
india_pop =[873.22, 963.92, 1056.57, 1285.39, 1234.28, 1310.15, 1324.57, 1338.67, 1352.64, 1366.41, 1380.00]
china_pop = [1176.88, 1240.92, 1290.55, 1330.76, 1368.48, 1406.22, 1414.04, 1421.02, 1427.64, 1433.78, 1439.32]
us_pop = [252.12, 265.16, 281.71, 294.99, 309.01, 320.87, 323.01, 325.08, 327.09, 329.06, 331.00]
brazil_pop = [149.00, 162.01, 174.79, 186.12, 195.71, 204.47, 206.16, 207.83, 209.46, 211.04, 212.59]
japan_pop = [124.50, 126.36, 127.52, 128.32, 128.54, 127.98, 127.76, 127.50, 127.20, 126.86, 126.47]

# Stacked Bar Graph
plt.bar(years, india_pop, label='India')
plt.bar(years, china_pop, bottom=india_pop, label='China')
plt.bar(years, us_pop, bottom=[india_pop[j] + china_pop[j] for j in range(len(years))], label='United States')
plt.bar(years, brazil_pop, bottom=[india_pop[j] + china_pop[j] + us_pop[j] for j in range(len(years))], label='Brazil')
plt.bar(years, japan_pop, bottom=[india_pop[j] + china_pop[j] + us_pop[j] + brazil_pop[j] for j in range(len(years))], label='Japan')

# Add labels and legend
plt.xlabel('Year')
plt.ylabel('Population (in millions)')
plt.title('Population of Countries over Time')
plt.legend()

# Display plot
plt.show()


import matplotlib.pyplot as plt

# Sample data
countries = ['India', 'China', 'United States', 'Brazil', 'Japan']
populations = [1380.00, 1439.32, 331.00, 212.59, 126.47] # in millions
areas = [3287, 9596, 9834, 8515, 377.97] # in thousand sq. km

# Scatter plot
plt.scatter(areas, populations)

# Add labels and legend
plt.xlabel('Geographical Area (in thousand sq. km)')
plt.ylabel('Population (in millions)')
plt.title('Population and Geographical Area of Countries')
for i in range(len(countries)):
    plt.annotate(countries[i], xy=(areas[i], populations[i]), xytext=(5,5), textcoords='offset points')

# Display plot
plt.show()