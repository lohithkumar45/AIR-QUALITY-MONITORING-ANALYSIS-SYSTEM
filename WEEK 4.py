def add_record(lst):
    name = input()
    aqi = int(input())
    lst.append([name, aqi])

def display(lst):
    for i in lst:
        print(i)

def search(lst):
    key = input()
    for i in lst:
        if key in i[0]:
            print(i)

data = []
add_record(data)
add_record(data)
display(data)
search(data)