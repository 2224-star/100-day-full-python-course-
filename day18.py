## The match -case statement in python (introduced in python i s similar to switch-case statemnt in other languages it allows you to compare a value against serva patterns and execute code based on wich pattern matches


x = int(input("Enter the value of x:"))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _ if x != 90:
        print("x is not 90")
    case _ if x != 80:
        print(x, "is not 80")
    case _:
        print(x)