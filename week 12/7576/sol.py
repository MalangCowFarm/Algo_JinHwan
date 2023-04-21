import sys
sys.stdin = open("input.txt")
from collections import deque


def bfs(V):
    visited[V] = 0
    while queue:
        V = queue.pop(0)
        print(V, end = ' ')
        for i in range(1, N+1):
            if visited[i] == 1 and arr[V][i] == 1:
                queue.append(i)
                visited[i] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

visited = [[0 for _ in range(N)] for _ in range(M)]
queue = deque()

result = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            bfs()

