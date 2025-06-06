# Set in python

# A set in python is an unordered collection of unique immuable elements. sets are useful for 
# for removing duplicate and performing mathemathical set operations like union intersection and dirrence.

# Example:
# s = {1,2,3,4}
# print(s)

# info = {"kumar_Nandan",19,False,5.9,19}
# print(info)

# nandan = set()
# print(type(nandan))
# for value in info:
#     print(value)



# Creating a Set

my_set = {1,2,3,4}

# Adding elements

my_set.add(5)

# Removing elements

my_set.remove(2) # Raise keyError if not found 

my_set.discard(3) # Does not raise error if not found

# set operations 
a = {1,2,3}
b= {3,4,5}

union = a | b # {1,2,4,5,6}
intersection = a & b 