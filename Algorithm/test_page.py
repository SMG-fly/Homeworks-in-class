import numpy as np

def matrix_chain_multiply(arr, s, i, j):
    """
    Args:
    arr: The array of matrices.
    s: The table computed by MATRIX-CHAIN-ORDER.
    i: The left index of the array.
    j: The right index of the array.

    Returns:
    matrix: The result of the matrix chain multiplication.
    """
    if i == j:
        return arr[i-1]
    else:
        k = s[i][j]
        left_product = matrix_chain_multiply(arr, s, i, k)
        right_product = matrix_chain_multiply(arr, s, k + 1, j)
        return np.dot(left_product, right_product)

# Example matrices
A1 = np.array([[1, 2], [3, 4]])
A2 = np.array([[5, 6], [7, 8]])
A3 = np.array([[9, 10], [11, 12]])

# Array of matrices
arr = [A1, A2, A3]

# Example s table computed by MATRIX-CHAIN-ORDER (hypothetical values)
s = [[0, 0, 0, 0], 
     [0, 0, 1, 1], 
     [0, 0, 0, 2], 
     [0, 0, 0, 0]]

# Indices for the full range
i = 1
j = len(arr)

# Compute the result
result = matrix_chain_multiply(arr, s, i, j)
print(result)
