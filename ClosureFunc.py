#Closure function is a function that remembers the variables from its outer
# even after outer function has finished executing

def outer():
    message="Welcome"

    def inner():
        print(message) # message variable is not local to inner func, still it can access this variable


    return inner
x=outer()
x()

# Another example
def multiply_by(x):
    print(x)
    def multiply(y):
        print(y)
        return x*y

    return multiply

double=multiply_by(2)   # outer func
double(5)               # inner func