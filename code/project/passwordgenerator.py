#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = None

print("Welcome to the PyPassword Generator!\n")

nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

for x in range (0, nr_letters):
    x = letters[random.randint(0, 25)]
    if password is None:
        password = x
    else:
        password += x
for y in range(0, nr_numbers):
    y = numbers[random.randint(0, 9)]
    if password is None:
        password = y
    else:
        password += y
for z in range(0, nr_symbols):
    z = symbols[random.randint(0, 8)]
    if password is None:
        password = z
    else:
        password += z
password = ''.join(random.sample(password,len(password)))
print(f'Try the generated password below\n{password}')
print("Thank you for using PyPassword Generator")
