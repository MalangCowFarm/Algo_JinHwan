import sys
sys.stdin = open("input.txt")
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x: x[0])
print(arr)
start, end = arr[0][0], arr[0][1]
result = 0
if len(arr) > 1:
    for a, b in arr[1:]:
        if end < b:
            if end < a:
                result += end - start
                start = a
            end = b
    result += end - start
else:
    result = end - start
print(result)