
# # Graph representation in Adjency List

# adj_list = {
#     "A": ["B", "C"],
#     "B": ["A", "D"],
#     "C": ["A", "D", "E"],
#     "D": ["B", "C", "E"],
#     "E": ["D", "C"]
# }

# print(adj_list["A"])


# # Add new Edge A->D

# adj_list["A"].append("D")
# adj_list["D"].append("A")
# print(adj_list)


class Graph:
    def __init__(self, Nodes, is_directed=False):
        self.is_directed = is_directed
        self.nodes = Nodes
        self.adj_list = {}

        # Generate Node
        for node in self.nodes:
            self.adj_list[node] = []

    def print_adj_list(self):
        for node in self.nodes:
            #print(node, " -> ", self.adj_list[node])
            print("{} -> {}".format(node, self.adj_list[node]))

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        if not self.is_directed:
            self.adj_list[v].append(u)

    def add_multiple_edges(self, edges):
        for u, v in edges:
            self.add_edge(u, v)

    def degree_of_node(self, node):
        return len(self.adj_list[node])


nodes = ["A", "B", "C", "D", "E"]
edges = [
    ("A", "C"),
    ("A", "B"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("D", "E"),
]

directed_edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "B"),
    ("D", "C")
]
graph = Graph(nodes)

# print(graph)
# graph.add_edge("A", "B")
# graph.add_edge("A", "C")
graph.add_multiple_edges(edges)
# graph.print_adj_list()

print(graph.degree_of_node("A"))
