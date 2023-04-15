import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = 0
res = 1e19
result = arr[0]
cnt = 2


while True:
    if result < M and e != N-1:
        e += 1
        result += arr[e]
        cnt += 1
    elif result >= M:
        result -= arr[s]
        s += 1
        cnt -= 1
        if res > cnt:
            res = cnt

    if e == N-1 and result < M:
        break



if res == 1e19:
    print(0)
else:
    print(res)

#_____________________________________________________________________________
# 틀린 식
N, M = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = 0
res = 1e19
result = arr[0]
cnt = 2



if sum(arr) == M:
    res = N
    for i in arr:
        if i >= M:
            res = 1
else:
    while s < N-1 and e < N-1:
        if result < M:
            e += 1
            result += arr[e]
            cnt += 1
        elif result >= M:
            result -= arr[s]
            s += 1
            cnt -= 1
            if res > cnt:
                res = cnt




if res == 1e19:
    print(0)
else:
    print(res)

