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




# Example usage
arr = [50, 4, 666, 797, 3, 2, 1, 1000]
sorted_arr = n_digit_number_sort(arr)
print(sorted_arr)
