# key value pair
# ordered, indexed
# mutable

user ={
    "name":"mango",
    "age":28,
    "height":70,
    "weight":90,
    "City":"Delhi"
}

user2={
    "name":["Meena","Charu","Richa","Lina"],
    "age":[28,28,28,28]
}
print(user)  # prints whole dictionary
print(user["name"])
print(user["age"])
print(user["height"])

# Adding and modifying
user["email"]="abc@kyc.com"
print(user)
user["age"]=40

user.pop("height")  # removes height
print(user)

#user.clear()  # empties

# iterating through entire dictionary
for k,v in user.items():
    print(k,v)


# iterating through key dictionary
for k,v in user.keys():
    print(k)

# iterating through value dictionary
for k,v in user.values():
    print(v)




