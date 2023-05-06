import sys
sys.stdin = open("input.txt")

N = int(input())
visited = [[0 for _ in range(8)] for _ in range(8)]
for _ in range(8):
    x, y, a, b = map(int, input().split())
    print(x, y, a, b)