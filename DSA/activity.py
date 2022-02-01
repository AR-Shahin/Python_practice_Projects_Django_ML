

def bubble_sort_asc(list):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i][1] > list[j][1]:
                list[i], list[j] = list[j], list[i]


def optimal_solution(list):
    print(list[0][2], end=" ")
    temp = list[0]
    for i in range(1, len(list)):
        if temp[1] <= list[i][0]:
            temp = list[i]
            print(list[i][2], end=" ")


activities = [
    (0, 6, "A"),
    (1, 2, "B"),
    (5, 7, "C"),
    (8, 9, "D"),
    (3, 4, "E"),
    (5, 9, "F"),
]

# print(activities)
bubble_sort_asc(activities)
optimal_solution(activities)
