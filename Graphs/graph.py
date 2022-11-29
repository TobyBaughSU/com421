import heapq
import sys

class Node:
    def __init__(self, name: str):
        self.data = [sys.maxsize, self]
        self.name = name
        self.parent = None
        self.used = False
        self.edges = []

        self.isInOpenList = False

    def __lt__(self, other):
        return self.name < other.name

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, start: Node, end: Node, dist: int):
        self.start = start
        self.end = end
        self.dist = dist


class Graph:
    def __init__(self):
        self.heap = []

    def add_edge(self, start: Node, end: Node, dist: int):
        start.add_edge(Edge(start, end, dist))
        end.add_edge(Edge(end, start, dist))

    def dijkstra(self, start: Node, end: Node):
        cur_node = start
        priority_queue = self.heap.copy()

        cur_node.data[0] = 0
        while cur_node != end and len(self.heap) != 0:

            for edge in cur_node.edges:
                if not edge.end.used and not edge.end.isInOpenList:
                    edge.end.isInOpenList = True
