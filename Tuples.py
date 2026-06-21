# ordered - Elements maintain the order in which they are inserted
# immutable - Elements cannot be edited, added, deleted after its creation
# index based
# round brackets
# allows duplicates

fruits=('apple','banana','mango')
print(fruits)
print(len(fruits))
print(fruits[1])

#fruits[1]="Cherry" # Tuple is immutable

# iterating though tuple
for f in fruits:
    print(f)

count=fruits.count('apple')  # count is how many occurrence of items
print(count)

# we cannot delete elements of tuple, but tuple can be deleted
# del fruits

index = fruits.index('mango')













