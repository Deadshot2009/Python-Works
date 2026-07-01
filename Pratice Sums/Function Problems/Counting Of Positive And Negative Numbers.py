a=[5, -2, 10, -7, 3, -9]
def count_negative():
    count1=0
    for numbers1 in a:
        if numbers1<0:
            count1=count1+1
    return count1
print(count_negative())
def count_positive():
    count2=0
    for numbers2 in a:
        if numbers2>0:
            count2=count2+1
    return count2
print(count_positive())
