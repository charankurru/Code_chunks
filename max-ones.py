def msb(num):
    c = 1
    while num != 0:
        c = c << 1
        num = num >> 1
    c = c >> 1
    return c - 1


a = 22
b = 25
maxi = 0
cur = msb(b)
if a == b:
    print(a)
if a <= cur <= b:
    print(cur)
else:
    maxi = 0
    for i in range(a, b + 1):
        curr = bin(i).count("1")
        if curr > maxi:
            maxi = curr
            num = i
    print(num)
