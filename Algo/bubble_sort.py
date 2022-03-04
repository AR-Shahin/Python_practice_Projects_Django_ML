
def bubble_sort(arr, n):
    for i in range(0, n):
        # print((len(arr) - 1 - i))
        for j in range(0, n):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


arr = [10, 50, 40, 30, 20]

# bubble_sort(arr, len(arr))


def fun(arr):
    for i in range(0, 2):
        for j in range(0, 2):
            if arr[j][0] < arr[j][1]:
                t1 = arr[j][0]
                t2 = arr[j][1]
                arr[j][0] = arr[j + 1][0]
                arr[j][1] = arr[j + 1][1]
            elif arr[j][0] == arr[j][1]:
                pass
                # if arr[j][1] < arr[j+1][1]:
                #     arr[j][1] = arr[j+1][1]
                #     arr[j][0] = arr[j+1][0]


brr = [
    [10, 20],
    [100, 10],
    [30, 20],
]
fun(brr)
print(brr)
