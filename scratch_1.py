class Csr:
    def __init__(self, val, col_ind, row_ptr, scalar):
        self.val = val
        self.col_ind = col_ind
        self.row_ptr = row_ptr
        self.scalar = scalar

    def create_matrix(self):
        m = int(input())
        n = int(input())
        trace = 0
        matrix = list()
        for iterations in range(n):
            matrix += [list(map(int, input().split()))]
        for i in range(n):
            counter = 0
            for j in range(m):
                if matrix[i][j] != 0:
                    self.val.append(matrix[i][j])
                    self.col_ind.append(j)
                    counter += 1
            self.row_ptr.append(self.row_ptr[i] + counter)
        return [self.val, self.col_ind, self.row_ptr]

    def mol(self, other):
        assert len(self.col_ind) == len(
            other.row_ptr) - 1, "Невозможное умножение: количество столбцов первой матрицы должно быть равно количеству строк второй."
        n = len(self.row_ptr) - 1  # Количество строк в первой матрице
        m = len(other.col_ind) - 1  # Количество столбцов во второй матрице
        result_val = []
        result_col_ind = []
        result_row_ptr = [0]
        for i in range(n):
            row_result = {}
            for j in range(self.row_ptr[i], self.row_ptr[i + 1]):
                a_val = self.val[j]
                a_col = self.col_ind[j]
                for k in range(other.row_ptr[a_col], other.row_ptr[a_col + 1]):
                    b_val = other.val[k]
                    b_row = other.col_ind[k]
                    if b_row not in row_result:
                        row_result[b_row] = 0
                    row_result[b_row] += a_val * b_val
            for self.col_ind, self.val in row_result.items():
                result_val.append(val)
                result_col_ind.append(col_ind)
            result_row_ptr.append(len(result_val))
        self.val = result_val
        self.col_ind = result_col_ind
        self.row_ptr = result_row_ptr
        return Csr.create_matrix(self.n, self.m, result_val, self.col_ind, self.row_ptr)

    def add(self, other):
        if len(self.row_ptr) != len(other.row_ptr):
            raise ValueError("Матрицы должны иметь одинаковое число строк.")
        result_val = []
        result_col_ind = []
        result_row_ptr = [0]
        i = 0
        j = 0
        while i < len(self.val) or j < len(other.val):
            if i < len(self.val) and (j == len(other.val) or self.col_ind[i] <= other.col_ind[j]):
                result_val.append(self.val[i])
                result_col_ind.append(self.col_ind[i])
                i += 1
            if j < len(other.val) and (i == len(self.val) or other.col_ind[j] < self.col_ind[i]):
                result_val.append(other.val[j])
                result_col_ind.append(other.col_ind[j])
                j += 1
            if i < len(self.val) and j < len(other.val) and self.col_ind[i] == other.col_ind[j]:
                result_val.append(self.val[i] + other.val[j])
                result_col_ind.append(self.col_ind[i])
                i += 1
                j += 1
            if i == self.row_ptr[len(result_row_ptr) - 1]:
                result_row_ptr.append(len(result_val))
        return Csr.create_matrix(result_val, result_col_ind, result_row_ptr)

def mol_by_scalar(self, matrix):
    matrix_val = matrix[0]
    matrix_col_ind = matrix[1]
    matrix_row_ptr = matrix[2]
    if self.scalar != 0:
        new_val = [element * self.scalar for element in matrix_val]
        return new_val, matrix_col_ind, matrix_row_ptr
    return [[], [], []]


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    f = 0
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in matrix[1:]]  # Удаляем первую строку и j-й столбец
        det += (-1) ** j * matrix[0][j] * determinant(minor)  # Рекурсия для вычисления детерминанта
        if det == 0:
            f = 1
    return det, f


if f==1:
    print(det,'Да')
else:
    print('Нет')
val = []
col_ind = []
row_ptr = [0]
scalar = 0
pdiddy = Csr(val, col_ind, row_ptr, scalar)
pdiddy.create_matrix()