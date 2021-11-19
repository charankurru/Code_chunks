N = 5
boysgiven = 5
girlsgiven = 2
res = 0
from math import factorial


def comb(tot, curr):
    val = factorial(tot) // (factorial(curr) * factorial(tot - curr))
    return val


for i in range(4, N):
    res += comb(boysgiven, i) * comb(girlsgiven, N - i)
print(res)
