# HW

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



for _ in range(3):
    arr = list(map(int, input().split()))
    print(*quick_sort(arr))