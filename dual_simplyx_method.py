from numpy import *

class DualSimplyxMethod(object):
  def __init__(self, A, b, c, d_low, d_high, Jb = None, Jnb = None):
    self.A = A
    self.b = b
    self.c = c
    self.d_low = d_low
    self.d_high = d_high
    self.Jb = Jb
    self.Jnb = Jnb

  def find_basis_indexes(self):
    if self.Jb == None:
      print self.lab3(self.c, self.b, self.A)

  def lab3(c, b, A):
    while True:
        M = len(A)
        N = len(A[0])
        # print(M)
        # print(N)
        two_task_Jb = np.array([], dtype=int)
        two_task_A = np.c_[A, np.eye(M)]
        print('Two task A = \n', two_task_A)
        two_task_x = np.c_[np.zeros((1, N)), b.reshape((1, M))]
        for i in range(1, M + 1):
            two_task_Jb = np.append(two_task_Jb, N + i)
        print('Two task Jb = ', two_task_Jb)
        two_task_c = np.c_[np.zeros((1, N)), np.ones((1, M))]
        print('Two task c = ', two_task_c)
        two_task_x = simplex_method(two_task_c, two_task_A, b, two_task_x, two_task_Jb)
        print('Two task x = ', two_task_x)
        if two_task_x is None:
            return
        for el in two_task_x[0]:
            if el != 0:
                print('Task not joined')
                return
        J = []
        for j in range(1, M + 1):
            if j not in two_task_Jb:
                J.append(j)
        print('J = ', J)
        for k in J:
            Ab = two_task_A[:, two_task_Jb - 1]
            print('Ab= \n', Ab)
            Ab_inv = np.linalg.inv(Ab)
            print('Ab^-1= \n', Ab_inv)
            Aj = two_task_A[:, k-1]
            print('Aj= \n', Aj)
            Lj = Ab_inv.dot(Aj)
            print('L(', k, ')=', Lj)
            if Lj[k-1] != 0:
                two_task_Jb[k -1] = k
            else:
                A = A[[i for i in range(0, M) if i != k - 1], :]
                b = b[[i for i in range(0, M) if i != k - 1]]
                two_task_Jb = two_task_Jb[[i for i in range(0, M) if i != k - 1]]
                break
        check = []
        for j in two_task_Jb:
            if 1 <= j < M:
                check.append(True)
        if all(check):
            break
    print('Result:')
    print('C=', c, '\nA=\n', A, '\nb=', b, '\nX=', two_task_x[:, range(0, M)], '\nJb=', two_task_Jb)
    return c, A, b, two_task_x, two_task_Jb

if __name__ == "__main__":
  A = array([
    array([2, 1, -1, 0, 0, 1], dtype=float),
    array([1, 0, 1, 1, 0, 0], dtype=float),
    array([0, 1, 0, 0, 1, 0], dtype=float)
  ])
  b = array([2, 5, 0], dtype=float)
  c = array([3, 2, 0, 3, -2, -4], dtype=float)
  d_low = array([0, -1, 2, 1, -1, 0], dtype=float)
  d_high = array([2, 4, 4, 3, 3, 5], dtype=float)
  DualSimplyxMethod(A, b, c, d_low, d_high).find_basis_indexes()
