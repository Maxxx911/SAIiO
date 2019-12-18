import numpy as np

def find_max_route(c, s, t):
  I_star, n = {s}, len(c)
  f = np.array([None]*n)
  f[s] = -1
  B = np.zeros(n)
  while True:

    I_plus = set()
    for iv in I_star:
      Iv_plus = set()    
      for i in range(n): # Находим связаные узлы
        if c[iv][i] != 0 and i not in I_star:
          Iv_plus.add(i)

      I_plus = I_plus.union(Iv_plus)

    for j in I_plus:

      Ij_minus = set()
      for i in range(n):
        if c[i][j] != 0:
          Ij_minus.add(i)

      if Ij_minus.issubset(I_star):
        I_star.add(j)

        Bp = []
        for bp in Ij_minus:
          Bp.append((B[bp] + c[bp][j], bp)) # Подсчет временых меток

        Bi = [x[0] for x in Bp]
        B[j] = max(Bi) # Находим максимальную метку и записываем ее 

        prev_v = Bp[Bi.index(B[j])][1]
        f[j] = prev_v
        break
    if t in I_star:
      break
  return B[t], f

def print_route(route, t, s):
  result, v = [t + 1], t
  while True:
    v = route[v]
    if v == -1:
      break
    result.append(v+1)
  result.reverse()
  for el in result:
    print(el, "=>", end=" ")


c = np.array([
  [[0, 2, 0, 0, 0, 1],
   [0, 0, 2, 0, 7, 0],
   [0, 0, 0, 8, 0, 0],
   [0, 0, 0, 0, 0, 0],
   [0, 0, 1, 1, 0, 0],
   [0, 4, 4, 0, 1, 0]],
        
  [[0, 4, 3, 2, 0, 0, 0, 0],
   [0, 0, 0, 5, 0, 3, 0, 0],
   [0, 0, 0, 0, 4, 7, 3, 0],
   [0, 0, 0, 0, 0, 0, 4, 0],
   [0, 0, 0, 0, 0, 2, 5, 0],
   [0, 0, 0, 2, 0, 0, 1, 0],
   [0, 0, 0, 0, 0, 0, 0, 0],
   [5, 6, 4, 1, 0, 0, 0, 0]],

  [[0, 0, 0, 2, 0, 0, 0],
   [1, 0, 6, 0, 3, 0, 0],
   [0, 0, 0, 4, 1, 4, 0],
   [0, 0, 0, 0, 2, 5, 0],
   [0, 0, 0, 0, 0, 1, 0],
   [0, 0, 0, 0, 0, 0, 0],
   [3, 4, 5, 3, 0, 0, 0]],

  [[0, 1, 5, 0, 0, 0, 0, 0],
   [0, 0, 4, 3, 5, 0, 0, 0],
   [0, 0, 0, 2, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 3, 1, 0],
   [0, 0, 4, 0, 0, 2, 7, 0],
   [0, 0, 0, 0, 0, 0, 6, 0],
   [0, 0, 0, 0, 0, 0, 0, 0],
   [4, 1, 3, 0, 2, 7, 0, 0]],

  [[0, 0, 5, 1, 0, 0, 0, 0],
   [3, 0, 2, 0, 6, 0, 0, 0],
   [0, 0, 0, 4, 7, 2, 0, 0],
   [0, 0, 0, 0, 3, 7, 1, 0],
   [0, 0, 0, 0, 0, 1, 4, 0],
   [0, 0, 0, 0, 0, 0, 6, 0],
   [0, 0, 0, 0, 0, 0, 0, 0],
   [3, 4, 6, 2, 0, 0, 0, 0]]
])
s = [0, 7, 6, 7, 7]
t = [3, 6, 5, 6, 6]

for i in range(len(c)):
  print('\nTask', i)
  res, route = find_max_route(np.array(c[i]), s[i], t[i])
  print_route(route, t[i], s[i])
  print('max:', res)
