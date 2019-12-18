import numpy as np


class HungarianAlgorithm:
  def __init__(self, job_matrix):
    self.n, self.m = job_matrix.shape
    self.job_matrix = self.reduce_matrix(job_matrix) # Находим и вычитаем мин элемент из столбца и строки
    print(job_matrix)
    self.stars_by_row = [-1 for _ in range(self.n)] # Для отметки в какой строке 0
    self.stars_by_col = [-1 for _ in range(self.m)] # Аналогично
    self.primes_by_row = [-1 for _ in range(self.n)]
    self.covered_rows = [False for _ in range(self.n)]
    self.covered_cols = [False for _ in range(self.m)]

  def reduce_matrix(self, job_matrix):
    for i in range(self.n):
      min_val = min(job_matrix[i])
      job_matrix[i] = [x - min_val for x in job_matrix[i]]

    for j in range(self.m):
      min_val = min(job_matrix[:, j])
      job_matrix[:, j] -= min_val

    return job_matrix

  def mark_stars(self): # Отмечаем колонку и строку в которой нашли 0
    row_has_starred_zero = [False for _ in range(self.n)] # Нужно чтобы не отметить строку с двумя 0
    col_has_starred_zero = [False for _ in range(self.m)] # Аналогично

    for i in range(self.n):
      for j in range(self.m):
        if self.job_matrix[i][j] == 0 and not row_has_starred_zero[i] and not col_has_starred_zero[j]:
          self.stars_by_row[i] = j
          self.stars_by_col[j] = i
          row_has_starred_zero[i] = True
          col_has_starred_zero[j] = True

  def cover_columns_of_starred_zeros(self): # Отмечаем отмеченые колонки
    for i in range(self.m):
      if self.stars_by_col[i] != -1:
        self.covered_cols[i] = True
      else:
        self.covered_cols[i] = False

  def all_columns_covered(self): # Проверяем все ли колонки отмечены
    for value in self.covered_cols:
      if value == False:
        return False
    return True

  def prime_any_uncovered_zero(self): # Находим еще один 0 в строке
    for i in range(self.n):
      if self.covered_rows[i] == True: # Пропускаем отмеченые
        continue
      for j in range(self.m):
        if self.job_matrix[i][j] == 0 and self.covered_cols[j] == False:
          self.primes_by_row[i] = j
          return i, j
    return None

  def solve(self):
    self.mark_stars() # Отмечаем колонку и строку в которой нашли 0
    self.cover_columns_of_starred_zeros() # Отмечаем отмеченые колонки

    while not self.all_columns_covered(): # Пока не все колонки отмечены
      primed_zero = self.prime_any_uncovered_zero() # Находим еще один 0 в строке
      while primed_zero is None:
        self.make_more_zeros()
        primed_zero = self.prime_any_uncovered_zero()

      column_index = self.stars_by_row[primed_zero[0]] # Ниже проверка если под таким индексом колонка уже отмечена
      if column_index == -1: # Если нет
        self.make_alternating_set(primed_zero)
        self.primes_by_row = [-1 for _ in range(self.n)]
        self.covered_rows = [False for _ in range(self.n)]
        self.covered_cols = [False for _ in range(self.m)]
        self.cover_columns_of_starred_zeros()
      else:
        self.covered_rows[primed_zero[0]] = True # Отмечаем колонку как не проверенную, чтобы позже проверить вдруг есть другой 0
        self.covered_cols[column_index] = False

    result = []
    for i in range(len(self.stars_by_col)):
      result.append((self.stars_by_col[i], i))

    return result

  def make_more_zeros(self): # Преобрахование если закончились простые 0
    min_uncovered_value = np.inf
    for i in range(self.n): # Находим мин значение среди не отмеченых колонок и строк
      if self.covered_rows[i] == True:
        continue
      for j in range(self.m):
        if self.covered_cols[j] == False and self.job_matrix[i][j] < min_uncovered_value:
          min_uncovered_value = self.job_matrix[i][j]

    for i in range(self.n): # Прибавляем мин значение к отмеченной строке
      if self.covered_rows[i] == True:
        for j in range(self.m):
          self.job_matrix[i][j] += min_uncovered_value

    for i in range(self.m):
      if self.covered_cols[i] == False: # Отнимаем мин значение у не отмеченых столбцах
        for j in range(self.n):
          self.job_matrix[j][i] -= min_uncovered_value
    print("\n", self.job_matrix)


  def make_alternating_set(self, prime_zero):
    j = prime_zero[1]
    zero_sequence = set()
    zero_sequence.add(tuple(prime_zero))

    while True:
      i = self.stars_by_col[j]
      if i != -1 and (i, j) not in zero_sequence:
        zero_sequence.add((i, j))
      else:
        break
      j = self.primes_by_row[i]
      if j != -1 and (i, j) not in zero_sequence:
        zero_sequence.add((i, j))
      else:
        break

    for zero in zero_sequence:
      i, j = zero
      if self.stars_by_col[j] == i:
        self.stars_by_col[j] = -1
        self.stars_by_row[i] = -1

      if self.primes_by_row[i] == j:
        self.stars_by_row[i] = j
        self.stars_by_col[j] = i


cost = np.array(
  [
    [2, -1, 9, 4],
    [3, 2, 5, 1],
    [13, 0, -3, 4],
    [5, 6, 1, 2]
  ]
)

hungarian = HungarianAlgorithm(cost)
solution = hungarian.solve()

for job, worker in solution:
  print("Worker", worker + 1, "gets job", job + 1)
