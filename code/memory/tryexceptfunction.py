number = input("Input the number\n")
try :
    number = int(number)
except :
    number = -1
if number > 0 :
    print("Noice!")
else :
    print("Not a number")