## .. The Recursion is when a function call itself. to solfve a smaller part of a problem. it's useful for problems that can 
 ## that can be broken down into similar subproblems , like calculating factorials or traversing trees.

## basic structure of a rexusive function

# 1. Base Case: A Condition that stops the recrsion.
# 2. Recursive case: The function calls itself with a smaller or simpler input.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    print(factorial(7)) 

    # Output : 5040
    

    ### Fibonacci Sequence
    def fibonacci(n):
        if n ==0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
        print(fibonacci(6))
        # Output : 8



        ## Example : Sum of a list

        def sum_list(list):
            if len(list) == 0:
                return 0
            elif len(list) == 1:
                return 1
            else:
                return sum_list[0] + sum_list(list[1:])
            print(sum_list([1,2,3,4,5]))
            # output : 15


            ## Reverse a string:

            def reverse_string(s):
                if len(s) == 0:
                    return  0
                elif len(s) == 1:
                    return 1
                else:
                    return s[-1] + reverse_string(s[-1])
                print(reverse_string("hello"))
                # Output : "Olleh"

                