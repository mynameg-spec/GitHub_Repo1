#printing Hello to console
from tkinter.constants import NUMERIC

print("Hello")

a=3
print(a)
MyName="Gayatri"
print(MyName)

a, c, d=5, 6.4, "Great"

print(type(a))  # data type of a
print(type(c))
print(type(d))

print(MyName+" "+d) # Concat 2 strings vars

print(a+c) #adding 2 integers

#print (a+d) # gives error due to different datatypes

print(str(a)+d)

# Data types tells us whst kind of value will be stored in a variable
# NUMERIC -Integers, float, complex num
# dictionary
# boolean
# set
# sequence - string, Tuple, list

# numeric
a=5
b=2.4
c=2+4j   # complex
d="Gayatri"

print(type(c))

# finding 1st latter of string

print(d[0])     # 1st letter G
print(d[-1])    #last letter i

# List
grocery=["milk","Dal","Eggs"]
print(grocery)

# Tuple - ordered and immutable (Cannor be modified)
GroceryTuple=["milk","Dal","Eggs",1]
print(GroceryTuple)

#boolean - True - False
print(type(True))

#set - unordered and mutable collection of items
s1={"a","b","c"}
print(s1)
print(type(s1))

#Dictionary - used to store key-value pair
d={12:'Pune', 14:'Hydrabad', 11:'Mumbai'}
print(d)