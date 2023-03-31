import sys
sys.stdin = open("input.txt")

N, K = map(int, input().split())
arr = list(map(int, input().split()))
st = []
cnt = 0
def dfs():
    result = True
    global cnt
    if len(st) == N:
        stan = 500
        for j in st:
            if stan + arr[j-1] - K < 500:
                result = False
            stan = stan + arr[j-1] - K
        if result == True:
            cnt += 1
        return cnt
    for i in range(1, N + 1):
        if i not in st:
            st.append(i)
            dfs()
            st.pop()

dfs()
print(cnt)


