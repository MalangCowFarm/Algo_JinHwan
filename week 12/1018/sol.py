import sys
sys.stdin = open("input.txt")
<<<<<<< HEAD

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
cnt = 0
print(arr)
=======
result = []
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N-8+1):
    for j in range(M-8+1):
        cnt = 0
        cnt1 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (l+k) % 2 == 0:
                    if arr[k][l] != 'B':
                        cnt += 1
                    if arr[k][l] != 'W':
                        cnt1 += 1
                else:
                    if arr[k][l] != 'W':
                        cnt += 1
                    if arr[k][l] != 'B':
                        cnt1 += 1

        result.append(cnt)
        result.append(cnt1)

print(min(result))





























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

>>>>>>> 91dc3310b103e1d4e8956c36ffd0ebf16d718c01
