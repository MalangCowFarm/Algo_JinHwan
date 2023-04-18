import sys
sys.stdin = open("input.txt")


dx = [0, 2, 4, 6]
dy = [1, 3, 5, 7]
def dfs(x, y):
    cnt = 0
    global bres, wres, result
    for k in range(i, i+8):
        wcnt = 0
        bcnt = 0
        for o in range(4):
            nx = j + dx[o]
            ny = j + dy[o]
            if 0 <= nx < M and 0 <= ny < M:

                if arr[k][nx] != arr[k][y]:
                    bcnt += 1
                if arr[k][ny] != arr[k][y+1]:
                    wcnt += 1

        if arr[k][nx] != arr[k][ny]:
            cnt += wcnt
            cnt += bcnt
#
        # print(cnt)
    #
    # print(cnt)
        if cnt > result:
            result = cnt
    # print(result)








N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
result = 0
arrk = [[0] for _ in range(8) for _ in range(8)]
bres = 0
wres = 0
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        dfs(i, j)





# if result == 0:
#     result = 0
print(result)



























# for i in range(N-8+1):
#     for j in range(M-8+1):
#         bcnt = 0
#         wcnt = 0
#         for k in range(i, i+8):
#             for l in range(j, j+8):
#                 print(k, l)
#                 if arr[k][l] == 'B':
#                     bcnt += 1
#                 elif arr[k][l] == 'W':
#                     wcnt += 1
#         print(bcnt, wcnt)
#         if abs(bcnt-wcnt) < result:
#             result = abs(bcnt-wcnt)
#             print(k, l)
#             arrk[i].append(arr[k][l])
# print(result)
# print(arrk)

