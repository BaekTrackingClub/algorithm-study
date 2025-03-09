#다익스트라

import sys
import heapq

v, e = map(int, input().split())  # v - 정점의 개수 e - 간선의 개수
k = int(input())  # 시작 정점

graph = [[] for _ in range(v+1)]
for _ in range(e):
    u_temp, v_temp, w_temp = map(int, sys.stdin.readline().split())  # u에서 v로 가는 w길이 간선
    graph[u_temp].append((v_temp, w_temp))

d = [float('inf')] * (v+1)  # 출발 노드로부터 최단거리 저장할 배열
d [k] = 0  # 출발 노드에는 0, 아닌 노드에는 inf


q = []
heapq.heappush(q, (0, k))  # 시작 정점 k 첫 비용은 0

while q:
    distance, current = heapq.heappop(q)
    if d[current] < distance:
        continue
    for v_temp, w_temp in graph[current]:
        cost = distance + w_temp
        if cost < d[v_temp]:
            d[v_temp] = cost
            heapq.heappush(q, (cost, v_temp))


for i in range(1, v + 1):
    if d[i] == float('inf'):
        print("INF")
    else:
        print(d[i])




