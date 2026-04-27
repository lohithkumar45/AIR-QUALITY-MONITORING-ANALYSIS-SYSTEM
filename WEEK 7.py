class Record:
    def __init__(self, id):
        self._id = id

class Station(Record):
    def __init__(self, id, name, aqi):
        super().__init__(id)
        self.name = name
        self.aqi = aqi
    def display(self):
        print(self._id, self.name, self.aqi)

s = Station(1, input(), int(input()))
s.display()