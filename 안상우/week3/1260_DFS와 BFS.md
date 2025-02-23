```python
import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
edges = {}
for _ in range(M):
    e1, e2 = map(int, sys.stdin.readline().split())
    edges.setdefault(e1, []).append(e2)
    edges.setdefault(e2, []).append(e1)

for key in edges:
    edges[key].sort(reverse=True) 

# DFS
stk = [V]
DFS_visited = set()
DFS_res = []
while stk:
    v = stk.pop()
    if v not in DFS_visited:
        DFS_visited.add(v)
        DFS_res.append(v)
        for neighbor in edges.get(v, []):
            if neighbor not in DFS_visited:
                stk.append(neighbor)

print(" ".join(map(str, DFS_res)))

# BFS
que = deque([V])
BFS_visited = {V}
BFS_res = [V]
while que:
    v = que.popleft()
    for neighbor in sorted(edges.get(v, [])):  # Sort for BFS
        if neighbor not in BFS_visited:
            que.append(neighbor)
            BFS_visited.add(neighbor)
            BFS_res.append(neighbor)

print(" ".join(map(str, BFS_res)))
```
