a=[5, -2, 10, -7, 3]
def count_positive():
    count=0
    for positive in a:
        if positive>0:
            count=count+1
    return count
x=count_positive()
print(x)
