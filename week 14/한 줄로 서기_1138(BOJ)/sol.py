import sys
sys.stdin = open("input.txt")

N = int(input())
arr = list(map(int, input().split()))
visited = [0 for _ in range(N)]

for i in range(1, N+1):
    k = arr[i-1]
    cnt = 0
    for j in range(N):
        if cnt == k and visited[j] == 0:
            visited[j] = i
            break
        elif visited[j] == 0:
            cnt += 1

print(*visited)