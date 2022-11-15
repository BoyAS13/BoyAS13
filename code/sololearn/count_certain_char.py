inp = input()
counter = 0
for word in inp:
    if word == 'a' or word == 'i' or word == 'u' or word == 'e' or word == 'o':
        counter += 1
    else:
        continue
print(counter)