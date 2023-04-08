import sys
sys.stdin = open("input.txt")

T = int(input())
kar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sar = [[] for _ in range(T)]
graph = [[1e9 for _ in range(26)] for _ in range(26)]
for _ in range(T):
    urr = list(input().split())
    sar[_].append(ord(urr[0])-ord('a'))
    sar[_].append(ord(urr[2])-ord('a'))
    graph[sar[_][0]][sar[_][1]] = 1


for k in range(26):
    for i in range(26):
        for j in range(26):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

o = int(input())
lar = [[] for _ in range(o)]

for _ in range(o):
    urr = list(input().split())
    lar[_].append(ord(urr[0])- ord('a'))
    lar[_].append(ord(urr[2]) - ord('a'))

    if graph[lar[_][0]][lar[_][1]] < 1e9:
        print('T')
    else:
        print('F')
#
