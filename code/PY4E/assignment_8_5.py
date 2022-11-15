fn = input("Enter file name: ")
fh = open(fn)
counter = 0
lst = list()
for line in fh:
    if not line.startswith("From ") :
        continue
    else :
        lst.append(line.split())
for x in lst:
    counter += 1
    print(x[1])
print("There were", counter, "lines in the file with From as the first word")