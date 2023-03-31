import sys
sys.stdin = open("input.txt")

perm = list(input())
li = ['' for _ in range(len(perm))]
perms = [[] for _ in range(len(perm))]
k = []
# print(perm)
for i in range(len(perm)):
    perms[i].append(perm[i])


end = perms[1][0]

for j in range(len(perm)):
    if end != perms[j][0]:
        li[j] = perms[j][0]
        end = perms[j][0]
    elif end == perms[j][0]:
        li[j] = (perms[j][0] + perms[j+1][0])
        end = perms[j][0] + perms[j+1][0]
        j = j + 2
k.append(li[0][0])
for j in range(len(li)-1):
    if len(li[j]) == 1:
        if li[j] != li[j+1]:
            if int(int((li[j]))%10) != int(li[j+1]):
                k.append(li[j+1])



print(*k)



