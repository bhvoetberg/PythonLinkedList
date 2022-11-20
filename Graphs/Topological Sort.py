from queue import Queue
from Graph import *

# directed acyclic graph
def topological_sort(graph):
    queue = Queue()
    indegree_map = {}

    for i in range(graph.num_vertices):
        indegree_map[i] = graph.get_indegree(i)

        if indegree_map[i] == 0:
            queue.put(i)

        sorted_list = []

        while not queue.empty():
            vertex = queue.get()

            sorted_list.append(vertex)

            for v in graph.get_adjacent_vertices(vertex):
                indegree_map[v] = indegree_map[v] -1

                if indegree_map[v] == 0
                    queue.put(v)

            # Hier verbleven
            # if len(sorted_list) != graph.num_vertices


