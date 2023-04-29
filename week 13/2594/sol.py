
import sys
sys.stdin = open("input.txt")

N = int(input())
time = [[600, 600], [1320, 1320]]
for _ in range(N):
    s, e = input().split()
    s = int(s[:2]) * 60 + int(s[2:]) - 10
    e = int(e[:2]) * 60 + int(e[2:]) + 10
    time.append([s, e])
time.sort()

rest = 0
last = 600

for run, stop in time:
    rest = max(rest, run-last)
    last = max(last, stop)

print(rest)
