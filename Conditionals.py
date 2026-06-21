# Conditional Statements are used to control the flow of execution in a program based on

# if statement
age = 20
if age >= 18:
    print("You are good")
elif age>=12:
    print("You are too young")
else:
    print("Not enough age ")


# Match case
number = 2

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other number")
        
