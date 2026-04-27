records = []
for i in range(3):
    name = input().strip().lower()
    city = input().strip().lower()
    aqi = int(input())
    records.append([name, city, aqi])
search = input().lower()
for r in records:
    if search in r[0]:
        print(r)
for r in records:
    print(r)