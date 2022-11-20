class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.id == v:
            raise ValueError("The vertex %d cannot be adjacent to itself" % v)

        self.adjacency_set.add(v)

    def remove_edge(self, v):
        if self.id == v:
            raise ValueError("The vertex %d cannot be adjacent to itself" % v)

        self.adjacency_set.remove(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)

    def is_adjacent(self, v):
        return v in self.adjacency_set