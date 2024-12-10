#얘가 그래도 속이 편함... 근데 programmmmmmming은 progamin 출력해버리는데??

def is_continuous(word):
    for i in range(len(word) - 1): # 범위가 len(word) - 1인 이유는, 아래 조건문에서 word[i+1]을 비교하기 때문.
        if word[i] != word[i + 1]: # 현재 문자가 다음 문자와 다르면서,
            if word[i] in word[i + 1:]: # 현재 문자가 다음 문자 이후 문자열에 존재하면 연속 단어가 아님. 
                return False
    return True

def make_continuous_word(word):
    continuous_word = "" 
    checked = [] # 이전에 등장한 문자들을 저장할 리스트

    for i in range(len(word)): #단어의 모든 문자에 대해 반복
        if word[i] not in checked: # 만약 현재 문자가 이전에 등장하지 않은 문자라면,
            checked.append(word[i]) # 그 문자를 checked에 추가하고,
            continuous_word += word[i] # 연속 단어에도 추가.
        else: # 현재 문자가 이미 등장한 문자라면,
            if (word[i] == word[i - 1] and # 현재 문자가 이전 문자와 같으면서,
                (word[i] not in word[:i - 1] and word[i] not in word[i + 1:])): 
                # 현재 문자와 이전 문자 이외 구역(word[k] s.t. k < i - 1 and k > i)에는 같은 문자가 없어야 함. 
                continuous_word += word[i]
    return continuous_word

def check_valid(word): # 입력된 문자가 모두 소문자인지 검사하는 함수
    for i in range(len(word)):
        if word[i].isupper(): # isupper()는 문자열이 모두 대문자라면 True를 반환. 여기서는 문자열의 문자 하나씩 검사함.
            return False
    return True



N = int(input("number of words? "))
word_list = []

while len(word_list) < N:
    word = input("word? ")
    if check_valid(word):
        word_list.append(word)
    else:
        print("invalid input.")

for i in range(N):
    if is_continuous(word_list[i]):
        print("continuous word!")
    else:
        print(make_continuous_word(word_list[i]))