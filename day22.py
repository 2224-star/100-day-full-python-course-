## Break Statement
# ... purpose : Exits the nearest enclosing loop immediately
# .... Use Case: Stop looping when a condition is met
for i in range(1,10):
    i = int(input("Enter the numer of value i:"))
    if i == 5:
        break
    print(i)

    # continue Statement
    #.... Purpose : Skips the rest of current loop iteration and moves to the next one.
    #..... Use case : Skip certain values or conditons

    for r in range (1,10):
        r = int(input("Enter the Value of r : "))
        if r == 5:
            continue # Skip printing when r is 3
        print(r)

    

    