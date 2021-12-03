# N = 5
# boysgiven = 5
# girlsgiven = 2
# res = 0
# from math import factorial


# def comb(tot, curr):
#     val = factorial(tot) // (factorial(curr) * factorial(tot - curr))
#     return val


# for i in range(4, N):
#     res += comb(boysgiven, i) * comb(girlsgiven, N - i)
# print(res)

st = input()
stk = []
for i in range(len(st)):
    if st[i] == "(":
        stk.append("(")
    elif st[i] == ")":
        if stk != [] and stk[-1] == "(":
            stk.pop(-1)
        else:
            stk.append(")")
if len(stk) == 0:
    print(1)
else:
    print(0)
