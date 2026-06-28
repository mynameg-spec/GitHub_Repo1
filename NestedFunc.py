#Nested functions are functions inside another function

def outer():
    def inner():  #Every function is a object
        print("Inside inner function")

    inner()

outer()

## Returning functions

def outer():
    def inner():  #Every function is a object
        print("Inside inner function")

    return inner

x=outer()
x()
