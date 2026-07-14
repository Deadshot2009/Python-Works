class ShoppingCart:
    def __init__(self,customer_name,product_name,quantity,price):
        self.customer_name=customer_name
        self.product_name=product_name
        self.quantity=quantity
        self.price=price
    def add_items(self,count):
        self.quantity+=count
        print("Items Added")
    def remove_items(self,count):
        if count<=self.quantity:
            self.quantity-=count
            print("Items Removed")
        else:
            print("Not Enough Items")
    def bill(self):
        total_bill=self.quantity*self.price
        print("Total Bill:",total_bill)
    def display(self):
        print(self.customer_name,self.product_name,self.price,self.quantity)
obj1=ShoppingCart("Jeevaa","Laptop Bag",3,400)
obj1.add_items(2)
obj1.remove_items(1)
obj1.bill()
obj1.display()

    