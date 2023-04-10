import sys
sys.stdin = open("input.txt")


n = int(input())
tree = list(map(int, input().split()))
grow = list(map(int, input().split()))
result = 0
tree += grow
print(tree)


for _ in range(n):
    for i in range(n):
        tree[i] += grow[i]
        if max(tree) == tree[i]:
            o = i
            # max 같을 때 증가량 작은 거 우선적으로 가져가게끔할예정

    result += tree[o]
    tree[o] = 0


print(result)

n = int(input())

hi = list(map(int, input().split()))
ai = list(map(int, input().split()))

arr = []
total = 0

arr = [[hi[i],ai[i]] for i in range(n)]
arr.sort(key = lambda x:x[1]) #  성장속도가 1에 해당하는 값 기준으로 정렬

for i in range(n):
    total += arr[i][0] + arr[i][1] * i

print(total)