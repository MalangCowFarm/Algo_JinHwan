import sys
sys.stdin = open("input.txt")

T = int(input())
kar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sar = [[] for _ in range(T)]
for _ in range(T):
    urr = list(input().split())
    sar[_].append(urr[0])
    sar[_].append(urr[2])

    for i in range(len(urr)+1):
        if sar[_][0] == kar[i]:
            sar[_][0] = i
        if kar[i] == sar[_][1]:
            sar[_][1] = i

N = max(sar[_])
tar = [[] for _ in range(N+1)]



for i in range(N+1):
    tar[i].append(i)
    for k in range(T):
        if tar[i][-1] == sar[k][0]:
            tar[i].append(sar[k][1])




o = int(input())
lar = [[] for _ in range(o)]

for _ in range(o):
    urr = list(input().split())
    lar[_].append(urr[0])
    lar[_].append(urr[2])

    for i in range(len(urr)+1):
        if lar[_][0] == kar[i]:
            lar[_][0] = i
        if kar[i] == lar[_][1]:
            lar[_][1] = i

try:
    for j in range(o):
        if lar[j][1] in tar[lar[j][0]]:
            print('T')
        else:
            print('F')
except TypeError:
    print('F')

