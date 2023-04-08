import sys
sys.stdin = open("input.txt")

n = int(input())
graph = [[1000] * (26) for _ in range(26)]
for _ in range(n):
    arr = input().split(' is ')

    s = ord(arr[0]) - ord('a')
    e = ord(arr[1]) - ord('a')

    graph[s][e] = 1

for i in range(26):
    for j in range(26):
        for k in range(26):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
            if j == k:
                graph[j][k] = False



m = int(input())
for _ in range(m):
    urr = input().split(' is ')
    es = ord(urr[0]) - ord('a')
    se = ord(urr[1]) - ord('a')
    if graph[es][se] != 1000:
        print('T')
    else:
        print('F')