total = 0
#your code goes here
loop = 5
while loop > 0:
    age = int(input())
    loop -= 1
    if age <= 3:
        continue
    else:
        total += 100
print(total)