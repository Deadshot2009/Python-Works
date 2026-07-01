numbers=[1, 2, 3, 4, 5, 6]

def even_numbers(numbers):
    total=0
    for a in numbers:
        if a%2==0:
            total=total+a
    return total
x=(even_numbers(numbers))
print(x)
