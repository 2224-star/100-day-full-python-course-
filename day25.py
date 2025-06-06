### a list in  python is an ordered , mutable collecton items. list can store elements of any thpe (numbers, Strings, other lists, etc).

##.... Creating a list.

# Creating a list
fruits = ['apple','banana','cherry']
print(fruits) # output : ['apple','banana','cherry']

##.... Accessing Elements

# Access by index (Starts at 0)
print(fruits[0]) # output : apple
print(fruits[-1]) # output : Cherry (last item)

## .... modifying a list
fruits.append("Orange" ) # append method use the modifying the current item
print(fruits) # Output: ['apple', 'banana', 'cherry', 'Orange']

## ....  Remove an item
fruits.remove("banana") # output : ['apple','cherry','Orange']
print(fruits)

## .... change an item

fruits[1] = "graps" ## output ['apple','graps', 'orange']
print(fruits)


##... list operations

# Length of list
print(len(fruits))

# loop through list
for fruit in fruits:
    print(fruit)

    



