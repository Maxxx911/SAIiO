import itertools

INF = 999999999


def held_karp(dist):
  min_cost_distance_path = {}
  parent = {}

  n = len(dist)
  vertices = tuple(range(1, n))

  all_sets = [()]
  for i in range(1, n):
    all_sets.extend(list(itertools.combinations(vertices, i))) # Формируем кобинации значений {}, {1}, {2} и

  for current_set in all_sets:
    for current_vertex in range(1, n):
      if current_vertex in current_set:
        continue

      index = (current_vertex, current_set)
      min_cost = INF
      min_prev_vertex = 0

      for prev_vertex in current_set:
        cost = dist[prev_vertex][current_vertex] + get_cost(current_set, prev_vertex, min_cost_distance_path)
        if cost < min_cost:
          min_cost = cost
          min_prev_vertex = prev_vertex

      if len(current_set) == 0: # значит у нас {}
        min_cost = dist[0][current_vertex]

      min_cost_distance_path[index] = min_cost
      parent[index] = min_prev_vertex

  min = INF
  prev_vertex = -1
  for k in vertices:
    cost = dist[k][0] + get_cost(vertices, k, min_cost_distance_path)
    if cost < min:
      min = cost
      prev_vertex = k

  parent[(0, vertices)] = prev_vertex
  print_tour(parent, n)
  print(min)


def get_cost(current_set, prev_vertex, min_cost_dp):
  l = list(current_set)
  l.remove(prev_vertex)
  index = (prev_vertex, tuple(l))
  cost = min_cost_dp.get(index)
  return cost


def print_tour(parent, total_vertices):
  vertices = list(range(total_vertices))
  start = 0
  stack = []
  while True:
    stack.append(start)
    if start in vertices:
      vertices.remove(start)
    start = parent.get((start, tuple(vertices)), None)
    if start is None:
      break

  print("->".join(reversed(list(map(lambda x: str(x + 1), stack)))))


def main():
  dist = [
    [0, 1, 15, 6],
    [2, 0, 7, 3],
    [9, 6, 0, 12],
    [10, 4, 8, 0]
  ]

  dist = [
    [0, 10, 25, 25, 10],
    [1, 0, 10, 15, 2],
    [8, 9, 0, 20, 10],
    [14, 10, 24, 0, 15],
    [10, 8, 25, 27, 0]
  ]
  held_karp(dist)


if __name__ == '__main__':
  main()
