#include <bits/stdc++.h>
using namespace std;
int main()
{
    unordered_map<int, int> hash;
    for (int i = 0; i < n; i++)
    {
        if (hash.count(input_no - arr[i]))
        {
            return 1;
        }
        else
            hash[arr[i]] = i;
    }
    return 0;
}