import sys
sys.stdin = open("input.txt")

def check(arr):
    answer = 1
    for i in range(N):
        for j in range(1, N):

N = int(input())
arr = [list(input()) for _ in range(N)]













































# def dfs(x, y):
#     pass
#
# N = int(input())
# arr = [list(input()) for _ in range(N)]
# visited = [[0 for _ in range(N)] for _ in range(N)]
# visited1 = [[0 for _ in range(N)] for _ in range(N)]
# print(visited)
# print(visited1)
# i = 0
# k = 0
# while True:
#     cnt = 0
#     s = i
#     e = k
#     start = arr[s][e]
#     # print(start)
#     for j in range(N):
#         if start == arr[s][j]:
#             cnt += 1
#         else:
#             break
#     k += 1
#     if e == N-1:
#         k = 0
#         i += 1
#     if s ==\
#             .N-1 and e == N-1:
#         break
#     print(cnt)
#
# # o = 0
# # p = 0
# # while True:
# #     cnt = 0
# #     s = o
# #     e = p
# #     start = arr[s][e]
# #     print(start)
# #     for j in range(N):
# #         if start == arr[j][e]:
# #             cnt += 1
# #         else:
# #             break
# #     o += 1
# #     if s == N-1:
# #         o = 0
# #         p += 1
# #     if e == N-1 and s == N-1:
# #         break
#     # print(cnt)