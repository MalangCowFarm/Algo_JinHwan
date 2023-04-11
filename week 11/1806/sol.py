import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
k = 0
result = [0] * N
# print(result)

cnt = 0
for i in range(N):
    result[i] = arr[i]
    if result[i] >= M:
        print(1)

for i in range(N-1):
    result[i] += arr[i+1]
    if result[i] >= M:
        print(2)

for








