import numpy as np


class ResourceAllocation(object):

    def __init__(self, f):
        self.f = f
        self.n = len(f)
        self.m = len(f[0])
        self.B = np.zeros([self.n, self.m])
        self.B[0] = self.f[0]
        self.x_with_zero = np.zeros([self.n, self.m])
        self.humanization_x = ''

    def construct_table_B(self):
        for k in range(1, self.n):
            for y in range(self.m):
                temp = []
                for z in range(y + 1):
                    temp.append(self.f[k][z] + self.B[k-1][y - z])
                max_value = max(temp)
                self.B[k][y] = max_value
                self.x_with_zero[k][y] = temp.index(max_value)
        self.print_table_B()

    def find_optimal_resource_allocation(self):
        ost = self.m - 1
        max_element = np.amax(self.B)
        max_element_index = np.where(self.B == max_element)
        x = max_element_index[0][0]
        y = max_element_index[1][0]
        value = self.x_with_zero[x][y]
        if value == 0:
            value = ost
        self.humanization_x += 'x{0}={1},'.format(x + 1, value)
        ost -= value
        while(x != 0):
            x -= 1
            value = self.x_with_zero[x][int(ost)]
            self.humanization_x += 'x{0}={1},'.format(x + 1, value)
            ost -= value
        print(self.humanization_x)

    def solve(self):
        self.construct_table_B()
        self.find_optimal_resource_allocation()

    def print_table_B(self):
        print(self.B)
        print(self.x_with_zero)

a = ResourceAllocation(np.array([[0, 1, 2, 4, 8, 9, 9, 23],
                                [0, 2, 4, 6, 6, 8, 10, 11],
                                [0, 3, 4, 7, 7, 8, 8, 24]]
                                ))
a.solve()
a = ResourceAllocation(np.array([[0, 2, 2, 3, 5, 8, 8, 10, 17],
                                [0, 1, 2, 5, 8, 10, 11, 13, 15],
                                [0, 4, 4, 5, 6, 7, 13, 14, 14],
                                [0, 1, 3, 6, 9, 10, 11, 14, 16]]
                                ))
a.solve()
