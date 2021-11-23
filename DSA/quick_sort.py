

def partition(arr, lb, ub):
    pivot = arr[lb]
    start = lb
    end = ub

    while start < end:
        while arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
    temp = arr[lb]
    arr[lb] = arr[end]
    arr[end] = temp

    return end


def quick_sort(arr, lb, ub):
    if lb < ub:
        loc = partition(arr, lb, ub)
        quick_sort(arr, lb, loc - 1)
        quick_sort(arr, loc+1, ub)


arr = [5, 1, 200, 15, 10, 9, 6, -1]
n = len(arr) - 1
quick_sort(arr, 0, n)

print(arr)
