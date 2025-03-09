import sys

n = int(input())
m = int(input())

graph = [[0] * n for _ in range(n)]  # n*n 2차원 배열

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a-1][b-1] == 0:
        graph[a-1][b-1] = c
    else:
        graph[a-1][b-1] = min(graph[a-1][b-1], c)


d = [[0 if i == j else float('inf') for j in range(n)]for i in range(n)]  # n*n 2차원 배열

for i in range(n):
    for j in range(n):
        if graph[i][j] > 0:
            d[i][j] = graph[i][j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])


for i in d:
    for j in i:
        if j == float('inf'):
            print(0, end = " ")
        else:
            print(j, end = " ")
    print("")
