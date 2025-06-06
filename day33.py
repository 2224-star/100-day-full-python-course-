## a Dictionary is a colletion of key-value pairs Each key must be unique and values can be any type

## Creating a dictionary

person = {
    "name":"kumar",
    "age":24,
    "city":"Madhubani",
    "State":"Bihar"
}
# Accessing Values
print(person) # Output: 'kumar',24,'Mahubani','Bihar'
print("Name:",person["name"]) # Output : 'kumar',
print("Age:",person["age"]) # Output : 24
print("State:",person["State"]) # Output : 'Bihar

## Adding a new key-value pair
person["Email"] = "xyz@gmail.com" # Add the Email 
person["phone"] = 7255636 # Add the Phone Number

# Check It
print(person) # OutPUt: {'name': 'kumar', 'age': 24, 'city': 'Madhubani', 'State': 'Bihar', 'Email': 'xyz@gmail.com', 'phone': 7255636}

# Updating the Value

person["age"] = 90
print("After updading the age:", person) # Output : After updading the age: {'name': 'kumar', 'age': 90, 'city': 'Madhubani', 'State': 'Bihar', 'Email': 
#'xyz@gmail.com', 'phone': 7255636}

# Removing a key-value pair

del person["city"]
print("After Removing the City:",person) ## Output: After Removing the City: {'name': 'kumar', 'age': 90, 'State': 'Bihar', 'Email': 'xyz@gmail.com', 'phone': 7255636}


## Dictionary Methods

print("Keys:", person.keys())
print("Values:",person.values())
print("Items:", person.items())
