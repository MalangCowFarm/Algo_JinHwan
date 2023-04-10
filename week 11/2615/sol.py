import sys
sys.stdin = open("input.txt")

def dfs(x, y, xcnt, ycnt):
    global result, k, l
    dx = [1, 1, 0, -1]
    dy = [0, 1, 1, -1]
    if arr[x][y] == 1:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 19 and 0 <= nx < 19:
                if xcnt == 5:
                    result = 1
                    k, l = x, y
                    return
                elif arr[nx][ny] == 1:
                    xcnt += 1
                    dfs(nx, ny, xcnt, ycnt)

    elif arr[i][j] == 2:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 19 and 0 <= nx < 19:
                if ycnt == 5:
                    result = 2
                    k, l = x, y
                    return
                elif arr[nx][ny] == 2:
                    ycnt += 1
                    dfs(nx, ny, xcnt, ycnt)





arr = [list(map(int, input().split())) for _ in range(19)]


result = -1
for i in range(19):
    for j in range(19):
        dfs(i, j, 0, 0)
print(result)
print(k, l)