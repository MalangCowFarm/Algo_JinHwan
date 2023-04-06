import sys
sys.stdin = open("input.txt")


n = int(input())
x, y = map(int, input().split())
m = int(input())
arr = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
result = []
for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b]= arr[b][a] = 1


def dfs(V, num):

    num += 1
    visited[V] = 1
    if V == y:
        result.append(num)
    for i in range(1, n+1):
        if visited[i] == 0 and arr[V][i] == 1:
            dfs(i, num)



dfs(x, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)