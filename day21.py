# the while loop in python repeatedly executes a block of code as lon as a given condtion is true.
## the basic syntax of a while loops is:
# while condition:

# Example of a while loop
count = 0
count = int(input("Enter the Number"))
while count <= 5:
    print(count) # print the current value of count
    if count == 3:
        print("count is 3, breaking the loop")
        break
    # if count is 3, break the loop
    count += 1 # Increment the count by 1S



# This is the (Else Clause)

# num = 0
# num = int(input("Enter a number:"))
# while num < 3:
#     print(num)
#     num += 1
# else:
#     print("the loop has ended")


#### 01. Counting Down
# Counting down from 5 to 1 
# num = 5
# while num > 0:
#     print(num)
#     num -= 1
#     print("blast Off!")

    ## the outpur is :
#     5
# blast Off!
# 4
# blast Off!
# 3
# blast Off!
# 2
# blast Off!
# 1
# blast Off!


