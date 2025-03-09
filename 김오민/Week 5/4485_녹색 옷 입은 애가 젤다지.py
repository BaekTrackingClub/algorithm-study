import sys
import heapq

count: int = 0

while True:
    n = int(input())
    count += 1
    if n == 0:
        break
    else:
        graph = []
        for _ in range(n):
            graph.append(list(map(int, sys.stdin.readline().split())))
        d = [[float('inf')] * n for _ in range(n)] # 각 칸까지 최소손실
        q = [(0, 0, graph[0][0])]  # (0,0) 에서는 graph[0][0] 도둑루피
        d[0][0] = graph[0][0]

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while q:
            x, y, cost = heapq.heappop(q)

            if d[x][y] < cost:
                continue
            else:
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        exp_cost = cost + graph[nx][ny]
                        if exp_cost < d[nx][ny]:
                            d[nx][ny] = exp_cost
                            heapq.heappush(q, (nx, ny, exp_cost))

    print("Problem %d: %d" %(count, d[n - 1][n - 1]))
