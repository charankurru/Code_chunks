d = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
digits = "234"
size = len(digits)


def rec(i, digits, size):
    arr = []
    if i == size - 1:
        return list(d[digits[i]])
    lst = rec(i + 1, digits, size)
    curr = d[digits[i]]
    for each in curr:
        for ch in lst:
            arr.append(each + ch)
    return arr


print(rec(0, digits, size))
