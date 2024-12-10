#이 코드 오류 있음. 모범 답안이 아님. programming cont_check 제대로 안 됨!!!!!

def continuous_word(word):
    for i in range(len(word)-1):
        if word[i] != word[i + 1]: #현재 문자와 다음 문자가 다른데,
            if word[i] in word[i + 1:]: #현재 문자가 그 이후 문자열에 존재한다면 #fiff
                return False #연속단어가 아니다!!
        else:
            continue
    return True

def make_continuous_word(word): #fffifa
    new_word = ""
    for i in range(len(word)):
        if i == 0 or word[i] not in new_word: #새로운 문자이면
            new_word += word[i] #new_word에 추가
        elif word[i] != word[i-1]: #새로운 문자가 아닌데, 이전 문자와 다르다면
            if (word[i] not in word[:i-1] and word[i] not in word[i+1:]): #현재 문자 앞뒤로 중복되지 않는다면
                    new_word += word[i]
    return new_word

num_words = int(input("number of words? "))
words = []
for i in range(num_words):
    word = input("word? ")
    
    if continuous_word(word):
        print("continuous word!")
    else:
        new_word = make_continuous_word(word)
        if new_word:
            print(new_word)