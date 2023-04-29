import sys
sys.stdin = open("input.txt")

def solve(depth):
    global result
    if depth == 11:
        result = max(result, sum(ans))
        return
    for i in range(11):
        if visited[i]:
            continue
        if skill[depth][i]:
            visited[i] = 1
            ans.append(skill[depth][i])
            solve(depth+1)
            ans.pop()
            visited[i] = 0

for tc in range(int(input())):
    skill = [list(map(int, input().split())) for _ in range(11)]

    result = 0
    ans = []
    visited = [0]*12
    solve(0)
    print(result)