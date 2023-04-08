import sys
sys.stdin = open("input.txt")

n, m, r = map(int, input().split())
arr = list(map(int, input().split()))
ar = [[1e9] * n for _ in range(n)]
ans = 0
for _ in range(r):
    a, b, l = map(int, input().split())
    ar[a-1][b-1] = min(ar[a-1][b-1], l)
    ar[b-1][a-1] = min(ar[b-1][a-1], l)



for k in range(n):
    for i in range(n):
        for j in range(n):
            ar[i][j] = min(ar[i][j], ar[i][k] + ar[k][j])
            if i == j:
                ar[i][j] = False


for i in range(n):
    cnt = 0
    for j in range(n):
        if ar[i][j] <= m:
            cnt += arr[j]
    ans = max(ans, cnt)
print(ans)

# for i in range(k)



