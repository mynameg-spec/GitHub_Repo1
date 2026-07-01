# Task-5

from functools import reduce
from datetime import datetime

#----------------------------------------------------
# 1. Filter people under 18 and map their names


people = [{"name": "Reena", "age": 20},
          {"name": "Rahul",   "age": 15},
          {"name": "Leena", "age": 25},
          {"name": "Dave", "age": 16}]

adults      = list(filter(lambda p: p["age"] >= 18, people))  # remove under 18
adult_names = list(map(lambda p: p["name"], adults))           # extract names

print("1) Adults names:", adult_names)

#----------------------------------------------------
# 2. Product of all numbers using reduce

numbers = [1, 2, 3, 4, 5]

# reduce keeps multiplying two numbers at a time until one result remains
product = reduce(lambda a, b: a * b, numbers)

print("2) Product:", product)

#----------------------------------------------------
# 3. Squares of even numbers using list comprehension

nums = [1, 2, 3, 4, 5, 6, 7, 8]
is_even = lambda x: x % 2 == 0  # stored in variable

# lambda checks if even, then square it
squares = [n**2 for n in nums if is_even(n) ]

print("3) Squares of even numbers:", squares)

#----------------------------------------------------
# 4. Check if a string is a number

# isnumeric() returns True if all characters are digits
is_number = lambda s: s.isnumeric()

print("4) '123' is number?", is_number("123"))
print("4) 'abc' is number?", is_number("abc"))

#----------------------------------------------------
# 5. Extract year, month, day from datetime

# lambda extracts year, month, day from a datetime object as a tuple
get_date = lambda d: (d.year, d.month, d.day)

# get current date and time
today1 = datetime.now()

# unpack tuple into 3 separate variables
year, month, day = get_date(today1)

print("5) Year:", year, "Month:", month, "Day:", day)

#----------------------------------------------------
# 6. Fibonacci series up to n terms

n = 8           # number of terms
series = [0, 1] # starting list with first two numbers
# lambda adds next fibonacci number to series
add_next = lambda: series.append(series[-1] + series[-2])

count = 2            # start from 2 (already have 2 numbers in series)
while count < n:
    add_next()       # add next fibonacci number
    count += 1

print("Fibonacci series:", series)