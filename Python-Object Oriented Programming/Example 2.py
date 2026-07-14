class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        area=self.length*self.breadth
        print(area)
    def perimeter(self):
        perimeter=2*(self.length+self.breadth)
        print(perimeter)
obj1=Rectangle(10,5)
obj1.area()
obj1.perimeter()