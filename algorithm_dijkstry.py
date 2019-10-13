import numpy as np


class Dijkstra(object):
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.length = graph.shape[0]

    def algorithm(self):
        valid = [True] * self.length
        weight = [np.inf] * self.length
        weight[self.start] = 0
        for i in range(self.length):
            min_weight = np.inf
            ID_min_weight = -1
            for j in range(len(weight)):
                if valid[j] and weight[j] < min_weight:
                    min_weight = weight[j]
                    ID_min_weight = j
            for i in range(self.length):
                if (weight[ID_min_weight] + self.graph[ID_min_weight][i]) < weight[i]:
                    weight[i] = weight[ID_min_weight] + self.graph[ID_min_weight][i]
            valid[ID_min_weight] = False
        return weight

    def solve(self):
        weight = self.algorithm()
matrix = np.array([
                    [np.inf, 5, np.inf, np.inf, np.inf, np.inf, np.inf, 3, np.inf, np.inf],
                    [np.inf, np.inf, 2, np.inf, np.inf, np.inf, 3, np.inf, np.inf, np.inf],
                    [np.inf, np.inf, np.inf, np.inf, 5, np.inf, np.inf, np.inf, np.inf, np.inf],
                    [np.inf, np.inf, 2, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
                    [np.inf, np.inf, np.inf, 1, np.inf, np.inf, np.inf, np.inf, np.inf, 2],
                    [np.inf, np.inf, 4, np.inf, 1, np.inf, np.inf, 6, 2, np.inf],
                    [2, np.inf, 2, np.inf, np.inf, 5, np.inf, np.inf, np.inf, np.inf],
                    [np.inf, 1, np.inf, np.inf, np.inf, np.inf, 4, np.inf, 1, np.inf],
                    [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 5],
                    [np.inf, np.inf, np.inf, 6, np.inf, 3, np.inf, np.inf, np.inf, np.inf]
                ])
a = Dijkstra(matrix, 0, 5)
print(a.algorithm())
