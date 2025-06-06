### in python a function is a resuble block of code that perform a specific task . you define a function using the def keyword , followed by the function name and parentheses . you can pass data t a function using parameters and a function can return a value using the return statement

##... Example of function :
# def function_name(parameters):
#     return function_name

## .... Parameters and Arguments

# ... paramenters: are variables listed in the function definition 
#..... Arguments are values passed to the function when calling it.
# Example:

# def add(a, b):  # a and b are parameters
#     return a + b

# result = add(2, 3)  # 2 and 3 are arguments

#... Default Paramenters
def greet(name,message="Hello"):
    print(f"{message},{name}!")
    greet("Alice")        # Output: Hello, Alice!
    greet("Bob", "Hi") # Output: Hi , Bob!
