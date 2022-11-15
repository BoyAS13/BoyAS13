fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    pieces = line.split()
    for x in pieces:
        if not x in lst:
            lst.append(x)
        else:
            continue
lst.sort()
print(lst)