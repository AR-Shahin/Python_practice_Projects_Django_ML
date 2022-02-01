

import sys
from heapq import heapify, heappush, heappop


def dijkstra(graph, source, destination):
    inf = sys.maxsize
    node_data = {}
    for node in graph.keys():
        node_data[node] = {'cost': inf, 'pred': []}

    node_data[source]['cost'] = 0
    visited = []
    temp = source

    for i in range((len(graph.keys())-1)):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + \
                            list(temp)
                    heappush(min_heap, (node_data[j]['cost'], j))
        heapify(min_heap)
        temp = min_heap[0][1]
        # print(temp)
        # return
    print("Sortest Distance : ", str(node_data[destination]['cost']))
    print("Sortest Path : ", str(
        node_data[destination]['pred'] + list(destination)))


graph = {
    "A": {"B": 2, "C": 4},
    "B": {"A": 2, "C": 3, "D": 8},
    "C": {"A": 4, "B": 3, "D": 2, "E": 5},
    "D": {"B": 8, "C": 2, "F": 22, "E": 11},
    "E": {"C": 5, "D": 11, "F": 1},
    "F": {"D": 22, "E": 1},
}


source = "A"
destination = "E"
dijkstra(graph, source, destination)
