import sys
sys.stdin = open("input.txt")


def dfs(V):
    visited[V] = 1
    print(V, end = ' ')
    for i in range(1, N+1):
        if visited[i] == 0 and arr[V][i] == 1:
            dfs(i)

def bfs(V):
    q = [V]
    visited[V] = 0
    while q:
        V = q.pop(0)
        print(V, end = ' ')
        for i in range(1,N+1):
            if visited[i] == 1 and arr[V][i] == 1:
                q.append(i)
                visited[i] = 0




N, M, V = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1
dfs(V)
print()
bfs(V)
