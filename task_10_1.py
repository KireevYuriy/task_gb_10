import random
import numpy as np

class Matrix:

    def __init__(self, matrix_list):
        self.matrix = matrix_list

    def __str__(self):
        matrix_str = ''
        for string in self.matrix:
            for elem in string:
                matrix_str += f'{elem} '
            matrix_str += '\n'
        return matrix_str

    def __add__(self, other):
        return np.array(self.matrix) + np.array(other.matrix)


def format_matrix(height, length):
    matrix = []
    for st in range(height):
        m_string = []
        for m_str in range(length):
            m_string.append(random.randint(0, 100))
        matrix.append(m_string)
    return matrix


matrix_one = format_matrix(3, 2)
matrix_two = format_matrix(3, 2)

matrix_class_one = Matrix(matrix_one)
matrix_class_two = Matrix(matrix_two)
print(matrix_class_one)
print(matrix_class_two)
print(matrix_class_one + matrix_class_two)
