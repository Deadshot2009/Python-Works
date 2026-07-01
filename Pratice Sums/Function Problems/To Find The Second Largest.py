numbers1=[5, 12, 3, 20, 8]
def largest(numbers1):
    larger=numbers1[0]
    for a in numbers1:
        if a>larger:
            larger=a
    return larger

x=(largest(numbers1))
numbers2=[5,12,3,8]
def second_largest(numbers2):
    secondlarger=numbers2[0]
    for b in numbers2:
        if b>secondlarger:
            secondlarger=b
    return secondlarger
y=(second_largest(numbers2))
if x>y:
    print("The Second Largest Is:",y)

