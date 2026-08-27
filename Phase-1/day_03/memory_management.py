def add_number(numbers):
    numbers.append(4)

numbers = [1, 2, 3]

add_number(numbers)

print(numbers)
numbers_copy = numbers.copy()
def add_five(numbers):
    numbers.append(5)
add_five(numbers_copy)
print(numbers)
print(numbers_copy)