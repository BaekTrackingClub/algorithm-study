import sys
from collections import deque

# 입력 받기
input = sys.stdin.readline
n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]


def bfs(graph):
    # 방문 기록
    log = [[[0, 0] for _ in range(m)] for _ in range(n)]  # log[x][y][wall demolition count]
    log[0][0][0] = 1

    que = deque([(0, 0, 0)])  # 시작 점 (0, 0)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while que:
        x, y, wall = que.popleft()

        if x == n - 1 and y == m - 1:
            return log[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:  # 다음 x, y 값이 범위 내인가?
                # 이동할 수 있는 곳
                if graph[nx][ny] == 0 and log[nx][ny][wall] == 0:
                    que.append((nx, ny, wall))
                    log[nx][ny][wall] = log[x][y][wall] + 1
                # 벽이 있는 곳
                elif graph[nx][ny] == 1 and wall == 0:
                    que.append((nx, ny, 1))
                    log[nx][ny][1] = log[x][y][0] + 1

    return -1


print(bfs(maze))
