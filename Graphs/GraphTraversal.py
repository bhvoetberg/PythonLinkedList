from queue import Queue
import numpy as np

def breadth_first(graph, start = 0):
    queue = Queue()
    queue.put(start)

    visited = np.full((graph.num_vertices, ), False, dtype=bool)

    while not queue.empty():
        vertex = queue.get()

        if visited[vertex]:
            continue

        print("Visited: ", vertex)
        visited[vertex] = True

        for v in graph.get_adjacent_vertices(vertex):
            if not visited[v]:
                queue.put(v)


