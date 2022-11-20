import numpy as np
from Graphs.Graph import Graph


class AdjacencyMatrixGraph(Graph):

    def __init__(self, num_vertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(num_vertices, directed)

        self.matrix = np.zeros((num_vertices, num_vertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        if weight == 0:
            raise ValueError("Edges cannot have a weight of 0")

        self.matrix[v1][v2] = weight
        if self.directed == False:
            self.matrix[v2][v1] = weight

    def remove_edge(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        self.matrix[v1][v2] = 0
        if self.directed == False:
            self.matrix[v2][v1] = 0

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex %d" % v)

        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def is_adjacent(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        return self.matrix[v1][v2] != 0

    def get_indegree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex %d" % v)

        indegree = 0
        for i in range(self.num_vertices):
            if self.matrix[i][v] > 0:
                indegree = indegree + 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def show(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


g = AdjacencyMatrixGraph(4)

g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 3)
g.add_edge(3, 2)

g.show()

for i in range(4):
    print("Adjacent to: ", i, g.get_adjacent_vertices(i))


g = AdjacencyMatrixGraph(4, directed=True)
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 3)
g.add_edge(3, 2)

g.show()

