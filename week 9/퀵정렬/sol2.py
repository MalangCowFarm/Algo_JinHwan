# 5205

def quick_sort(arr):
    # 분할 정복
    if len(arr) <= 1:
        return arr
    else:
        #분할작업
        pivot = arr[0]
        left, right = [], []
        for i in range(1, len(arr)):
            if arr[i] > pivot:
                right.append(arr[i])
            else:
                left.append(arr[i])
        return [*quick_sort(left), pivot, *quick_sort(right)]

##
T = int(input())
for tc in range(1, T+1):
    arrs = []
    N = int(input())
    arr = list(map(int, input().split()))
    arrs = quick_sort(arr)
    print(f'#{tc} {arrs[len(arrs)//2]}')