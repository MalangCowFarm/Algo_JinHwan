import sys
sys.stdin = open("input.txt")

n = int(input())
m = int(input())
INF = 100000000
graph = [[INF  for _ in range(n)]for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in graph:
    for j in range(n):
        if i[j] == INF:
            i[j] = 0
    print(*i)




