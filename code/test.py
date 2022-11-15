txt = input()
letter = input()

txt_counter = 0
ltr_counter = 0

for char in txt:
    txt_counter += 1
    if not letter == char:
        continue
    else:
        ltr_counter += 1
frequency = (ltr_counter/txt_counter)*100

print(int(frequency))