# Loops are used to execute a block of code repeatedly until
# if condition is satisfied

# For loop - used to iterate over a sequence

# iterating through range of numbers
n=4
for i in range(0,n):
   print(i)

# iterating through tuple, list, set, dictionary
fruits=['apple','banana','orange']
for fruit in fruits:
    print(fruit)

# iterating through string
for letter in "Python":
    print(letter)

#----------------------------------------------
# While loop - is used to repeat a block of code until some condition is met
number=1
while number<=3:    # evaluates the condition: true or false
    print(number)
    number+=1       # process continues until condition is false

## Program for printing the number until user enters 0

num= int(input("Enter a number: "))     # ask user to enter the number

# iterate until the user enters 0
while num!=0:
    print(num)
    num=int(input("Enter a number: "))
print("The end")

#while loop with break statement
while True:
    user_input=input("Enter a name: ")

# terminate the loop when enters END
    if user_input=="End":  # == is comparison
        print("User enter End, so ending")
        break

    print(user_input)

# while loop with continue statement
# continue skip the current iteration and proceeds to next

for j in range(0,5):
    if j==3:
        continue    # to go to next iteration
    print(j)

# Continue in while loop
d=0
while d<6:
    d+=1
    if d==3:
        continue
    print(d)

# # nested loop
# sweets=["Pedha","Laddu","Jalebi"]
# fruits=["apple","banana","orange"]
#
# for s in sweets:
#     for f in fruits:
#         print(s,f)








































