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
            val = self.val
            col_ind = self.col_ind
            row_ptr = self.row_ptr
        return [val, col_ind, row_ptr]

    def trace(self):
        trace = 0
        val = self.val
        col_ind = self.col_ind
        row_ind = self.row_ptr
        if max(col_ind) + 1 != len(row_ind) - 1:
            return "error, not a square matrix"
        for i in range(len(val)):
            if (i >= row_ind[col_ind[i]]) and (i < row_ind[col_ind[i] + 1]):
                trace += val[i]
        return trace

    def display_element(self, row, col):
        row1 = row - 1
        col1 = col - 1
        val = self.val
        col_ind = self.col_ind
        row_ind = self.row_ptr
        element = 0
        for i in range(len(val)):
            if (col_ind[i] == col1) and (i >= row_ind[row1]) and (i < row_ind[row1 + 1]):
                element = val[i]
        return element
    def mol(self, other):
        if max(self.col_ind) + 1 != len(other.row_ptr) - 1:
            return "ошибка, матрицы не могут быть перемножены, потому что количсетво столбцов в первой матрице не равно количеству строк во второй"
        n = len(self.row_ptr) - 1  # Количество строк в первой матрице
        val = list(int())
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
            return "Матрицы должны иметь одинаковое число строк"
        result_val = []
        result_col_ind = []
        result_row_ptr = [0]
        val1 = self.val
        col_ind1 = self.col_ind
        row_ptr1 = self.row_ptr
        val2 = other.val
        col_ind2 = other.col_ind
        row_ptr2 = other.row_ptr
        matrix1 = Csr.csr_to_normal(self, [val1, col_ind1, row_ptr1])
        matrix2 = Csr.csr_to_normal(self, [val2, col_ind2, row_ptr2])
        resmatrix = [[(matrix1[i][j]+matrix2[i][j]) for j in range(max(col_ind1)+1)] for i in range(len(row_ptr1) - 1)]
        for i in range(len(row_ptr1) - 1):
            counter = 0
            for j in range(max(col_ind1)+1):
                if resmatrix[i][j] != 0:
                    result_val.append(resmatrix[i][j])
                    result_col_ind.append(j)
                    counter += 1
            result_row_ptr.append(result_row_ptr[i] + counter)
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
                inv_mt = 'Да'
            else:
                inv_mt = 'Нет'
            return matrix[0][0], inv_mt
        det = 0
        for j in range(n):
            minor = [row[:j] + row[j + 1:] for row in matrix[1:]]  # Удаляем первую строку и j-й столбец
            det += (-1) ** j * matrix[0][j] * Csr.determinant(0, minor)[0]  # Рекурсия для вычисления детерминанта
        if det != 0:
            inv_mt = 'Да'
        else:
            inv_mt = 'Нет'
        return [det, inv_mt]

    def csr_to_normal(self, csr_matrix):
        col_ind = csr_matrix[1]
        row_ind = csr_matrix[2]
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
m = p.create_matrix()
print(m)
#d = Csr()
#print(d.create_matrix())
#print(p.mol(d))
#print(p.add(d))
#print(p.trace())
print(p.display_element(2,3))
#print(p.determinant(Csr.csr_to_normal(0, m))[0])
#print(p.determinant(Csr.csr_to_normal(0, m))[1])
#print(p.mol_by_scalar(4))

