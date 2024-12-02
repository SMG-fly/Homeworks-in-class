#9 
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

#10-1
def n_digit_number_sort(arr):
    """
    Args:
      arr: The list of integers where the total number of digits over all the integers in the array is n.

    Returns:
      arr: The sorted array.
    """
    
    # Implement the function here!!
    #
    # Create buckets for each possible length of numbers
    max_digits = len(str(max(arr, key=abs))) # 절댓값이 가장 큰 숫자를 찾고, 자릿수 구하기
    buckets = [[] for _ in range(max_digits + 1)] # max_digits만큼 [](bucket) 생성

    # Place each number in the appropriate bucket based on its length
    for number in arr:
        buckets[len(str(number))].append(number)

    # Sort each bucket using counting sort
    for i, bucket in enumerate(buckets): # bucket: []
        if bucket:  # if the bucket is not empty
            # Apply counting sort for each digit place from least significant digit to most # 뒤에서부터 앞으로 counting sort
            exp = 1 # 1의 자리부터 시작
            max_digit = max(bucket, key=abs)
            while max_digit // exp > 0: # 모든 자리 검사하면 끝
                
                # counting sort by digit
                n = len(bucket)
                output = [0] * n
                count = [0] * 10
                
                # Count occurrences of each digit at the current exponent level
                for j in range(n):
                    index = (abs(bucket[j]) // exp) % 10 # 현재 자릿수에 해당하는 숫자를 추출 # exp 이상 숫자 남긴 뒤 마지막 자리만 남김.
                    count[index] += 1

                # Transform count array to get the actual positions
                for j in range(1, 10):
                    count[j] += count[j - 1] # 자기 앞에 있는 숫자 더하기

                # Build the output array from the end to maintain stable sort
                for j in range(n - 1, -1, -1): # 배열을 끝에서부터 시작하여 처음까지 역순으로 반복
                    index = (abs(bucket[j]) // exp) % 10 # 현재 숫자의 자릿수 출력
                    output[count[index] - 1] = bucket[j] # output 배열의 올바른 위치에 배치
                    count[index] -= 1 # 현재 숫자의 현재 자릿수에 해당하는 숫자의 등장 횟수를 감소
                
                bucket = output 
                exp *= 10 # 다음 10의 자리, 100의 자리로 이동
                
            buckets[i] = bucket

    # Flatten the list of buckets back into our array
    arr = [num for bucket in buckets for num in bucket] # 이중 for문 써서 하나의 array로 병합

    return arr

#10-2
def counting_sort_string(arr):
    """
    Args:
      arr: The list of strings where the total number of characters over all the strings is n.

    Returns:
      arr: The sorted array in the standard alphabetical order.
    """
    
    # Implement the function here!!
    #
    # Find the maximum length of string in arr
    max_length = max(len(s) for s in arr)

    # Perform radix sort starting from the least significant character to the most
    for i in range(max_length-1, -1, -1): # 뒤에 있는 string부터 보겠다! a와 ab를 sorting할 때 i=2라면 a는 그냥 0 반환
        # Initialize buckets for each character (26 lowercase English letters)
        buckets = [[] for _ in range(26)]

        # Place strings into buckets based on the i-th character
        for s in arr:
            # If the string is shorter than the current position, place it in the first bucket
            index = ord(s[i]) - ord('a') if i < len(s) else 0 # ord('a'): 주어진 문자의 ASCII 값을 반환 # 'a'를 빼줌으로써 a를 0번 bucket으로 반환 
            buckets[index].append(s)                           # i번째 숫자 없으면 0 반환

        # Flatten the list of buckets back into arr
        arr = [s for bucket in buckets for s in bucket] # i번째 자리에서 비교 완료 후 펴서 하나의 array로 만든다.-> 다음 비교
        # buckets 안에 알파벳 별로 bucket이 있고 그 안에 있는 '문자열'이 s 인 것이지!

    return arr

