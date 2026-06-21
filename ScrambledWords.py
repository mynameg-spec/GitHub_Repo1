import random

original = ['python', 'javascript', 'guvi','java','automation','pytest','selenium']
print(original)
original=random.choice(list) #java

scrampled=list(original)    #will convert choosen word into the list['j','a','v','a']
random.shuffle(scrampled) #gives shuffled list
scrambled_words=''.join(scrampled) # will give you scrambled word
print(scrambled_words)
