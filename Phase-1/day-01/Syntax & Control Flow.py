"""Ask the user to enter a number.
Tell whether the number is:
Positive
Negative
Zero
Tell whether the number is:
Even
Odd
Print all numbers from 1 up to the entered number using a loop.
Calculate and print the sum of all numbers from 1 to the entered number.

If the user enters a negative number, don't try to do steps 4–5. Instead, print:

"Please enter a positive number."""

number=int(input("Please enter a number: "))
if number > 0:
    print("The number is Positive.")
    if number % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")

    print("Numbers from 1 to", number, ":")
    total_sum = 0
    for i in range(1, number + 1):
        print(i)
        total_sum += i
    print("The sum of all numbers from 1 to", number, "is:", total_sum)

elif number == 0:
    print("The number is Zero.")
    

else:
    print("The number is Negative.")
    print("Please enter a positive number.")
