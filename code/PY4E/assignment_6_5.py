text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(' ')
target = text[pos : 30]
print(float(target.lstrip()))