import sys
sys.stdin = open("input.txt")

def dfs(x, y):
    pass

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
visited1 = [[0 for _ in range(N)] for _ in range(N)]
print(visited)
print(visited1)
for i in range(N):
    for j in range(N-1):
        dfs(i, j)

