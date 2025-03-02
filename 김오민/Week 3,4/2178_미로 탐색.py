import sys
from collections import deque

#입력 받기
input = sys.stdin.readline
n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]



def bfs(graph):
    # 방문 기록
    log = [[0] * m for _ in range(n)]
    log[0][0] = 1

    que = deque([(0,0)]) # 시작 점 (0, 0)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while que:
        x, y = que.popleft()

        if x == n - 1 and y == m - 1:
            return log[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and log[nx][ny] == 0:
                que.append((nx,ny))
                log[nx][ny] = log[x][y] + 1

print(bfs(maze))


