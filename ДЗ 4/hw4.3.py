import numpy as np

# Генерация случайной квадратной матрицы размером 10 на 10
matrix = np.random.rand(10, 10)

# Определение определителя матрицы
det = np.linalg.det(matrix)
# Обработка вырожденной матрицы
if np.isclose(det, 0):
    print("Матрица вырождена, определитель равен:", det)
else:
    print("Определитель матрицы:", det)

# Транспонирование матрицы
transposed_matrix = matrix.T
print("Транспонированная матрица:\n", transposed_matrix)

# Нахождение ранга матрицы
rank = np.linalg.matrix_rank(matrix)
print("Ранг матрицы:", rank)

# Нахождение собственных значений и собственных векторов
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Собственные значения:\n", eigenvalues)
print("Собственные векторы:\n", eigenvectors)

# Генерация второй матрицы размером 10 на 10
matrix2 = np.random.rand(10, 10)

# Сложение двух матриц
sum_matrices = matrix + matrix2
print("Сумма двух матриц:\n", sum_matrices)

# Умножение двух матриц
product_matrices = np.matmul(matrix, matrix2)
print("Произведение двух матриц:\n", product_matrices)
