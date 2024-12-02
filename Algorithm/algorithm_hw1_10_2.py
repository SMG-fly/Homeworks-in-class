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

# Example usage:
strings = ["banana", "apple", "cherry", "date", "a", "ab", "b"]
sorted_strings = counting_sort_string(strings)
print("Sorted strings:", sorted_strings)