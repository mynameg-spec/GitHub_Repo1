# functions are used to reuse the code and easy to maintain, provide clean code, less code.

def greet(name1,name2): # name is the parameter
    print("Hello", name1,name2)

# greet("Gokul")  # Gokul is a argument
# greet("Kokila")
# greet("Monica")

greet("Gayatri","Reena")

# new function

def add(num1,num2):
    print(num1+num2)
    return num1+num2

add(1,2)

##calculate are of rectangle
def area(length,width):
        print("area",length*width)

area(10,5)

#Another function returning the result back to calling place
def add(num1,num2):
    return num1+num2    # send value back

result = add(10,2)
print(result)

# Local variable
# def demo():
#     x=10    # Local variable of function
#     print(x)
#
# demo()

# Global variable
x=100   # Global variable
def demo(   ):
    print(x)

demo()
print(x)
