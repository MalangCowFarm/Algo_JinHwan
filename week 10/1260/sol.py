import sys
sys.stdin = open("input.txt")




def dfs(a):
    global result
    result.append(a)
    if len(result) == M+1:
        print(*result)
        return

    for i in range(len(ar[a])):
        if ar[a][i] not in result:
            if visited[ar[a][i]] != 1:
                visited[ar[a][i]] = 1
                dfs(ar[a][i])

# def bfs(a):
#     global result
#     result.append(a)
#     if len(result) == M+1:
#         print(*result)
#         return
#     for i in range(len(ar[a])):
#         result.append(ar[a][i])
#         if ar[a][i] not in result:
#             if visited






N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]
result = []
for _ in range(M):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

ar = [[] for _ in range(N+1)]
for i in range(len(arr)):
    arr[i] = sorted(arr[i])
    ar[i] = arr[i]
visited = [0 for _ in range(N+1)]
visited[V] = 1

dfs(V)
