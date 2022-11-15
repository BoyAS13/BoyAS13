#your code goes here
while True:
    weight = input('Weight in kg: ')
    height = input('Height in m: ')
    try :
        weight = float(weight)
        height = float(height)
        if weight <= 0 or height <= 0:
            print("Invalid value!")
            continue
        else :
            bmi = weight / height ** 2
            break
    except :
        print("Invalid value!")
        continue
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi <= 30:
    print("Overweight")
else:
    print("Obesity")