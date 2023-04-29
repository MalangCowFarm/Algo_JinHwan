import sys
sys.stdin = open("input.txt")


dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

def delta(x, y):
    cnt = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if island[nx][ny] == '.':
                cnt += 1
        else:
            cnt += 1
    if cnt >= 3:
        island1[x][y] = '.'




N, M = map(int, input().split())
island = [list(input()) for _ in range(N)]
island1 = [['.' for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        island1[i][j] = island[i][j]
        if island[i][j] == 'X':
            delta(i, j)
rx = []
ry = []

for i in range(N):
    for j in range(M):
        if island1[i][j] == 'X':
            rx.append(i)
            ry.append(j)

rey = max(ry)
mrey = min(ry)

rex = max(rx)
mrex = min(rx)


for i in range(mrex, rex+1):
    for j in range(mrey, rey+1):
        print(*island1[i][j], end= '')
    print()