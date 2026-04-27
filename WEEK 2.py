data = []
while True:
    print("1.Add 2.View 3.Exit")
    ch = input()
    if ch == "1":
        name = input()
        aqi = int(input())
        data.append((name, aqi))
    elif ch == "2":
        for i in data:
            print(i)
    elif ch == "3":
        break
    else:
        print("Invalid")