### the if-else statement in python is used to make decisions based on conditions.
#### the Basic syntax of the if-else statement in python 
#> if condition:
#      code to be executed if the condition is true
#> else:
#      code to be run if condition is false

age = int(input("Enter your age: "))
if age >= 14:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Now check the elif (else if) Example
# You can use the elif statement to check multiple conditions in a single if-else statement

number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

# Check if a number is even or odd
num = int(input("Enter another number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")