import sys
sys.stdin = open("input.txt")
from collections import deque
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(x, y, cnt):
    global result
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
            arr[nx][ny] = 1
            print(nx, ny)
            print(visited)


def bfs(x, y):
    q = deque([x, y])

    while q:
        x, y = q.popleft()
        print(x, y, end = '')
        for i in range(1, N+1):
            if not visited[i]



        print(arr)






N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

visited = [[0 for _ in range(N)] for _ in range(M)]

result = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            bfs(i, j, 0)

