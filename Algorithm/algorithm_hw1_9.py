
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
    
    # Merge step (similar to merge sort)
    n1 = mid - l + 1 # 왼쪽 subarray의 요소 수 # l은 포함해야지.
    n2 = r - mid # 오른쪽 subarray의 요소 수 # mid 포함 X
    
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    
    for i in range(n1):
        L[i] = arr[l + i] # [l:mid + l]
    for j in range(n2):
        R[j] = arr[mid + j + 1] # [mid + 1:r + 1]
    
    L[n1] = float('inf')  # Use infinity as a sentinel value
    R[n2] = float('inf')
    
    i = 0  # Initial index of the first subarray 
    j = 0  # Initial index of the second subarray 
    inversions = 0
    
    for k in range(l, r + 1):
        if L[i] <= R[j]: # 앞 절반, 뒷 절반 순차적으로 비교
            arr[k] = L[i]
            i += 1
        else:
            inversions += (n1 - i)  # L에 남은 숫자들 다 inversion(이미 통과한 i개 제외)
            arr[k] = R[j]
            j += 1
            
            
    cnt = inversions + left + right
    return cnt

def count_inversion(arr):
    return count_inversion_sub(arr, 0, len(arr) - 1)

# Example usage:
test_arr = [2, 3, 8, 6, 1]
print("Number of inversions:", count_inversion(test_arr))