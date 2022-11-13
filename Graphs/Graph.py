import abc

import numpy as np


class Graph(abc.ABC):
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def remove_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjecent_vertices(self, v):
        pass

    @abc.abstractmethod
    def is_adjecent(self, v1, v2):
        pass

    @abc.abstractmethod
    def get_indegree_edge(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def show(self):
        pass


class Vertex:
    def __int__(self):
        self.id = id
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.id == v:
            raise ValueError("Vertex % d cannot be adjacent to itself" % v)
        self.adjacency_set.add(v)

    def remove_edge(self, v):
        if self.id == v:
            raise ValueError("Vertex % d cannot be adjacent to itself" % v)
        self.adjacency_set.remove(v)

    def get_adjacency_vertices(self):
        return sorted(self.adjacency_set)

    def is_adjacent(self, v):
        return v in self.adjacency_set

class AdjacencySetGraph(Graph):
    def __init__(self, num_vertices, directed = False):
        super(AdjacencySetGraph, self).__init__(num_vertices, directed)

        self.vertex_list = []
            for i in range(num_vertices):
                v = Vertex(i)
                self.vertex_list.append(v)

    def add_edge(self, v1, v2, weight):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))
        if weight != 1:
            raise ValueError("An adjacency set cannot represent edge weights > 1")

        self.vertex_list[v1].add_edge(v2)

        if self.directed == False:
            self.vertex_list[v2].add_edge(v1)

    def remove_edge(self, v1, v2, weight):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        self.vertex_list[v1].remove_edge(v2)

        if self.directed == False:
            self.vertex_list[v2].remove_edge(v1)

    def get_adjecent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex % d" % v)

        return self.vertex_list[v].get_adjacency_vertices()

    def is_adjecent(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        return self.vertex_list[v1].is_adjacent((v2)) or self.vertex_list[v2].is_adjacent(v1)

    def get_indegree_edge(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex % d" % v)
        indegree = 0
        for i in range(self.num_vertices):
            if i == v:
                continue
            if v in self.get_adjecent_vertices(i):
                indegree = indegree + 1

            return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def show(self):
        for i in range(self.num_vertices):
            for v in self.get_adjecent_vertices(i):
                print(i, "-->", v)

    def __int__(self, num_vertices, directed=False):
        super(AdjacencySetGraph, self).__init__((num_vertices, directed))

        self.vertex_list = []
        for i in range(num_vertices):
            v = Vertex(i)

            self.vertex_list.append(v)


g = AdjacencySetGraph(4)
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 3)
g.add_edge(3, 2)

