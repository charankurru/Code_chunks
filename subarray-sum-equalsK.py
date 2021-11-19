# index =     0 1 2 3  4 5 6 7
# arr   =     3 4 7 2 -3 1 4 2
# prefix =    3 7 14
# for each ele in prefix array  store it in
# dictionay holding the frequency of each element

# if( cummulativeSum-k) exists in dictionary then a subarray
# of given sum exists so we need to increase the count
#  count = count+d[cummulativeSum-k]


def noOfSubArr(arr, k):
    d = {0: 1}
    c = 0
    summ = 0
    for i in arr:
        summ += i
        if summ - k in d:
            c += d[summ - k]
        d[summ] = d.get(summ, 0) + 1
    return c


nums = [1, 2, 3]
k = 3
print(noOfSubArr(nums, k))
