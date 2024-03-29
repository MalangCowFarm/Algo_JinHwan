import sys
sys.stdin = open("input.txt")

# dx = [0, 0, -1, 1, 0]
# dy = [1, -1, 0, 0, 0]
# def cost(x, y):
#     global cnt
#     visited = [[0 for _ in range(N)] for _ in range(N)]
#     result = 0
#     for k in range(5):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
#             result += arr[nx][ny]
#             visited[nx][ny] += 1
#         cnt += 1
#         if cnt > 3:
#             print(result)
#             return result
#
#
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# cnt = 0
# for i in range(N):
#     for j in range(N):
#         cost(i, j)
# 본래 자리를 포함한 4방향에 이미 꽃을 심었다면
# False를 아니면 True를 리턴
def check(a, b):
    for i in range(5):
        x = a + di[i]
        y = b + dj[i]
        if visited[x][y] == 1:
            return False
    return True


def recur(cur):
    global total, answer

    # 꽃을 3개 다 심었을 때 최소 코스트 갱신
    if cur == 3:
        answer = min(answer, total)
        return

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            # 5 공간에 이미 심지 않았다면
            if check(i, j):
                for k in range(5):
                    x = i + di[k]
                    y = j + dj[k]
                    visited[x][y] = 1
                    total += g[x][y]

                recur(cur + 1)

                # 다음 재귀를 위해 초기화
                for k in range(5):
                    x = i + di[k]
                    y = j + dj[k]
                    visited[x][y] = 0
                    total -= g[x][y]


n = int(input())
g = [list(map(int, input().split())) for i in range(n)]

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

visited = [[0] * n for i in range(n)]
answer = 99999999
total = 0
recur(0)
print(answer)
