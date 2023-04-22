import sys
sys.stdin = open("input.txt")



def bfs(e):
    q = [e]
    while q:
        x = q.pop(0)
        for i in range(N+1):
            if visited[i][x] == 1:
                k[x].append(i)
                q.append(i)


# T = int(input())
N, K = map(int, input().split())
arr = list(map(int, input().split()))
visited = [[0 for _ in range(N+1)] for _ in range(N+1)]
result = [[0 for _ in range(N+1)] for _ in range(N+1)]
k = [[] for _ in range(N+1)]
res = [[] for _ in range(N+1)]
ro = []
for i in range(K):
    n, m = map(int, input().split())


    visited[n][m] = 1
w = int(input())
# cnt = 0
# for i in range(N+1):
#     if visited[i][w] == 1:
#         cnt += 1
# print(cnt)
for i in range(N+1):
    for j in range(N+1):
        if j == w and visited[i][j] == 1:
            ro.append(i)



bfs(w)
print(k)

# for i in range(N+1):
#     for j in range(len(k[i])):
#
#         print(k[i][j])
#         print(arr[k[i][j]])
# print(result)











# for i in range(N):
#     for j in range(N):
#         if visited[i][j] == 1:
#             pass



