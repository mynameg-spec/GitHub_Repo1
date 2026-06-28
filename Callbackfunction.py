
# WHat is call back function?
# A function that is passed as an argument to another function and is executed later

# def greet():
#     print("Hello Everyone")
# def greet2():
#     print("Good Morning")
#
# def execute(func):  #func=greet
#     func()
#     #processing
#
# execute(greet2)
# execute(greet)

## Example 2
def add(a,b):
    print(a+b)

def subtract(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def calculate(func,a,b):
    print(func(a,b))

calculate(multiply,10,20)










