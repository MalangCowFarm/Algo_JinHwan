
import sys
sys.stdin = open("input.txt")

kar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


T = int(input())
sar = [[] for _ in range(T)]

for _ in range(T):
    arr = list(input().split())
    sar[_].append(arr[0])
    sar[_].append(arr[2])


    for i in range(len(kar)):
        if sar[_][0] == kar[i]:
            sar[_][0] = i
        if kar[i] == sar[_][1]:
            sar[_][1] = i

    N = max(sar[_])
p = [[] for _ in range(N+1)]
k = [[] for _ in range(N+1)]
for i in range(N+1):
    k[i].append(i)
    p[i].append(i)
visited = [0] * (N+1)

result = 0
def dfs(o):
    global result
    for i in range(N+1):
        if o == N-i:
            return
        for j in range(len(sar)):
            result = k[i+o][0]
            if result == sar[j][0] and visited[o] != 1:
                k[i].append(sar[j][1])
                visited[o] = 1
            result = sar[j][1]
            visited[i] = 0
        dfs(o+1)

dfs(0)

p = []
q = [[] for _ in range(len(k))]
for i in range(len(k)):
    p = sorted(k[i])

    for j in range(len(p)-1):
        if p[j] != p[j+1]:
            q[i].append(p[j])
    q[i].append(p[-1])

#
# o = int(input())
# tar = [[] for _ in range(o)]
#
# for _ in range(o):
#     urr = list(input().split())
#     tar[_].append(urr[0])
#     tar[_].append(urr[2])
#
#     for i in range(len(urr)+1):
#         if tar[_][0] == kar[i]:
#             tar[_][0] = i
#         if kar[i] == tar[_][1]:
#             tar[_][1] = i
#
# for i in range(len(tar)):
#     if tar[i][1] in q[i]:
#         print('T')
#     else:
#         print('F')
#
# #
# #
# #



