og = "hackerrank"
ency = "hackerworld"


def subseq(og, ency):
    i = 0
    lastidx = -1
    while i < len(og):
        curr = og[i]
        f = False
        # print(lastidx)
        for j in range(lastidx + 1, len(ency)):
            if ency[j] == curr:
                f = True
                lastidx = j
                break
        if not f:
            return False
        i += 1
    return True


print(subseq(og, ency))
