import sys
sys.stdin = open("input.txt")
from collections import deque

def knight():
    global cnt
    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [2, -2, 2, -2, 1, -1, 1, -1]
    # 시작점
    q = deque([[sx,sy]])
    while q:
        x,y = q.popleft()
        # 이동하려는 칸 도착시 현재칸 까지 이동횟수 리턴
        if x == lx and y == ly:
            cnt = graph[x][y]

            return graph[x][y]
        # 나이트 이동 방향 탐색
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위 내 있고 탐색 X 탐색
            if 0 <= nx < I and 0 <= ny < I:
                if not graph[nx][ny]:
                    q.append([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1 # 이동횟수 초기화


T = int(input())
for tc in range(1, T+1):
    I = int(input())
    graph = [[0 for _ in range(I)] for _ in range(I)]
    sx, sy = map(int, input().split())
    lx, ly = map(int, input().split())
    cnt = 0
    knight()
    print(cnt)
    # print(graph)