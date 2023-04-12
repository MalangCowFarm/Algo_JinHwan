import sys
sys.stdin = open("input.txt")

#
# def dfs():
#     if 0 in arr and 1 in arr:
#         N //= 2
#         for i in range(N):
#             for j in range(N):
#                 arr
#
dx = [0, 1, 0]



N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
result = []

if '0' not in arr:
    print(1)
elif '1' not in arr:
    print(0)