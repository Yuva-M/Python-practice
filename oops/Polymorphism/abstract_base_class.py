from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(vehicle):
    def start(self):
        return "car started"

class motorcycle(vehicle):
    def start(self):
        return "motorcycle started"
    
def start_vehicle(vehicle):
    print(vehicle.start())

car = car()
motorcycle = motorcycle()

start_vehicle(car)
start_vehicle(motorcycle)
        
        
