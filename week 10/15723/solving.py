import sys
sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):
    arr = input().split('is')
    print(arr)

for i in range(1, T +1):
