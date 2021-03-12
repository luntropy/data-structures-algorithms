#!/usr/bin/python3

import sys
sys.path.append('../algorithms/')
import algorithms as alg

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph.keys():
            self.graph[u] = []

        self.graph[u].append(v)

    def dfs(self, s):
        alg.dfs(self.graph, s)

    def dfs_stack(self, s):
        alg.dfs_stack(self.graph, s)

    def bfs(self, s):
        alg.bfs(self.graph, s)

if __name__ == '__main__':
    g = Graph()

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print('Recursive DFS: ')
    g.dfs(0)

    print()
    print('DFS using stack: ')
    g.dfs_stack(0)

    print()
    print('BFS: ')
    g.bfs(0)
    print()
