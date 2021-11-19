def println(dp):
    for each in dp:
        print(*each)


val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
W = 7
n = len(val)
dp = [[0 for i in range(W + 1)] for j in range(len(wt) + 1)]
# println(dp)

## constructing dp
val.insert(0, 0)
wt.insert(0, 0)
for i in range(1, len(wt)):
    for j in range(1, (W + 1)):
        if wt[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - wt[i]] + val[i], dp[i - 1][j])
println(dp)
print()
maxi = dp[len(wt) - 1][W]
print("Maximum profit:",maxi)
i = len(wt) - 1
while W > 0 and maxi > 0:
    if dp[i - 1][W] == maxi:
        pass
    else:
        print("picked weight is:",wt[i],"profit =>",val[i])
        W -= wt[i]
        maxi -= val[i]
    i -= 1
