

def knapsack(list, weight=50):
    for item in list:
        item.insert(0, item[0]/item[1])
    list.sort()
    list.reverse()
    profit = 0
    for i in range(0, len(list)):
        if weight >= list[i][2]:
            profit = profit + list[i][1]
            weight = weight - list[i][2]
        else:
            profit = profit + (weight * list[i][0])
            weight = 0
    print(profit)


list = [
    [60, 10],
    [120, 30],
    [100, 20],
]
l = [
    [10, 2],
    [4, 1],
    [20, 2],
]
knapsack(list, 50)
