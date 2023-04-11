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



N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
result = []
# N //= 2
# N + k, N - K, N, 0
# N == 1 or break
# dfs()
if 0 in arr and 1 in arr:
    while N != 1:
        N //= 2
        for i in range(N):
            for j in range(N):
                if arr[N+i][N+j] == 1:
                    result.append(1)
                else:
                    result.append(0)
                if arr[N-i][N+j] == 1:
                    result.append(1)
                else:
                    result.append(0)
                if arr[N-i][N+j] == 1:
                    result.append(1)
                else:
                    result.append(0)
                if arr[N+i][N-j] == 1:
                    result.append(1)
                else:
                    result.append(0)
else:
    if 0 in arr:
        result.append(0)
    elif 1 in arr:
        result.append(0)
print(result)