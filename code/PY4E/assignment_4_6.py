def computepay(h, r):
    if h > 40 :
        hour = 40 * r
        overtime = (h - 40) * (r * 1.5)
        p = hour + overtime
        return p
    else :
        p = 40 * r
        return p
h = input("Enter Hours:")
r = input("Enter rate:")
p = computepay(int(h), float(r))
print("Pay", p)