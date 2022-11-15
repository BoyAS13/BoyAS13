# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
tot = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else :
        count += 1
        data = line.rstrip()[line.find('0') : 30]
        tot = tot + float(data)
avg = tot / count

print(f'Average spam confidence: {avg}')