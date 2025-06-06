# # opration of list

## ... what is a List?
# a list is an ordered , changeable (mutable) collection of items. you can store any type 
# .. of data in a list

#..# basic operation of list

fruits =["apple","banana","cherry"]

###... Accessing elements
print(fruits[0]) # First item: 'apple'
print(fruits[-1]) # Last item: 'cherry'
print(fruits[1]) # Second item : 'banana'


##... Adding an item
fruits.append("Orange") # Output will be: 'apple, 'banana', 'cherry'
print(fruits)


##.. Removing an item
fruits.remove("Orange") # ['apple', 'cherry', 'Orange']
print(fruits) 

### .. changing an item

fruits[1] = "graps"
print(fruits) # ['apple' , 'graps', 'oragen']

### Looping through a list
# for fruit in fruits:
#     print(fruit)

# insert at postion 1 
fruits.insert(1,"banana")
print(fruits)

## .. remove the last item

last = fruits.pop()
print(last)
print(fruits)

#... sort the list
fruits.sort()
print(fruits)

# ...reverse the list
fruits.reverse()
print(fruits)