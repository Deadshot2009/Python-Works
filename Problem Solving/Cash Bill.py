a=input("Enter The Name")
b=int(input("Enter The Price"))
c=int(input("Enter The Number Of Quantities"))
d=int(input("Enter The Discount Percentage"))
Total_price=b*c
discount_amt=Total_price*d/100
Final_bill=Total_price-discount_amt
print("\t\t\t\tCash Bill")
print("Name\t\t\t\t:","\t",a)
print("Price\t\t\t\t:","\t",b)
print("Number Of Qty\t\t\t:","\t",c)
print("Discount Percentage\t\t:","\t",d)
print("Total Amount Without Discount\t:","\t",Total_price)
print("discount amount\t\t\t:","\t",discount_amt)
print("Final Bill\t\t\t\t:","\t",Final_bill)
