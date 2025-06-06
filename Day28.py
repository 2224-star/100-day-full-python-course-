# an f-string (formatted string literal) ia a string that is prefixed with 'f' or 'F'
# and allows for the inclusion of expressions inside curly braces {} that are evaluated at rendertime.
# f-strings provide a way to embed expressions inside string literals, using curly braces {}.
# syntax : 
# name =" Alice"
# age = 20
#greeting = f"Hello,{name}. you are {age} years old."
#print(greeting)

# Example :

name = "Kumar_Nandan"
age = 22
print(f"Hello, {name}. you are {age} years old.")

# output : Hello, Kumar_Nandan. you are 22 years old.

# Example 2:

price = 50.49
quantity = 3
brand  = "Style_Smart"
store_name = "Style_Smart_Store_Malad_Mumbai"
print(f"The total price for {quantity} {brand} items is ${price *quantity:.2f} Store Name: {store_name}")

