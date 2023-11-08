#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = [[integer ** 2 for integer in row] for row in matrix]
    return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = square_matrix_simple(matrix)
for row in result:
    print(row)
