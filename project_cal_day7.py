# Create a calculator capable of performing addition, subtraction, multiplication, and division operations on two numbers.
# The program formats the output in a readable manner.

# Input: Get two numbers from the user
num1 = float(input("Enter first Number: "))
num2 = float(input("Enter the second Number: "))

# Perform operations
Addition = num1 + num2
Subtraction = num1 - num2
Multiplication = num1 * num2

# Handle division carefully to avoid division by zero
if num2 != 0:
    Division = num1 / num2
else:
    Division = "undefined"

# Output: Display results in a readable format
print("\n--- Calculator Results ---")
print(f"Addition of {num1} + {num2} = {Addition}")
print(f"Subtraction of {num1} - {num2} = {Subtraction}")
print(f"Multiplication of {num1} * {num2} = {Multiplication}")
print(f"Division of {num1} / {num2} = {Division}")


 # this is the another methods

# a = 50
# b= 3
# print("the  value of :", a, "+", b, "is", a+b)
# print("the value of :",a, " a-b ", b,"is ",a-b)
# print("The value of :",a, "a*b",b,a*b)