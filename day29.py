# in Python , a docstring (documentation string) is a special string used ot describe what a 
# function , class or module does it helps other ( and your future self ) understand your code


# use the and Write the Docstring  

# Place it as the first statement inside a function, class, or module.

# use triple quotes to write a docstring

# Example :

def add(a,b):

    """ 
    Add the numbers a and b. and return the result. 
    Args:
    a(int or float): The first number .
    b (int or float): The second number 
    Returns:
    int or float : the sum of a and b """
    return a+b
print(add(2,3)) # Output: 5
def multiply(a,b):
    """
    Multiply the numbers a and b and return the result.
    Args:
    a (int or float): The first number.
    b (int or float): The second number.
    Returns:
    int or float: the product of a and b."""
    return a * b
print(multiply(2,5)) # output:10
