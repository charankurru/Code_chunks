## isSafe Function
def isSafe(node, col, graph, filled):
    for child in graph[node]:
        if filled[child] == col:
            return False
    return True


## DFS function
def dfs(start, graph, vis, No_colors, filled):
    if start == len(filled):
        print(filled)
        return True
    for i in range(No_colors):
        if isSafe(start, i, graph, filled):
            filled[start] = i
            if dfs(start + 1, graph, vis, No_colors, filled):
                return True
            filled[start] = -1
    return False


## Inputs
nodes = 4
edges = 5
No_colors = 3
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]


## creating an adjacency list
from collections import defaultdict

graph = defaultdict(list)
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
# print(graph)

## essestials
vis = [False] * nodes
filled = [-1] * nodes
colors = [i for i in range(No_colors)]

## calling dfs function
print(dfs(0, graph, vis, No_colors, filled))
