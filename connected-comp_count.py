nodes = 2
edges = 3
X = 3
edges = [[0, 1]]
# edges = [[0, 1], [1, 2], [1, 3], [3, 4], [5, 6]]
## creating an adjacency list
from collections import defaultdict

graph = defaultdict(list)
for edge in edges:
    graph[edge[0]].append(edge[1])

visited = [False] * (nodes)

comp = []
for i in range(nodes):
    if not visited[i]:
        q = [i]
        res = [i]
        while q != []:
            node = q.pop()
            visited[node] = True
            for child in graph[node]:
                if not visited[child]:
                    q.append(child)
                    res.append(child)
        comp.append(len(res))
print(comp)
comp.sort(reverse=True)
cnt = 0
for i in range(len(comp)):
    if comp[i] <= X:
        cnt += comp[i]
        X -= comp[i]
print(cnt)
