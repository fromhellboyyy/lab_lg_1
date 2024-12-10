class csr:
    def create_matrix():
        m = int(input())
        n = int(input())
        val = []
        trace = 0
        col_ind = []
        row_ind = [0]
        matrix = list()
        for iterations in range(n):
            matrix += [list(map(int, input().split()))]
        for i in range(n):
            counter = 0
            for j in range(m):
                if matrix[i][j] != 0:
                    val.append(matrix[i][j])
                    col_ind.append(j)
                    counter += 1
            row_ind.append(row_ind[i] + counter)
        return [val, col_ind, row_ind]


print(csr.create_matrix())
#meow
class csr:
    def __init__(self, val, col_ind, row_ptr):  # Исправлено на row_ptr
        self.val = val
        self.col_ind = col_ind
        self.row_ptr = row_ptr  # Исправлено на row_ptr

    def add(self, other):
        if len(self.row_ptr) != len(other.row_ptr):
            raise ValueError("Матрицы должны иметь одинаковое число строк.")

        result_val = []
        result_col_ind = []
        result_row_ptr = [0]  # Исправлено на row_ptr

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

        return csr(result_val, result_col_ind, result_row_ptr)

    def mol_by_scalar(matrix):
        val = matrix[0]
        col_ind = matrix[1]
        row_ind = matrix[2]
        if scalar!=0:
            new_val = [element * scalar for element in val]
            return new_val, col_ind, row_ind
        return [[], [], []]



def mol(self, other):
    assert len(self.col_ind) == len(other.row_ind) - 1, "Невозможное умножение: количество столбцов первой матрицы должно быть равно количеству строк второй."

    n = len(self.row_ind) - 1  # Количество строк в первой матрице
    m = len(other.col_ind) - 1  # Количество столбцов во второй матрице

    result_vals = []
    result_col_ind = []
    result_row_ind = [0]

    for i in range(n):
        row_result = {}

        for j in range(self.row_ind[i], self.row_ind[i + 1]):
            A_val = self.val[j]
            A_col = self.col_ind[j]

            for k in range(other.row_ind[A_col], other.row_ind[A_col + 1]):
                B_val = other.val[k]
                B_row = other.col_ind[k]

                if B_row not in row_result:
                    row_result[B_row] = 0
                row_result[B_row] += A_val * B_val

        for col, val in row_result.items():
            result_vals.append(val)
            result_col_ind.append(col)

        result_row_ind.append(len(result_vals))

    return CSR(n, m, result_vals, result_col_ind, result_row_ind)


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    f=0
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in matrix[1:]]  # Удаляем первую строку и j-й столбец
        det += (-1) ** j * matrix[0][j] * determinant(minor)  # Рекурсия для вычисления детерминанта
        if det==0:
            f=1


    return [det, f]

if f==1:
    print(det,'Да')
else:
    print('Нет')
