import numpy as np

def threshold_function(matrix):
    return np.where(matrix < 0, 0, 1)

# 예시
matrix = np.array([[-1, 2, -3], [4, -5, 6]])
result = threshold_function(matrix)

print(result)