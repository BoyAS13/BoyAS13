weight = input('Weight in kg: ')
height = input('\nHeight in m: ')
try :
    weight = float(weight)
    height = float(height)
except :
    print("\nInvalid value!")
    quit()
if weight <= 0 or height <= 0 :
    print("\nInvalid value!")
else :
    bmi = round(weight / height ** 2, 2)
    if bmi < 18.5 :
        print(f"\nBMI: {bmi}\n\nYou are underweight.")
    elif 18.5 <= bmi < 25 :
        print(f"\nBMI: {bmi}\n\nYou have a normal weight.")
    elif 25 <= bmi < 30 :
        print(f"\nBMI: {bmi}\n\nYou are overweight.")
    elif 30 <= bmi < 35 :
        print(f"\nBMI: {bmi}\n\nYou are obese (class 1).")
    elif 35 <= bmi < 40 :
        print(f"\nBMI: {bmi}\n\nYou are obese (class 2).")
    else :
        print(f"\nBMI: {bmi}\n\nYou are extremely obese.")