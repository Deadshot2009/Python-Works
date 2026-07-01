numbers=[5, 12, 3,2, 20, 8]
def second_largest(numbers):
    smallest=numbers[0]
    for a in numbers:
        if smallest> a:
            smallest=a

    return smallest
print(second_largest(numbers))
