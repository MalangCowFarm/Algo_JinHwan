import sys
sys.stdin = open("input.txt")



for _ in range(7):
    w, h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [0] * (h+1)
    ar = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                ar.append(i)
                ar.append(j)

    ark = [[] for _ in range(len(ar)//2)]
    for i in range((len(ar))//2):
        x = ar[i*2]
        y = ar[i*2+1]
        ark[i].append(x)
        ark[i].append(y)
    print(arr)
