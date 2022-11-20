from queue import Queue
import numpy as np

from Graphs.AdjacencyMatrixGraph import AdjacencyMatrixGraph


def breadth_first(graph, start=0):
    queue = Queue()
    queue.put(start)

    visited = np.full((graph.num_vertices,), False, dtype=bool)

    while not queue.empty():
        vertex = queue.get()

        if visited[vertex]:
            continue

        print("Visited: ", vertex)
        visited[vertex] = True

        for v in graph.get_adjacent_vertices(vertex):
            if not visited[v]:
                queue.put(v)


def depth_first(graph, visited, current=0):
    if visited[current]:
        return

    visited[current] = True

    print("Visited: ", current)

    for vertex in graph.get_adjacent_vertices(current):
        depth_first(graph, visited, vertex)





print("Adjacency Graph Matrix")

g = AdjacencyMatrixGraph(9)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 5)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(7, 3)
g.add_edge(3, 4)
g.add_edge(2, 5)

print("Breadth first")
g.show()
breadth_first(g, 2)

print("Depth first")

visited = np.full((g.num_vertices,), False, dtype=bool)
depth_first(g, visited)
