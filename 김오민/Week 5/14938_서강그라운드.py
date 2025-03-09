import sys

#  지역의 개수 n (1 ≤ n ≤ 100), 수색 범위 m (1 ≤ m ≤ 15), 길의 개수 r (1 ≤ r ≤ 100)
n, m, r = map(int, sys.stdin.readline().split())
item = list(map(int, sys.stdin.readline().split()))

graph = [[0] * n for _ in range(n)]  # n*n 2차원 배열
for _ in range(r):
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a-1][b-1] == 0:
        graph[a-1][b-1] = c
    else:
        graph[a-1][b-1] = min(graph[a-1][b-1], c)

print(graph)

d = [[0 if i == j else float('inf') for j in range(n)]for i in range(n)]  # n*n 2차원 배열

for i in range(n):
    for j in range(n):
        if 0 < graph[i][j]:  # 수색 범위 반영
            d[i][j] = graph[i][j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
print(d)
d = [[0 if x == float('inf') else x for x in row] for row in d]
print(d)
max_item = 0
for start in range(n):
    temp = 0
    for end in range(n):
        if d[start][end] <= m:
            temp += item[end]
    max_item = max(max_item, temp)


print(max_item)



