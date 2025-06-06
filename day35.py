## Exception handling in python is done using the try, except , else, and finally blocks, This 
# allows you to handle errors gracefully without stopping the program.

### Example of Exception Handling
try:
    # code that might raise an exception
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("No Exception occured.")
finally:
    print("This will always execute.")

try:
    x = int(input("Enter Number"))
    print(("you Enter :", x))
except ValueError:
    print("Invalid Input")
else:
    print("No error Occured")
finally:
    print("This runs no matter what")

    ## Handling Multiple Exception
try:
    num = int(input("Enter a number:"))
    result = 10/num
except ValueError:
    print("you must enter a valid integer.")
except ValueError:
    print("you cannot divide by zero,")
else:
    print("Result is:", result)
finally:
    print("Execution completed.")

        