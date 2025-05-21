## The String Methods in python 
# # 1. Lower() - converts all characters to lowercase 
Text = "Hello Python Class"
print(Text.lower()) # the output will be "hello python class"
# # 2. Convert the text Upper() - convert all characters to uppercase
Text1 = "hello pthon class"
print(Text.upper()) # the output will be "HELLO PYTHON CLASS"
print(Text) # output will be "hello python class"

## strip () - Removes the leading and trailing whitespaces
print(Text.strip()) # the output will be "Hello python class"

# # 4. Replace() - replace a substring with another substring
print(Text.replace("Hello", "Hi there")) # the output will be " Hi there Python class"
 ## 5. the split () - splits a string into a list of substrings
print(Text.split(" , ")) # the output will be ['Hello', 'Python', 'Class')]

## find() - return the index of the first occurrence of a substring

print(Text.find("Python")) # the output will be 6 

# # the count() - return the number of occurrences of a substring

print(Text.count("2"))  # the output will be 0 

## Startwith() - check if a string starts with a substring
print(Text.startswith("Hi")) 
# the output will be False
print(Text.startswith("Hello"))