def subarrayFinder(arr, k):
    n = len(arr)
    start = 0
    curr_sum = arr[0]
    i = 1
    while i < n - 1:
        if i < n:
            curr_sum += arr[i]
        while curr_sum > k and start < i - 1:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == k:
            return start, i
        i += 1
    print("array notfound")
    return -1


print(subarrayFinder([15, 2, 4, 8, 9, 5, 10, 23], 103))
