"""def calculate_total(price, quantity):
    total = price * quantity
    return total


price = 100
quantity = 3

total = calculate_total(price, quantity)


print("Total:", total)"""


"""def calculate_discount(price, discount):
    final_price = price - discount
    return final_price


price = 1000
discount = 200

final_price = calculate_discount(price, discount)

print("Final price:", final_price)"""

"""def calculate_total(price, quantity):
    total = price * quantity
    return total   
total = calculate_total(100, 3)
print(total)"""

"""numbers = [2, 4, 7, 8]

total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print("Total:", total)"""

def calculate_total(price, quantity):
    discounted_price = apply_discount(price)
    total = discounted_price * quantity
    return total


def apply_discount(price):
    discount = 100
    return price - discount


price = 1000
quantity = 2

total = calculate_total(price, quantity)

print("Total:", total)






