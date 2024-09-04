#Base class 1
class animal():
    def __init__(self,name):
        self.name = name
    
    def speack(self):
        print("the subclass must implement the method")

#Base class 2
class pet:
    def __init__(self,owner):
        self.owner = owner
#Derived class

class dog(animal,pet):
    def __init__(self,name,owner):
        # one way to call the base class instead of using super()
        animal.__init__(self,name)
        pet.__init__(self,owner)
        
    def speack(self):
        return f"The {self.name} says woof"


dog_instance = dog('shephard','kay')
print(dog_instance.speack())
print(f"The owner of the dog is {dog_instance.owner}")