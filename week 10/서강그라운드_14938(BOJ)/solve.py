import sys
sys.stdin = open("input.txt")

n, m, r = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[10000] * n for _ in range(n)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], l)
    graph[b-1][a-1] = min(graph[b-1][a-1], l)


for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
            if j == k:
                graph[j][k] = False
ans = 0
print(graph)
for i in range(m):
    cnt = 0
    for j in range(m):
        if graph[i][j] <= m:
            cnt += arr[j]
    ans = max(ans, cnt)

print(ans)
