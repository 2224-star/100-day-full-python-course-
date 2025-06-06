### for loop with else in pyton

# a for loop can have an else clause the else block  runs only if hte loop completes normally (i.e not interruppted by a break statement)

# Example

numbers = [1,2,3,4,5]
for num in numbers:
    print(num)
else:
    print("loop finished without break")

    ## If you add a break, the else block will not run.

    numbers1 = [1,2,3,4,5]
    for num1 in numbers1:
        print(num1)
        if num1== 3:
            break
        else:
            print("Loop finished without break.")
            