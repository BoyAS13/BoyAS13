while True:
    weight = input('Weight in kg: ')
    print(weight)
    height = input('\nHeight in m: ')
    print(height)
    try :
        weight = float(weight)
        height = float(height)
        if weight <= 0 or height <= 0 :
            print("\nInvalid value!")
            quit()
        else :
            bmi = round(weight / height ** 2, 2)
            break
    except :
        print("\nInvalid value!")
        quit()
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