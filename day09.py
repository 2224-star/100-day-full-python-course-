# typecasting in python programming
# # typecasting is the process of converting a variable from one data type to another. This is  useful when you want ot perform operaton between different types ro need a specific type for a function  
# # Example of typeecasting
# # there are two types of typecastin in python 
 # # Implicit typecasting
# # the implicit typecasting in python automatically converts one data type to another when needed.
a= 5 # int
b= 9.8 # float
result = a + b # 
print(result) # now python converts automatically into the floot
print(type(result)) # check the type of result

# # Explicit typecasting 
 # # you can manually convert  one type to another using the functions like int(),float(),str(),etc,
 # int() - converts to integer 
x = "10"
y = int(x) # convert string to integer
print(type(x)) # check the type of x 
print (type(y)) # check the type of y
# float() - converts to float
z = float(x) # convert string to float
print(type(z)) # check the type of z
# str() - converts to string
number = 40
s = str(number) # convert integer to string
print(type(s)) # check the type of s
# common typecasting functions
#> int(): - Converts a value to an integer
#> float():- converts a value to a float
#> str():- converts a value to a string
#> list():- converts a value to a list
#> tuple():- converts a value to a tuple
# # Example of typpecasting
a = 54
b=3
result = a/int(b)
print(result) # now python converts automatically into the float
print(type(result)) # check the type of reuslt
