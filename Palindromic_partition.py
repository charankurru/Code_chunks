def partition(s):
    res = []

    def recursive(arr, s):
        if s:
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    recursive(arr + [s[:i]], s[i:])
        elif arr:
            res.append(arr)

    recursive([], s)
    return res


s = input()
if s == s[::-1]:
    mid = len(s) // 2
    print(s[: mid + 1])
else:
    print(partition(s))  # rotor
