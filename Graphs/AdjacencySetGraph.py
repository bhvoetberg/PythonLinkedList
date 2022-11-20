import Graph
import Vertex


class AdjacencySetGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super(AdjacencySetGraph, self).__init__(num_vertices, directed)

        self.vertex_list = []
        for i in range(num_vertices):
            v = Vertex(i)
            self.vertex_list.append(v)

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        if weight != 1:
            raise ValueError("An adjacency set cannot represent edge weights > 1")

        self.vertex_list[v1].add_edge(v2)

        if self.directed == False:
            self.vertex_list[v2].add_edge(v1)

    def remove_edge(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        self.vertex_list[v1].remove_edge(v2)

        if self.directed == False:
            self.vertex_list[v2].remove_edge(v1)

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex %d" % v)

        return self.vertex_list[v].get_adjacent_vertices()

    def is_adjacent(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        return self.vertex_list[v1].is_adjacent(v2) or self.vertex_list[v2].is_adjacent(v1)

    def get_indegree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex %d" % v)

        indegree = 0
        for i in range(self.num_vertices):
            if i == v:
                continue
            if v in self.get_adjacent_vertices(i):
                indegree = indegree + 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def show(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


# ------------------------------------------------------

g = AdjacencySetGraph(4)
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 3)
g.add_edge(3, 2)

g.show()

for i in range(4):
    print("Adjacent to: ", i, g.get_adjacent_vertices(i))

for i in range(4):
    print("Indegree for vertex %d is %d" % (i, g.get_indegree(i)))

g.remove_edge(2, 3)
g.show()

for i in range(4):
    print("Adjacent to: ", i, g.get_adjacent_vertices(i))

g.is_adjacent(0, 1)

g.is_adjacent(0, 2)

g = AdjacencySetGraph(4, directed=True)

g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 3)
g.add_edge(3, 2)

g.show()

for i in range(4):
    print("Adjacent to: ", i, g.get_adjacent_vertices(i))

for i in range(4):
    print("Indegree for vertex %d is %d" % (i, g.get_indegree(i)))

