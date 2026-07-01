a=int(input("Enter The Year"))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("The Year is Leap year")
        else:
            print("The Year Is Not leap year")
    else:
        print("The Year Is Leap Year")
else:
    print("The Year is not Leap Year")
