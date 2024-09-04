class car():
    def __init__(self,windows,doors,enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype

    def drive(self):
        print(f"the car driven is a {self.enginetype} car")


class electriccar(car):
    def __init__(self,windows,doors,enginetype,is_selfdriving):
        super().__init__(windows,doors,enginetype)
        self.is_selfdriving = is_selfdriving

    def selfdrive(self):
        print(f"The car supports {self.is_selfdriving} feature")


t1 = electriccar(4,5,"electric",True)
t1.drive()
t1.selfdrive()


        