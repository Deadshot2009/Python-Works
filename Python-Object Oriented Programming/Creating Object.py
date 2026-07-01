class jeevaa:
    name="Tharun"
    age=14
    def my_func(self):
        print(self.name)
        print(self.age)
obj=jeevaa()
obj.name="Govindammal"
obj.age=43
print("Name1 Is",obj.name)
print("Age1 Is",obj.age)
print("Name2 Is",jeevaa.name)
print("Age2 Is",jeevaa.age)
obj.my_func()
