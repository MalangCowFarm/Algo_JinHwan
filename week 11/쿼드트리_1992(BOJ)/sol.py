import sys
sys.stdin = open("input.txt")

#
# def dfs():
#     if 0 in arr and 1 in arr:
#         N //= 2
#         for i in range(N):
#             for j in range(N):
#                 arr
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

#
def dfs(x, y, N):
    for i in range(x, x+N):
        for j in range(y, y+N):
            if arr[x][y] != arr[i][j]:
                print('(', end = "")
                dfs(x, y, N//2)
                dfs(x,y+ N//2,N//2)
                dfs(x+N//2, y, N//2)
                dfs(x+N//2, y+N//2, N//2)
                print(')', end = "")
                return

    if arr[x][y] == 1:
        print(1, end = '')
    else:
        print(0, end = '')


dfs(0, 0, N)