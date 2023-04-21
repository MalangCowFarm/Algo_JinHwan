import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
lst = list(map(int,input().split()))


ans = n+1
sm = 0
end = 0

# start 증가시키며 반복
for start in range(n):
    while sm<m and end<n:
        sm += lst[end]
        end += 1
    # 부분합이 m일때 cnt+=1
    if sm >= m:
        if len(lst[start:end]) < ans:
            ans = len(lst[start:end])
        sm -= lst[start]

if ans == n+1:
    print(0)
else:
    print(ans)