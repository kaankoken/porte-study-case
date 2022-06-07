# A class to represent a graph object
from queue import PriorityQueue
from typing import List, Tuple
from path import Path


class Graph:
    # Constructor to construct a graph
    def __init__(self, edges: List[Tuple[int]], n: int):
        self.vertices = n

        # To keep track of visited vertices
        self.visited = []

        # A list of lists to represent an adjacency list
        self.adjacent = [None] * n

        # allocate memory for the adjacency list
        for i in range(n):
            self.adjacent[i] = []

        # add edges to the directed graph
        for (src, dest, weight, label) in edges:
            # allocate node in adjacency list from src to dest
            self.adjacent[src].append((dest, weight, label))

    def _printPath(self, parent, j: int, path: List[Tuple]):
        if parent[j] == -1:
            path.append((j, ''))
            return

        self._printPath(parent, parent[j][0], path)
        path.append((j, parent[j][1]))

        return path

    def dijkstra(self, start: int, end: int):
        queue = PriorityQueue()
        # Unknown distance from source to each node set to infinity
        distance = [float("inf")] * self.vertices
        parent = [-1] * self.vertices

        distance[start] = 0

        for v in range(self.vertices):
            queue.put((0, v))

        while not queue.empty():
            (_, current_vertex) = queue.get()
            self.visited.append(current_vertex)

            for (dest, weight, label) in self.adjacent[current_vertex]:
                old_cost = distance[dest]
                new_cost = distance[current_vertex] + weight
                if new_cost < old_cost:
                    queue.put((new_cost, dest))
                    distance[dest] = new_cost
                    parent[dest] = (current_vertex, label)

        path = self._printPath(parent, end, [])

        result = Path(
            from_=start, to_=end, cost=distance[end], num_of_days=len(path) - 1, path=path
        )

        return result


# Function to print adjacency list representation of a graph
def printGraph(graph):
    for src in range(len(graph.adjacent)):
        # print current vertex and all its neighboring vertices
        for (dest, weight, label) in graph.adjacent[src]:
            print(f'({src} —> {dest}, {weight}, {label}) ', end='')
        print()
