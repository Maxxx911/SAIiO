def swap(a, b):
  temp = a[:]
  a = b[:]
  b = temp[:]
  return a, b


def make_basis_graf(n, S): #строим базисный граф, списками смежности
  g = dict()
  for i in range(n):
    g[i] = []

  for i in range(n):
    for j in range(len(S)):
      if S[j][4] == 1:
        if i == S[j][0]:
          g[i].append(S[j][1]) #Задаем прямую дуга
          g[S[j][1]].append(i) #и тут же обратную

  return g


def dfs_u(v, g, S, u, used): # поиск в глубину чтобы искать потенциалы,
  # проходимся по всем вершинам и смотрим какая вершина является выходом или входом
  # чтобы отнимать или добавлять Ui или Uj
  used[v] = True
  for to in g[v]:
    if used[to] == False:
      for elem in S:
        if v == elem[0] and to == elem[1]:
          u[to] = u[v] - elem[2]
        elif v == elem[1] and to == elem[0]:
          u[to] = u[v] + elem[2]
      dfs_u(to, g, S, u, used)


def solve_potensial(n, g, S):
  used = [False for i in range(n)] # массив посещенный вершин
  u = [0 for i in range(n)] # потенциалы
  u[0] = 0
  dfs_u(0, g, S, u, used) # Запускаем поиск в глубину
  return u


def solve_marks(S, u): # считаем оценки
  delta = []
  for elem in S:
    if elem[4] == 0:
      delta.append(((elem[0], elem[1]), u[elem[0]] - u[elem[1]] - elem[2]))

  return delta


def dfs(v, color, p, g): # 2 Функции для поиска циклов (тоже поиск в глубину) => 
                         # берём все вершины и карсив в 2 цвета (0 и 1) и как только доходим до
                         #  новой верины красим в 1, когда снова дошли в 1 - нашли цикл
  color[v] = 1
  for to in g[v]:
    if color[to] == 0:
      p[to] = v
      if (dfs(to, color, p, g)):
        return True

    elif (color[to] == 1) and (p[v] != to):
      global cycle_st
      global cycle_end
      cycle_end = v
      cycle_st = to
      return True

  color[v] = 2
  return False


def cycle(uu, n, g): #раскраска для поиска цикла
  color = []
  p = []
  for i in range(n):
    color.append(0)
    p.append(-1)

  if dfs(uu, color, p, g):
    temp_cycle = []
    v = cycle_end
    while (v != cycle_st):
      temp_cycle.append(v)
      v = p[v]

    temp_cycle.append(cycle_st)

  return temp_cycle


def matrics_network_task(n, S):
  while (True):
    g1 = make_basis_graf(n, S) #строим базисный граф
    u = solve_potensial(n, g1, S) #считаем потенциалы
    delta = solve_marks(S, u) # считаем оценки
    temp_list = [elem[1] for elem in delta]
    max_delta = max(temp_list) # находим макс оценку
    if max_delta <= 0: # => Решено
      sum = 0
      for elem in S:
        sum += elem[2] * elem[3]

      print (sum)
      return S

    ind = temp_list.index(max_delta) # иначе ищем Jo , Io
    curve_0 = delta[ind][0]
    for i in range(len(S)):
      if S[i][0] == curve_0[0] and S[i][1] == curve_0[1]:
        S[i][4] = 1 # Добавляем в базис

    g2 = make_basis_graf(n, S) # перестраиваем граф
    U = cycle(curve_0[0], n, g2) # строим для него цикл
    U.reverse() # переворачиваем потому что храним в обратном порядке
    U.append(U[0]) # Добавляем нулевую вершину чтобы циклиться
    U_plus = []
    U_minus = []
    for i in range(len(U) - 1): # создаём наши U+ , U-
      for elem in S:
        if U[i] == elem[0] and U[i + 1] == elem[1]:
          U_plus.append((U[i], U[i + 1]))
          break
        elif U[i] == elem[1] and U[i + 1] == elem[0]:
          U_minus.append((U[i + 1], U[i]))
          break

    if curve_0 not in U_plus:
      U_minus, U_plus = swap(U_minus, U_plus) # Когда ищем цикл. Не факт что дуга по направлению может замкнуть цикл. Может не получиться дуга ?

    tetta = [] # ищем все тетты
    for elem in S:
      tupl = (elem[0], elem[1])
      if tupl in U_minus:
        tetta.append((tupl, elem[3]))

    tetta0 = min([tetta[i][1] for i in range(len(tetta))]) # ищем минимальную тетту
    for elem in tetta:
      if elem[1] == tetta0:
        curve_star = elem[0]
        break

    for curve in U_plus: # Добавлям для всех
      for i in range(len(S)):
        if curve[0] == S[i][0] and curve[1] == S[i][1]:
          S[i][3] += tetta0
          break

    for curve in U_minus: # отнимаем
      for i in range(len(S)):
        if curve[0] == S[i][0] and curve[1] == S[i][1]:
          S[i][3] -= tetta0
          break

    for i in range(len(S)): # убираем дугу из базиса
      if curve_star[0] == S[i][0] and curve_star[1] == S[i][1]:
        S[i][4] = 0
        break


if __name__ == "__main__":
  cycle_st = -1
  cycle_end = -10
  # Из какой вершина, в какую, стоимость, поток, 1 - базисная 0 - не базисная
  # Task 1
  S1 = [
    [0, 1, 9, 2, 1],
    [0, 7, 5, 7, 1],
    [1, 2, 1, 4, 1],
    [1, 5, 3, 0, 0],
    [1, 6, 5, 3, 1],
    [2, 8, -2, 0, 0],
    [3, 2, -3, 0, 0],
    [4, 3, 6, 3, 1],
    [5, 4, 8, 4, 1],
    [6, 2, -1, 0, 0],
    [6, 3, 4, 0, 0],
    [6, 4, 7, 5, 1],
    [6, 8, 1, 0, 0],
    [7, 6, 2, 0, 0],
    [7, 8, 2, 0, 0],
    [8, 5, 6, 2, 1],
  ]
  n1 = 9
  # Task 7
  S7 = [
    [0, 1, 7, 2, 1],
    [0, 2, 6, 3, 1],
    [2, 3, 6, 4, 1],
    [2, 4, 5, 4, 1],
    [5, 6, 4, 2, 1],
    [6, 4, 7, 5, 1],
    [1, 2, 4, 0, 0],
    [1, 5, 3, 0, 0],
    [3, 5, 1, 0, 0],
    [4, 3, 4, 0, 0],
    [4, 5, -1, 0, 0],
    [0, 4, 3, 0, 0],
    [6, 0, 2, 0, 0]
  ]
  n7 = 7
  res = matrics_network_task(n1, S1)
  for i in res:
    if i[3] != 0:
      print("from:", i[0] + 1, " to:", i[1] + 1, " = ", i[3])
