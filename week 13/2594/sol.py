
import sys
sys.stdin = open("input.txt")

N = int(input())

arr = [[] for _ in range(N)]
for _ in range(N):
    s, e = input().split()
    s1 = s[:2]
    s2 = s[2:]
    e1 = e[:2]
    e2 = e[2:]
    arr[_].append(int(s1) * 60 + int(s2) - 10)
    arr[_].append(int(e1) * 60 + int(e2) + 10)




print(arr)
a = []
#
# for i in range(N):
#     for j in range(N):
#         if i != j:
#             if arr[i][0] >= arr[j][1]:
#                 a.append(arr[i][0]-arr[j][1])

            print(a)
if arr[0][0]-600 > 0:
    a.append(arr[0][0]-600)
if 1320 - int(arr[N-1][1]) > 0:
    a.append(1320 - arr[N-1][1])

if len(a) != 0:
    res = max(a)
else:
    res = 0

print(res)
