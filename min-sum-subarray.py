from sys import maxsize


def minSumFinder(arr):
    mini, curr = maxsize, 0
    for i in range(len(arr)):
        curr += arr[i]
        if curr < mini:
            mini = curr
        if curr > 0:
            curr = 0
    return mini


print(minSumFinder([5, -3, -2, 6, -1]))
