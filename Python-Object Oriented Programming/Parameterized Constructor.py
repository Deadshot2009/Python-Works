class company:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        
    def show(self):
        print(self.name,self.age,self.salary)
obj1=company("Naveen",23,20000)
obj1.show()
obj2=company("Jeevaa",21,200000)
obj2.show()

#Parametrized Constructor Is Something That Pass The Value To Argument While Calling The Functions 
