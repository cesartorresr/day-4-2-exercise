# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_items = len(names)
random = random.randint(0, num_items - 1)
person_who_pay = names[random]
print(person_who_pay +" is going to pay the bills")


