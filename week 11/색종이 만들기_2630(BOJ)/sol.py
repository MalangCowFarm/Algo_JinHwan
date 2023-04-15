import sys
sys.stdin = open("input.txt")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
wcnt = 0
bcnt = 0
def dfs(x, y, n):
    global wcnt, bcnt
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[x][y] != arr[i][j]:
                dfs(x, y+n//2, n//2)
                dfs(x+n//2, y, n//2)
                dfs(x+n//2, y+n//2, n//2)
                dfs(x, y, n//2)
                return

    if arr[x][y] == 0:
        wcnt += 1
    elif arr[x][y] == 1:
        bcnt += 1

dfs(0, 0, n)
print(wcnt)
print(bcnt)