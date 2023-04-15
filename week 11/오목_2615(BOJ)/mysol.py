import sys
sys.stdin = open("input.txt")


def dfs():
    global cnt
    dx = [0, 1, 1, -1]
    dy = [1, 0, 1, 1]
    for i in range(19):
        for j in range(19):
            if arr[i][j]:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    cnt = 1
                    while 0 <= nx < 19 and 0 <= ny < 19 and arr[i][j] == arr[nx][ny]:
                        cnt += 1
                        if cnt == 5:
                            if 0<=nx+dx[k]<19 and 0<=ny+dy[k]<19 and arr[nx][ny] == arr[nx+dx[k]][ny+dy[k]]:
                                break
                            if 0<=nx-dx[k]<19 and 0<=ny-dy[k]<19 and arr[i][j] == arr[i-dx[k]][j-dy[k]]:
                                break
                            return arr[i][j], i+1, j+1
                        nx += dx[k]
                        ny += dy[k]

    return 0, -1, -1






arr = [list(map(int, input().split())) for _ in range(19)]
cnt = 0


color, x, y = dfs()
if not color:
    print(color)
else:
    print(color)
    print(x, y)


