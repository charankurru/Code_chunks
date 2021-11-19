#include <bits/stdc++.h>
#define f(i, a, b) for (int i = a; i <= b; i++)
#define rf(i, a, b) for (int i = a; i >= b; i--)
using namespace std;

int n, happiness[100001][4], dp[100001][4];

int MaxHappinessBU()
{
    dp[1][1] = happiness[1][1];
    dp[1][2] = happiness[1][2];
    dp[1][3] = happiness[1][3];
    f(i, 2, n)
    {
        dp[i][1] = happiness[i][1] + min(dp[i - 1][2], dp[i - 1][3]);
        dp[i][2] = happiness[i][2] + min(dp[i - 1][1], dp[i - 1][3]);
        dp[i][3] = happiness[i][3] + min(dp[i - 1][1], dp[i - 1][2]);
    }
    return min(min(dp[n][1], dp[n][2]), dp[n][3]);
}

int main()
{
    int i;
    cin >> n;
    f(i, 1, n) cin >> happiness[i][1] >> happiness[i][2] >> happiness[i][3];
    memset(dp, 10000001, sizeof(dp));
    cout << MaxHappinessBU() << endl;
    return 0;
}