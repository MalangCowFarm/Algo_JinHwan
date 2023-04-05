from collections import deque
import sys
sys.stdin = open("input.txt")

def bfs(x, y):
    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 0, -1, 1, 0, -1, 1]
    arr[x][y] = 0
    q = deque()
    q.append([x, y])
    while q:
        a, b = q.popleft()
        for k in range(8):
            nx = a + dx[k]
            ny = b + dy[k]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append([nx, ny])
            print(arr)

while True:
    k = 0
    cnt = 0
    l = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        arr = [list(map(int, input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)