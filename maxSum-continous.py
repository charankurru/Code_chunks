from sys import maxsize


def maxSumFinder(arr):
    maxi, curr = -maxsize - 1, 0
    for i in range(len(arr)):
        curr += arr[i]
        if curr > maxi:
            maxi = curr
        if curr < 0:
            curr = 0
    return maxi


def minSumFinder(arr):
    mini, curr = maxsize, 0
    for i in range(len(arr)):
        curr += arr[i]
        if curr < mini:
            mini = curr
        if curr > 0:
            curr = 0
    return mini, curr


def maxSum_Circular(arr):
    arrasum = sum(arr)
    print("arrsum is ", arrasum)
    maxi = maxSumFinder(arr)
    mini, curr = minSumFinder(arr)
    if arrasum == curr:
        return maxi
    else:
        return max(maxi, (arrasum - mini))


print(maxSum_Circular([1, -2, 3, -2]))
print(maxSum_Circular([-5, -3, -2, -6, -1]))
