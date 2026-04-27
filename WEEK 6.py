class Station:
    def __init__(self, name, city, aqi):
        self.name = name
        self.city = city
        self.aqi = aqi
    def display(self):
        print(self.name, self.city, self.aqi)

s1 = Station(input(), input(), int(input()))
s2 = Station(input(), input(), int(input()))
lst = [s1, s2]
for s in lst:
    s.display()