# Task - 4
# 1. Even - odd List

List=[10,501,22,37,100,999,87,351]
even=[]
odd=[]
for i in List:
    if i%2==0:
      even.append(i)
    else:
       odd.append(i)
print("Even numbers' List", even)
print("Odd numbers' List", odd)
#---------------------------------------
# 2. Prime No.

prime=[]
for n in List:
    if n/1==n and n/n==1 and n>1:
        if n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0:
         prime.append(n)
print("Prime numbers: ", prime)

print("Prime numbers' List", prime)
print("Total prime number/s in the list:\t", len(prime))
#------------------------------------------------
# 3. Happy Numbers count

happy_num = []

for num in List:
    unique = set()  # To detect cycle
    temp = num  # Current number to process

    while True:
        sum = 0

        while temp > 0:
            sum = sum + (temp % 10) ** 2
            temp = temp // 10
        if sum == 1:
            happy_num.append(num)
            #print("Sum is : ", sum, "Happy number : ", num)
            break
        elif sum in unique:
            #print("Not Happy number : ", num)
            break
        else:
            #print("Unique_list: ", unique)
            unique.add(sum)
            temp = sum  # Move to next number for next iteration
            #print("Sum is : ", sum, "Continue checking for number : ", num)

print("Happy numbers: ", happy_num)
print("Total Happy number/s in the list:\t", len(happy_num))
#-------------------------------------------
# 4. sum of 1st and last digit of an integer

num=int(input("Enter a number: "))
# convert integer into string and then define as a list value
k=list(str(num))
# Convert string into integer and then add
print("Sum of 1st and the last number: ",int(k[0])+ int(k[-1]))

#-------------------------------------------
# 5. Make Rs. 10 using coins: 1, 2, 5, 10

ways = []

for ones  in range(11):   # 0 to 10 one-rupee coins
    for twos  in range(6):    # 0 to 5  two-rupee coins
        for fives in range(3):    # 0 to 2  five-rupee coins
            for tens  in range(2):    # 0 or 1  ten-rupee coin
                # Regular number multiplication
                TEN_Rs = 1*ones + 2*twos + 5*fives + 10*tens
                if TEN_Rs == 10:
                    # repeats the item in a list
                    combo = [1]*ones + [2]*twos + [5]*fives + [10]*tens
                    ways.append(combo)
                    print(combo)

print("All ways to make Rs. 10:")
print(ways)
print("Total:", len(ways))

#-------------------------------------------
# 6. Find duplicates from 3 lists.

L1={2,4,5,10}
L2={3,5,6,7}
L3={6,0,1,2}
uniq=(L1.intersection(L2)) # finds duplicate between L1 and L2
uniq.update((L1.intersection(L3))) # finds duplicate between L1 and L3 and updates values
uniq.update((L2.intersection(L3))) # finds duplicate between L2 and L3 and updates values
print("Given lists are: ", L1, L2, L3)
print("Duplicate numbers are: ",uniq)
#-------------------------------------------
# 7. To find non repeating elements from list

numbers = [1, 2, 3, 2, 4, 3, 5]
non_repeating = []

for n in numbers:
    if numbers.count(n) == 1:
        non_repeating.append(n)

print("Given list:", numbers)
print("Non-repeating elements:", non_repeating)

#-------------------------------------------
# 8. Find minimum element in a rotated sorted list

numbers = [14, 18, 21, 24, 3, 5, 9]
minimum = numbers[0] # starts with minimum number: 4

for n in numbers:
    if n < minimum:  # if found number less than starting minimum number,
                     # then assign latest minimum number to minimum
        minimum = n

print("Given list:", numbers)
print("Minimum element:", minimum)
#-------------------------------------------
# 9. Sum of list values is 59

numbers=[10,20,30,9]
total=59
triplet=[]

for i in range( len(numbers) ):
    for j in range(i+1, len(numbers) ):
        for k in range(j+1, len(numbers) ):
            if numbers[i] + numbers[j] + numbers[k] == total:
                triplet=[numbers[i],numbers[j],numbers[k]]

if triplet:
    print("Given List: ",numbers)
    print("Target Value: ",total)
    print("Triplet found: ",triplet)
else:
    print("No triplet found")

#-------------------------------------------
# 10. To Find a sub_list with sum equal to zero

numbers = [4, 2, -3, 1, 6]
found = []

for i in range( len(numbers) ):
    total = 0
    for j in range(i, len(numbers) ):
        total += numbers[j]
        if total == 0:
            for k in range(i, j + 1):
                found.append(numbers[k])

if found:
    print("Given list:", numbers)
    print("Sub-list with sum zero:", found)
else:
    print("No sub-list found with sum zero")





