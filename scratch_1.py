class Csr:
    def __init__(self):
        self.val = []
        self.col_ind = []
        self.row_ptr = [0]

    def create_matrix(self):
        n = int(input())
        m = int(input())
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
        assert max(self.col_ind) != len(other.row_ptr) - 1, "Невозможное умножение: количество столбцов первой матрицы должно быть равно количеству строк второй."
        n = len(self.row_ptr) - 1  # Количество строк в первой матрице
        m = len(other.col_ind)  # Количество столбцов во второй матрице
        val = self.val
        col_ind = self.col_ind
        row_ptr = self.row_ptr
        result_val = []
        result_col_ind = []
        result_row_ptr = [0]
        for i in range(n):
            row_result = {}
            for j in range(row_ptr[i], row_ptr[i + 1]):
                a_val = val[j]
                a_col = col_ind[j]
                for k in range(other.row_ptr[a_col], other.row_ptr[a_col + 1]):
                    b_val = other.val[k]
                    b_row = other.col_ind[k]
                    if b_row not in row_result:
                        row_result[b_row] = 0
                    row_result[b_row] += a_val * b_val
            for col_ind, val in row_result.items():
                result_val.append(val)
                result_col_ind.append(col_ind)
            result_row_ptr.append(len(result_val))
        return [result_val, result_col_ind, result_row_ptr]

    def add(self, other):
        if (len(self.row_ptr) != len(other.row_ptr)) or (max(self.col_ind) != max(other.col_ind)):
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
        return [result_val, result_col_ind, result_row_ptr]

    def mol_by_scalar(self, scalar):
        matrix_val = self.val
        matrix_col_ind = self.col_ind
        matrix_row_ptr = self.row_ptr
        if scalar != 0:
            new_val = [element * scalar for element in matrix_val]
            return [new_val, matrix_col_ind, matrix_row_ptr]
        return [[], [], []]


    def determinant(self, matrix):
        n = len(matrix)
        if n == 1:
            if matrix[0][0] != 0:
                print(matrix[0][0], 'Да')
            else:
                print('Нет')
            return matrix[0][0]
        det = 0
        for j in range(n):
            minor = [row[:j] + row[j + 1:] for row in matrix[1:]]  # Удаляем первую строку и j-й столбец
            det += (-1) ** j * matrix[0][j] * Csr.determinant(self, minor)  # Рекурсия для вычисления детерминанта

    def csr_to_normal(self, csr_matrix):
        col_ind = csr_matrix[1]
        row_ind = csr_matrix[2]
        print(max(col_ind))
        print(len(row_ind))
        matrix = [[0 for i in range(max(col_ind) + 1)] for j in range(len(row_ind) - 1)]
        val = csr_matrix[0]
        for i in range(len(val)):
            col = col_ind[i]
            row = 0
            for j in range(len(row_ind) - 1):
                if i >= row_ind[j] and i < row_ind[j + 1]:
                    row = j
            matrix[row][col] = val[i]
        return matrix
p = Csr()
print(p.create_matrix())
d = Csr()
print(d.create_matrix())
print(p.add(d))
