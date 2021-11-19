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


print(maxSumFinder([5, -3, -2, 6, -1]))
print(maxSumFinder([-2, -3, 4, -1, -2, 1, 5, -3]))


# using dp
# public int maxSubArray(int[] A) {
#         int n = A.length;
#         int[] dp = new int[n];//dp[i] means the maximum subarray ending with A[i];
#         dp[0] = A[0];
#         int max = dp[0];

#         for(int i = 1; i < n; i++){
#             dp[i] = A[i] + (dp[i - 1] > 0 ? dp[i - 1] : 0);
#             max = Math.max(max, dp[i]);
#         }

#         return max;
# }
