import numpy as np


class Dijkstra(object):
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end

    def solve(self):
        
        print()


a = Dijkstra(np.array([[np.inf, 5, np.inf, np.inf, np.inf, np.inf, np.inf, 3, np.inf, np.inf],
                       [np.inf, np.inf, 2, np.inf, np.inf, np.inf, 3, np.inf, np.inf, np.inf],
                       [np.inf, np.inf, np.inf, np.inf, 5, np.inf, np.inf, np.inf, np.inf, np.inf],
                       [np.inf, np.inf, 2, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
                       [np.inf, np.inf, np.inf, 1, np.inf, np.inf, np.inf, np.inf, np.inf, 2],
                       [np.inf, np.inf, np.inf, np.inf, 1, np.inf, np.inf, 6, 2, np.inf],
                       [1, np.inf, 2, np.inf, np.inf, 5, np.inf, np.inf, np.inf, np.inf],
                       [np.inf, 1, np.inf, np.inf, np.inf, np.inf, 2, np.inf, 1, np.inf],
                       [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 5],
                       [np.inf, np.inf, np.inf, 6, np.inf, 3, np.inf, np.inf, np.inf, np.inf]
                       ]))
a.solve()
