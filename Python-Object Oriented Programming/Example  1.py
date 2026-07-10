class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("The Name Is:",self.name)
        print("The Salary Is:",self.salary)
obj=Employee("Jeevaa",25000)
obj.display()