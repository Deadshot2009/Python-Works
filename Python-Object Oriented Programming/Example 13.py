class ShoppingAccount:
    def __init__(self,customer_name,wallet_balance,product_name,product_price,is_logged_in):
        self.customer_name=customer_name
        self.wallet_balance=wallet_balance
        self.product_name=product_name
        self.product_price=product_price
        self.is_logged_in=is_logged_in
    def login(self):
        if self.is_logged_in==True:
            print("Already Login")
        else:
            self.is_logged_in=True:
            print("Login Successfully")
    def buy_product(self):
        if self.is_logged_in==False:
            print("Please Login First")
        elif self.wallet_balance>=self.product_price:
            self.wallet_balance-=self.product_price
            print("Purchase Successfully")
        else:
            print("Insufficient Balance")
    def add_money(self,amount):
        if self.is_logged_in==True:
            self.wallet_balance+=amount
            print("Money Added")
        else:
            print("Please Login First")
    def logout(self):
        if self.is_logged_in==True:
            self.is_logged_in=False
            print('Logout Successfully')
        else:
            print("Already Logout")
    def display(self):
        print(self.customer_name,self.wallet_balance,self.product_name,self.product_price,self.is_logged_in)
obj1 = ShoppingAccount("Jeevaa",1500,"Headphones",1200,False)

obj1.login()
obj1.buy_product()
obj1.add_money(500)
obj1.logout()
obj1.display()