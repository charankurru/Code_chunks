st = "eccbbbbdec"
d = {}
qu = []
for i in range(len(st) - 1, -1, -1):
    if st[i] in d:
        curridx = i
        lastidx = d[st[i]]
        end = -1
        while qu != [] and lastidx >= qu[-1][0]:
            removed = qu.pop(-1)
            end = removed[1]
        qu.append((curridx, end))
    else:
        d[st[i]] = i
        qu.append((i, i))

print(qu)
print(d)
ans = []
for i in range(len(qu) - 1, -1, -1):
    tup = qu[i]
    ans.append(tup[1] - tup[0] + 1)
print(ans)
