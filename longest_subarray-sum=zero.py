# we are using prefixSum and dictionay to solve this
# Note this can be used to find the longest valid parenthesis


def lenFinder(arr):
    d = {}
    leng = len(arr)
    presum = 0
    maxi = 0
    for i in range(leng):
        presum += arr[i]
        if presum == 0:
            maxi = i + 1
            continue
        if presum in d:
            val = i - d[presum]
            if val > maxi:
                maxi = val
        else:
            d[presum] = i
    print(d)
    return maxi


arr = [1, -1, 3, 2, -2, -8, 1, 7, 10, 23]
print(lenFinder(arr))
