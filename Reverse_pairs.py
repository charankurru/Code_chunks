"""This problem is based on Inversion Count which uses merge sort techniqueu"""


class solution:
    def __init__(self):
        self.count = 0

    # Counting the pairs
    def merge(self, left, right):
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] > 2 * right[r]:
                self.count += len(left[l:])
                r += 1
            else:
                l += 1
        # merging the left and right side
        res = []
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] > right[r]:
                res.append(right[r])
                r += 1
            else:
                res.append(left[l])
                l += 1

        # when left elements remained
        while l < len(left):
            res.append(left[l])
            l += 1

        # when right elements remained
        while r < len(right):
            res.append(right[r])
            r += 1
        return res

    def merge_sort(self, nums):
        if len(nums) == 1:
            return nums
        return self.merge(
            self.merge_sort(nums[: len(nums) // 2]),
            self.merge_sort(nums[len(nums) // 2 :]),
        )


s = solution()
nums = [2, 4, 3, 5, 1]
print(s.merge_sort(nums))
print(s.count)

# def merge(left,right):
#     l,r=0,0
#     count = 0
#     while l<len(left) and r<len(right):
#         if left[l]>2*right[r]:
#             count+=len(left[l:])
#             r+=1
#         else:
#             l+=1
#     return count
# print(merge([40],[12]))
