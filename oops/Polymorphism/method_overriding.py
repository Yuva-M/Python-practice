class shape():
    def area(self):
        return "The area of the shape"

class rectangle(shape):
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height

class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius

def area_c(shape):
    print(f"the area is {shape.area()}")

rectangle = rectangle(3,4)
circle = circle(4)

area_c(rectangle)
area_c(circle)