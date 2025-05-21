# In Python, variables are created to store data, and data types define the type of data a variable can hold. Here's a quick overview:

# VARIABLES:
# 1. Variables are created when you assign a value to them.
# 2. You don't need to declare the type explicitly; Python infers it automatically.

# Example:
name = "Nandan"  # String
age = 20         # Integer
height = 6.9     # Float
is_student = True  # Boolean

print("The type of name is", type(name))
print("The type of age is", type(age))
print("The type of height is", type(height))
print("The type of is_student is", type(is_student))

# DATA TYPES:
# a. Numeric types:
# int: Integer numbers (e.g., whole numbers like 10, -5)
# float: Decimal numbers (e.g., 1.9, -0.5)
# complex: Complex numbers (e.g., 3+5j)

# Example:
a = 30  # int
b = 3.5  # float
c = complex(3, 5)  # complex (3 + 5j)

print("The type of a is", type(a))
print("The type of b is", type(b))
print("The type of c is", type(c))

# b. Text types of data:
# > str: String (sequence of characters)

# Example:
greeting = "Hello, Kumar_Nandan"
print("The type of greeting is", type(greeting))

# c. Sequence Data Types:
# > There are several sequence data types in Python, including:
# - list: Ordered, mutable collection of items (e.g., [1, 2, 3])
# - tuple: Ordered, immutable collection of items (e.g., (1, 2, 3))
# - range: Sequence of numbers (e.g., range(5))

# Example:
fruits = ["lichi", "apple", "banana", "cherry"]  # This is an example of a list
print("The type of fruits is", type(fruits))

coordinates = (30, 20)  # This is an example of a tuple
print("The type of coordinates is", type(coordinates))

# d. Mapping type:
# > dict: Key-value pairs

person = {"name": "kumar_nandan", "age": 20}
print("The type of person is", type(person))
print(person)