# 🚨 Don't change the code below 👇
from re import A, S


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size in ['L', 'l', 'M', 'm']:
    if size in ['L', 'l']:
        bill = 25
    elif size in ['M', 'm']:
        bill = 20
    if add_pepperoni in ['Y', 'y']:
        bill += 3
elif size in ['S', 's']:
    bill = 15
    if add_pepperoni in [ 'Y', 'y']:
        bill += 2
if extra_cheese in ['Y', 'y']:
    bill += 1
print(f"Your final bill is: ${bill}.")