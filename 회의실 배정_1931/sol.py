import sys
sys.stdin = open("input.txt")

T = int(input())
arr = []

for _ in range(T):

    st, lt = map(int, input().split())
    arr.append([st, lt])

arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])

cnt = 0
end = 0

for i,j in arr:
    print(i, j)
    if i >= end:
        cnt += 1
        end = j

print(cnt)




#     arr.sort(key = lambda x : x[0])
#     arr.sort(key = lambda x : x[1])
#
#
# cnt = 1
# end = arr[0][1]
# for i in range(1, T):
#     if arr[i][0] >= end:
#         cnt += 1
#         end = arr[i][1]
#
# print(cnt)

