## check if a number is ever or odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
     ## check the grade 
    marks = int(input("Enter your marks:"))
    if marks >=90:
        print("Grade A")
    elif marks >=80:
        print("Grade B")
    elif marks >=70:
        print("Grade C")
    elif marks >=60:
        print("Grade D")
    elif marks >=60:
        print("Grade E")
    elif marks >=50:
        print("Grade F")
    elif marks >=40:
        print("Grade G")
    elif marks >=30:
        print("Grade your are the time pass the coding")
    else:
        print("Greade Wow kiya marks hai lale lagta hai share ka bhaw niche ja raha hai")

        ### the Largest number of three numbers
        a = int(input("Enter first number:"))
        b= int (input("Enter second number:"))
        c = int(input("Enter third number:"))
        if a>=b and a>=c:
            print("The Largest number is:", a)
        elif b>=a and b>=c:
            print("The Largest number is:",b)
        elif a==b and a==c:
            print("All numbers are equal")
            
        else:
            print("The Largest number is:",c)
        
        