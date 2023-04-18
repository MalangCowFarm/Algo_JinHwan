import sys
sys.stdin = open("input.txt")
result = 1e9
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N-8+1):
    for j in range(M-8+1):
        cnt = 0
        cnt1 = 0
        for k in range(8):
            for l in range(8):
                if k % 2 == 0:
                    if l % 2 == 0:
                        if arr[i+k][j+l] == 'B':
                            cnt += 1
                        elif arr[i+k][j+l] == 'W':
                            cnt1 += 1
                    else:
                        if arr[i+k][j+l] == 'W':
                            cnt1 += 1
                        elif arr[i + k][j + l] == 'B':
                            cnt += 1
                elif k % 2 == 1:
                    if l % 2 == 0:
                        if arr[i+k][j+l] == 'W':
                            cnt1 += 1
                        elif arr[i+k][j+l] == 'B':
                            cnt += 1
                    else:
                        if arr[i+k][j+l] == 'B':
                            cnt += 1
                        elif arr[i+k][j+l] == 'W':
                            cnt1 += 1

        print(cnt, cnt1)
        if result > 64-(cnt+cnt1):
            result = 64-(cnt+cnt1)

print(result)
    #































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

