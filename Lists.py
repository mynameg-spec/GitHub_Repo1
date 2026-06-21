# List- stores collection of items
# dynamic - can increase or decrease
# Mutable - List elements can be changed, updated, added, removed after the list is created
#Ordered - Elements maintained the order in which they are inserted
# index based - 0,1

a=[1,2,3,4,5]
print(a)

b=["apple", "banana", "cherry"]
print(b)

# Another way of creating the lists using constructor
a=list(
    (1,2,3,"Apple")
)
print(a)

b=list("Heena")
print(b)

print(a[1]) # List are always index based, starts from 0
print(a[-1])    # last item

# Adding more items in the list at the end
a.append("Banana")
print(a)

# Adding the items at specific position
a.insert(4,"Peru")
print(a)

# Adding multiple elements to the end of the list
a.extend([3,4,5])
print(a)

# Lists are mutable - elements can be updated with new values
a[4]="cherry"
print(a)

# remove
a.remove(2) # here 2 is element. will remove 1st ocurrence of element
print(a)

# remove element with index
a.pop(3) # removes 3rd index. it returns value because it is a function
print(a)

a.pop() # removes last item if no index specified

# delete at specified index
del a[1]

#Difference between pop and delete
print("Diff")
c=["T",4,6,"U"]
status=c.pop(2)
print(c)
print(status)

# removing all items, deletes complete array
c.clear()
print(c)

# iterating through the list
for  items in a:
    print(items)

#------------

list1=[1,2,3,4,5]
list2=[11,12,13,14,15]
combine= list1+list2
print(combine)

#-------------

#sorting the list
numbers=[2,5,4,1,3]
new_list=sorted(numbers)
print(numbers)
print(new_list)

numbers.sort()  # sorts and overrides the list

# convert tuple into list

numbers=(4,1,3,2)
mylist=list(numbers)




