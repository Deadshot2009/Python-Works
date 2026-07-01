class company:
    def __init__(self,name):
        self.name=name
        print("Inside Constructor")
        print("Object Initialized")
        
    def show(self):
        print(self.name)
    def __del__(self):
        print("Inside Destructor")
        print("Destroy Object")
obj1=company("Jeevaa")
obj1.show()
#delete object Destructor Is Something That Delete The Object
del obj1
obj.show()
