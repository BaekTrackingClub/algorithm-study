import sys

#  지역의 개수 n (1 ≤ n ≤ 100), 수색 범위 m (1 ≤ m ≤ 15), 길의 개수 r (1 ≤ r ≤ 100)
n, m, r = map(int, sys.stdin.readline().split())
item = list(map(int, sys.stdin.readline().split()))

graph = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for _ in range(r):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c

d = [row[:] for row in graph]

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

max_item = 0
for start in range(n):
    temp = 0
    for end in range(n):
        if d[start][end] <= m:
            temp += item[end]
    max_item = max(max_item, temp)


print(max_item)



