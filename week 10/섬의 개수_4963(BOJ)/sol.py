from collections import deque
import sys
sys.stdin = open("input.txt")

def bfs(x, y):
    # 대각선 까지 8방향 순회
    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 0, -1, 1, 0, -1, 1]
    q = deque()
    q.append([x, y])
    arr[x][y] = 0
    while q:
        # bfs기에 q에 값을 빼서 x,y에 넣어줌 (값이 초기화되는 것을 방지)  1일 때 조사하기로 하였고 섬에 중복 조회를 막기위해 arr에 방문처리(0으로 변환)
        x, y = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                q.append([nx, ny])
                arr[nx][ny] = 0


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