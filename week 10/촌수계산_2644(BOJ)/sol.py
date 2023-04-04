import sys
sys.stdin = open("input.txt")
# 입력값 받는 부분
N = int(input())
A, B = map(int, input().split())
M = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

result = []
####

# 어떤 노드들이 연결되어 있는지 arr라는 인접행렬에 저장
for _ in range(M):
  x, y = map(int, input().split())
  arr[x][y] = arr[y][x] = 1

def dfs(V, num):
  num += 1
  visited[V] = 1
  if V == B:
    result.append(num)
  for i in range(1, N + 1):
    if visited[i] == 0 and arr[V][i] == 1:
      dfs(i, num)
          
dfs(A, 0)
if len(result) == 0:
  print(-1)
else:
  print(result[0]-1)
