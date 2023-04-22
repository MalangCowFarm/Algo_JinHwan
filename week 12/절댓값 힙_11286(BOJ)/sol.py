import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
import  heapq
N = int(input())
l = []

for _ in range(N):
    k = int(input())
    if k != 0:
        heapq.heappush(l, (abs(k), k))
    else:
        try:
            print(heapq.heappop(l)[1])
        except:
            print(0)

# for i in range(len(l)):
#     temp = []
#     if l[i] == 0:
#         continue
#     if l[i] != 0:
#         temp[i]
# for i in range(len(l)):
#     if l[i] != 0:
#         u.append(l[i])
#     else:
#         for i in range(len(l)):
#             if l[i] != 0:
#                 u.append(l[i])
#             else:
#                 if len(u) == 0:
#                     print(0)
#                 else:
#                     print(u.pop())
#
