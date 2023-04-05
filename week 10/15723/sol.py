import sys
sys.stdin = open("input.txt")


# alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# K = []
# for i in range(len(alp)):
#     K.append({alp[i]:i})
# print(K)
T = int(input())
sar = [[] for _ in range(T)]
for _ in range(T):
    arr = list(input().split())
    sar[_].append(arr[0])
    sar[_].append(arr[2])

result = []
for i in range(len(sar)):
    for j in range(i, len(sar)-i):
        if sar[i][1] == sar[i+1][0]:
            print(sar[i][1], i, sar[i+1][0], i+1)
        print()


#
#
# R = int(input())
# tar = [[] for _ in range(R)]
# for _ in range(R):
#     arr_ = list(input().split())
