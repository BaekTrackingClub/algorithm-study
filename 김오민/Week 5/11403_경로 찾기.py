import sys

n = int(input())
d = []
for _ in range(n):
    d.append(list(map(int, sys.stdin.readline().split())))

#플로이드 워셜

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][k] == 1 and d[k][j] == 1:
                d[i][j] = 1

for i in range(n):
    for j in range(n):
        print(d[i][j], end=' ')
    print("")