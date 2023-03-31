import sys
sys.stdin = open("input.txt")

dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]
def knight(i, j):
    global result, cnt
    i, j = sx, sy
    for k in range(8):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < I and 0 <= ny < I:
            i, j = nx, ny
            if lx == sx and sy == ly:
                cnt = 0
            if arr[nx][ny] != 1:
                if arr[nx][ny] == 2:
                    return result
                else:
                    arr[i][j] = 1
                    cnt += 1
                    result = cnt
                    if result < cnt:
                        continue

T = int(input())
for tc in range(1, T+1):
    I = int(input())
    arr = [[0 for _ in range(I)] for _ in range(I)]
    sx, sy = map(int, input().split())
    lx, ly = map(int, input().split())
    result = 0
    cnt = 0
    knight(sx, sy)
    arr[sx][sy] = 1
    arr[lx][ly] = 2
    print(cnt)

    for x in arr:
        print(x)
    print()
