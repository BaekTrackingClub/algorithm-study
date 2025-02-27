```python
import sys
from collections import deque
input = sys.stdin.read
commands = input().splitlines()
N, M, V = map(int, commands[0].split()) # N: 정점의 개수, M: 간선의 개수, V: 시작점
adjacent_list = [[] for _ in range(N + 1)] # 인접 리스트
visited = [0] * (N + 1)
result_dfs = []
result_bfs = []
vertice_deque = deque()

for i in range(M): # 인접 리스트 생성
    a, b = map(int, commands[i + 1].split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
  
for i in range(N + 1): # 인접 리스트의 각 행을 오름차순으로 정렬
  adjacent_list[i].sort()

def dfs(start):
  visited[start] = 1
  result_dfs.append(start)
  if adjacent_list[start]:
    for i in adjacent_list[start]:
      if visited[i] == 0:
        dfs(i)

def bfs(start):
  visited[start] = 1
  result_bfs.append(start)
  vertice_deque.append(start)
  while vertice_deque:
    current = vertice_deque.popleft()
    for i in adjacent_list[current]:
      if visited[i] == 0:
        visited[i] = 1
        result_bfs.append(i)
        vertice_deque.append(i)
dfs(V)
visited = [0] * (N + 1)
bfs(V)

print(*result_dfs)
print(*result_bfs)
```
