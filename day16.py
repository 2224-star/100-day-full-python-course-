## Check if a character is a vowel or consonant
char = input("Enter a character:")
if char.lower() in "aeiou":
    print("The character is a vowel.")
else:
    print("The character is a consonant.")

    ## simple Login system
    username = input("Enter your username:")
    password = input("Enter your password:")
    if username == "Sharekhan" and password == "1234":
        print("Login Sucessful!")
    else:
        print("invalid Creadentials.")