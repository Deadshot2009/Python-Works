a=int(input("Enter The Tamil Mark"))
b=int(input("Enter The English Mark"))
c=int(input("Enter The Maths Mark"))
d=int(input("Enter The Physics Mark"))
e=int(input("Enter The Chemistry Mark"))
f=int(input("Enter The Computer Science Mark"))
if a>b and a>c and a>d and a>e and a>f:
    print("Tamil Mark Is Greater Than All Subjects")
elif b>a and b>c and b>d and b>e and b>f:
    print("English Mark Is Greater Than All Subjects")
elif c>a and c>b and c>d and c>e and c>f:
    print("Maths Mark Is Greater Than All Subjects")
elif d>a and d>b and d>c and d>e and d>f:
    print("Physics Mark Is Greater Than All Subjects")
elif e>a and e>b and e>c and e>d and e>f:
    print("Chemistry Mark Is Greater Than All Subjects")
else:
    print("Computer Science Mark Is Greater Than All Subjects")
