from numpy import array, inf

class Floyd(object):
  def __init__(self, graph):
    self.graph = graph
    self.n = len(self.graph)
    self.d = array(self.graph)
    self.r = array([list(range(1, self.n + 1)) for _ in range(1, self.n + 1)])

  def solve(self):
    for k in range(self.n):
      for i in range(self.n):
        for j in range(self.n):
          if self.d[i, k] < inf and self.d[k, j] < inf and (self.d[i, k] + self.d[k, j]) < self.d[i, j]:
            self.d[i, j] = self.d[i, k] + self.d[k, j]
            self.r[i, j] = self.r[i, k]

    return self.d, self.r

matrix = [
  [0, 9, inf, 3, inf, inf, inf, inf],
  [9, 0, 2, inf, 7, inf, inf, inf],
  [inf, 2, 0, 2, 4, 8, 6, inf],
  [3, inf, 2, 0, inf, inf, 5, inf],
  [inf, 7, 4, inf, 0, 10, inf, inf],
  [inf, inf, 8, inf, 10, 0, 7, inf],
  [inf, inf, 6, 5, inf, 7, 0, inf],
  [inf, inf, inf, inf, 9, 12, 10, 0]]

matrix1 = [
  [0, 3, 2, 6, inf, inf, inf, inf, inf],
  [inf, 0, inf, 2, inf, inf, inf, inf, inf],
  [inf, inf, 0, inf, inf, 4, inf, inf, inf],
  [inf, inf, 3, 0, 1, inf, 6, inf, inf],
  [inf, inf, inf, inf, 0, inf, 7, 5, inf],
  [inf, inf, inf, inf, 5, 0, inf, 4, inf],
  [inf, inf, inf, inf, inf, inf, 0, 2, 4],
  [inf, inf, inf, inf, inf, inf, inf, 0, 4],
  [inf, inf, inf, inf, inf, inf, inf, inf, 0]]

matrix2 = [
  [0, 3, 4, inf, 5, inf, inf, inf],
  [inf, 0, 2, 1, inf, inf, 4, inf],
  [inf, inf, 0, 3, 2, inf, inf, inf],
  [inf, inf, inf, 0, inf, inf, 3, inf],
  [inf, inf, inf, 4, 0, 8, inf, 3],
  [inf, inf, inf, 5, inf, 0, inf, 2],
  [inf, inf, inf, inf, inf, 2, 0, 1],
  [inf, inf, inf, inf, inf, inf, inf, 0]]

Dn, Rn = Floyd(matrix).solve()

print(Dn)
print("\n", Rn)
