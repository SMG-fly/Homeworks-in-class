# 깔끔한 버전
def merge_inversions(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]

    L[n1] = float('inf')  # Use infinity as a sentinel value
    R[n2] = float('inf')
    
    i = 0
    j = 0
    inversions = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            inversions += (n1 - i)  # Count the inversions
            A[k] = R[j]
            j += 1
            
    return inversions



def count_inversion_sub(arr, l, r):
    """
    Args:
      arr: The array to count the number of inversions.
      l: The left index of the array.
      r: The right index of the array.

    Returns:
      cnt: The number of inversions in the array.
    """
    
    # Implement the function here!!
    
    ## Base case: no inversions if there is less than two elements(처음과 끝이 만날 때)
    if l >= r:
        return 0
        
    ## Find the midpoint
    mid = (l + r) // 2
    cnt = 0 # initialize
    
    ## Count inversions in the left half and right half recursively
    left = count_inversion_sub(arr, l, mid)
    right = count_inversion_sub(arr, mid + 1, r)
    cnt = merge_inversions(arr, l, mid, r) + left + right
    
    return cnt

def count_inversion(arr):
    return count_inversion_sub(arr, 0, len(arr) - 1)

# Example usage:
test_arr = [2, 3, 8, 6, 1]
print("Number of inversions:", count_inversion(test_arr))