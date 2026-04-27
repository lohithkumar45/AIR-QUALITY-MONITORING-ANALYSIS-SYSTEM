records = []
ids = set()
for i in range(3):
    rid = i + 1
    name = input()
    city = input()
    aqi = int(input())
    rec = {"id": rid, "name": name, "city": city, "aqi": aqi}
    records.append(rec)
    ids.add(rid)
key = input()
for r in records:
    if r["city"] == key:
        print(r)