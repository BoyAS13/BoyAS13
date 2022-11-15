largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try :
        num = int(num)
        for x in [num] :
            if smallest is None and largest is None :
                smallest = x
                largest = x
            elif x < smallest :
                smallest = x
            elif x > largest :
                largest = x
    except :
        print("Invalid input")
        continue
print(f"Maximum is {largest}\nMinimum is {smallest}")