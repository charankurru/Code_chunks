#include <bits/stdc++.h>
using namespace std;
int main()
{
    map<char, int> alpha;
    char ch;
    for (int i = 97; i <= 122; i++)
    {
        ch = i;
        alpha[ch] = i - 96;
    }
    // for (auto each : alpha)
    //     cout << each.first << " " << each.second << endl;

    vector<string> strs = {"cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"};
    // vector<string> strs = {"a", "d", "aaaa"};
    multimap<int, vector<string>> mp;
    for (auto word : strs)
    {
        int value = 0;
        for (auto ch : word)
            value += alpha[ch];
        auto it = mp.equal_range(value);
        bool found = false;
        for (auto itr = it.first; itr != it.second; ++itr)
        {
            string top = itr->second[0];
            sort(top.begin(), top.end());
            string curr = word;
            sort(curr.begin(), curr.end());

            if (top == curr)
            {
                itr->second.push_back(word);
                found = true;
                break;
            }
        }
        if (!found)
        {
            // value is not present in multimap
            vector<string> res;
            // sort(res.begin(), res.end());
            res.push_back(word);
            mp.insert({value, res});
        }
    }
    vector<vector<string>> fin;
    for (auto pr : mp)
    {
        cout << pr.first << " ";
        vector<string> inn;
        for (auto ele : pr.second)
        {
            cout << ele << " ";
            inn.push_back(ele);
        }
        fin.push_back(inn);
        cout << endl;
    }
}