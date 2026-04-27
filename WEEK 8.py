import json
data = []
for i in range(2):
    name = input()
    aqi = int(input())
    data.append({"name": name, "aqi": aqi})
with open("air.json", "w") as f:
    json.dump(data, f)
with open("air.json", "r") as f:
    d = json.load(f)
for i in d:
    print(i)