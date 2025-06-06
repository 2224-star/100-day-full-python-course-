### the for loops in python 

## a for loop is used to iterate over a sequence (like a list, tuple, or string) or other  range and exucuet e a 
# block o of code multiple times.
#### basic syntax of a for loop in python
# for variable in sequence:
# loop through a list
names=["Alice", "bob", "Charlie"]
for name in names:
    print(name)
    # loops through a string
for char in "Hello":
        if char == "Hello":
            print("Happy found ")
        else:
            print("not found")
 ### Using the range() function
i = 10
for i in range(5):
     print(i)

     for char in range(4):
          print(char)

          ## sum of number using in a list
        
     numbers= [1,2,3,4,5,6,7,8,9,10]
     total = 0
     for num in numbers:
        total += num
        print("The sum of the numbers is :", total)
          
student = {"name": "Nandan", "age": 20, "grade": "A"}
for key in student:
    print(key, ":", student[key])
for i in range(1, 4):
 for j in range(1, 4):
        print(i, "*", j, "=", i*j)
print("---")
## nested for loop (multiplication table)
for n in range(3):
    print("Number:", n)
else:
    print("Loop finished!")