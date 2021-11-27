
# Selection Sort
def selection_sort(arr, mode='asc'):
    l = len(arr)
    for i in range(0, l):
        min_index = i
        for j in range(i+1, l):
            if mode == 'asc':
                if arr[min_index] > arr[j]:
                    min_index = j
            elif mode == 'dsc':
                if arr[min_index] < arr[j]:
                    min_index = j

        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            # temp = arr[i]
            # arr[i] = arr[min_index]
            # arr[min_index] = temp
    print(arr)


arr = [10, 10, 15, 16, 45, 9, 2, 1, 50]

selection_sort(arr, 'asc')

# print(arr)
