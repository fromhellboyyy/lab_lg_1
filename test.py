j = 0
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
minor = [row[:j] + row[j + 1:] for row in matrix[1:]]

print(minor)