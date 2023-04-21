import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
cnt = 0
print(arr)