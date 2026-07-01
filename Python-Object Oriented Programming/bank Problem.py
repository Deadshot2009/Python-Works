class bank:
    salary=200000
    incentive=10000
    name="sbi"
    experience="5 years"
    def demo1(self):
        return "Account opening"
    def demo2(self):
        return"Cash Deposit"
    def demo3(self):
        return "Loan Section"
    def add(self,a,b):
        c=a+b
        return c
obj1=bank()
print(obj1.add(10,20))
print(obj1.demo1())
print(obj1.demo2())
print(bank.salary)
