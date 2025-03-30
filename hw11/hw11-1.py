class Bus:
    def __init__(self, maxseat, maxspeed):
        self.speed = 0
        self.maxseat = maxseat
        self.maxspeed = maxspeed
        self.passengername = [ ]
        self.emptyseat = True
        self.dictseat = {i: None for i in range(1, maxseat + 1)}

    def boarding(self, name):
        if len(self.passengername) < self.maxseat:
            self.passengername.append(name)
            for seat, occupant in self.dictseat():
                if occupant is None:
                    self.dictseat = name
                    break
        else:
            print('Нет свободных мест')

    def alight_passenger(self, name):
        if name in self.passengername:
            self.passengername.remove(name)
            for seat, occupant in self.dictseat.items():
                if occupant == name:
                    self.dictseat[seat] = None
                    break
                    self.check_emptyseat()
        else:
            print("Пассажир не найден!")

    def adjust_speed(self, delta):
        new_speed = self.speed + delta
        if 0 <= new_speed <= self.maxspeed:
                    self.speed = new_speed
        else:
            print("Скорость вне допустимого диапазона!")

    def check_emptyseat(self):
            self.emptyseat_flag = len(self.passengername) < self.maxseat

    def __str__(self):
        return (f"Скорость: {self.speed}, "
                f"Максимальная скорость: {self.maxspeed}, "
                f"Пассажиры: {self.passengername}, "
                f"Свободные места: {self.emptyseat}")


bus = Bus(maxseat=10, maxspeed=80)
bus.boarding("Иванов")
bus.boarding("Петров")
bus.adjust_speed(50)
print(bus)
bus.alight_passenger("Иванов")
print(bus)





