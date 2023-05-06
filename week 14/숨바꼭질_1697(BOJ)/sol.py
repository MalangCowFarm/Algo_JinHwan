import sys
sys.stdin = open("input.txt")
from collections import deque
N, K = map(int, input().split())
visited = [0 for i in range(100001)]
q = deque()
q.append([N, 0])
while q:
    x, y = q[0][0], q[0][1]
    if x == K:
        break
    q.popleft()
    visited[x] = 1
    if x -1 >= 0 and visited[x-1] == 0:
        q.append([x-1, y+1])
    if x +1 <= 100000 and visited[x+1] == 0:
        q.append([x+1, y +1])
    if x * 2 <= 100000 and visited[x * 2] == 0:
        q.append([x*2, y+1])
print(q[0][1])

