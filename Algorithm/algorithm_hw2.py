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
    matrix = None
    
    if i == j:
        matrix = arr[i]
    elif i + 1 == j:
        matrix = np.dot(arr[i], arr[j])
    else:
        k = s[i][j] # 분할 지점
        left_product = matrix_chain_multiply(arr, s, i, k)
        right_product = matrix_chain_multiply(arr, s, k + 1, j)
        matrix = np.dot(left_product, right_product)
    
    return matrix
