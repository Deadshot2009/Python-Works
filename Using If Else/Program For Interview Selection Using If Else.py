print("\t\t\tGoogle Company")
print("\t\t\tInterview Selection")
a=input("Enter The Name")
b=int(input("Enter The Age"))
if b>18:
    c=input("Enter The City")
    if c=="salem":
        d=input("Enter The Address")
        if d=="ammapet":
            e=input("Enter Your Degree")
            if e=="Bsc Computer":
                f=input("Enter Your Extra Skills")
                if f=="Programming Languages":
                    g=input("Enter Your Known Languages")
                    if g=="tamil , english":
                        h=int(input("Enter Your Experience Years"))
                        if h>5:
                            i=int(input("Enter Your Expected Salary"))
                            if i<15000:
                                print("Name\t\t\t:",a)
                                print("Age\t\t\t:",b)
                                print("City\t\t\t:",c)
                                print("Area\t\t\t:",d)
                                print("Degree\t\t\t:",e)
                                print("Extra Skills\t\t:",f)
                                print("Speaking Langauges\t:",g)
                                print("Experience\t\t:",h)
                                print("Expected Salary\t\t:",i)
                                print("\t\tYour Are Eligible To The Interview")
                            else:
                                print("Your Are Not Eligible Because Of Your Expected Salary")
                        else:
                            print("Your Are Not Eligible Because Of Your Experience Years")
                    else:
                       print("Your Are Not Eligible Because Of Your Languages")
                else:
                    print("Your Are Not Eligible Because Of Your Extra Skills")
            else:
                print("Your Are Not Eligible Because Of Your Degree")
        else:
            print("Your Are Not Eligible Because Of Your Area")
    else:
        print("Your Are Not Eligible Because Of Your City")
else:
    print("Your Are Not Eligible Because Of Your Age")


            
            
            
                
            
            
 
