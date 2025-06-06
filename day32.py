## a set in an unordered collection of unique elements.

## Creating a set

# Creating a set 
my_set = {1,2,3,4,5,6}
print("original set:", my_set)

## Adding an element

my_set.add(7)
print("Original Set", my_set)

### Remove an Element

my_set.remove(3)
print("Original set", my_set)

## Checking Membership
print("Is 2 in the Set?", 8 in my_set)

## Set operations
another_set = {4,2,8,5,3}
print("Union",my_set.union(another_set))
print("Intersection:",my_set.intersection(another_set))
print("Difference:",my_set.difference(another_set))