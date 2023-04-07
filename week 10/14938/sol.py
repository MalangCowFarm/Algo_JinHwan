import sys
sys.stdin = open("input.txt")

n, m, r = map(int, input().split())
arr = list(map(int, input().split()))
ar = [[1000] * (n+1) for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    ar[a][b] = min(ar[a][b], l)


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                ar[i][j] = 0
            else:
                ar[i][j] = min(ar[i][j], ar[i][k] + ar[k][j])
result = 0
for i in range(len(ar)):
    for j in range(len(ar[i])):
        if 0 < ar[i][j] <= r:
            result += arr[i-1]
            u = j
print(result+arr[u-1])

# for i in range(k)



