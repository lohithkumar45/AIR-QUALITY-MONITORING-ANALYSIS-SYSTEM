import matplotlib.pyplot as plt
cities = [input(), input(), input()]
aqi = [int(input()), int(input()), int(input())]
plt.bar(cities, aqi)
plt.xlabel("City")
plt.ylabel("AQI")
plt.title("Air Quality")
plt.show()
plt.hist(aqi)
plt.show()