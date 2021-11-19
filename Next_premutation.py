def next_prem(lst):
    size = len(lst)
    i = j = size - 1
    while i >= 0 and lst[i - 1] >= lst[i]:
        i -= 1
    i = i - 1
    if i <= -1:
        return -1
    while j > 0 and lst[j] <= lst[i]:
        j -= 1
    lst[i], lst[j] = lst[j], lst[i]
    print(i, j)
    res = "".join(lst[: i + 1]) + "".join(list(reversed(lst[i + 1 :])))
    return res if int(res) < 2 ** 31 else -1


num = 123
lst = list(str(num))
print(next_prem(lst))
