import sys
sys.stdin = open("input.txt")

# i를 방문안하고 arr[V][i]에 값이 있으면, 탐색하겠다. 탁색이 완료되면 이를 방문처리하고 프린트하겠다.
def dfs(V):
    visited[V] = 1
    print(V, end = ' ')
    for i in range(1, N+1):
        if visited[i] == 0 and arr[V][i] == 1:
            dfs(i)

# dfs과정에서 순환과정에서 다 방문처리가 됨 그렇기에 방문처리가 되어있고 arr에 값이 있으면 방문처리를 취소해줌
# 큐에 값이 있는 동안 bfs는 돌게되는데 위과정에서 i를 추가 후 V에 pop해서 넣어주게 됨으로 마지막에 큐에 값이 없을 수 있다.
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
