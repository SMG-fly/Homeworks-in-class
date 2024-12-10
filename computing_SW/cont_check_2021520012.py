
    
def is_cont (word): 
    word_test = []
    for i in range(len(word)): 
        if i == 0 :
            word_test.append(word[i])
        else:
            if word[i] not in word_test:
                word_test.append(word[i])
            else:
                if word[i] != word[i-1]:
                    return False
    return True

       
def not_cont(word):
    result = ''
    word_test = []
    Cnt = 0
    for i in range(len(word)):
        if i == 0 :
            result += word[i]
            word_test.append(word[i])
        else:
            if word[i] not in word_test:
                Cnt = 0
                result += word[i]
                word_test.append(word[i])
            else: 
                if word[i] != word[i-1]:
                    Cnt = 1
                else:
                    if Cnt == 0:
                        result += word[i]
                    else:
                        pass
                
    print(result)
                
            
words = []

cycle = int(input('number of words? '))

for i in range(cycle):
    ans = input('word? ')
    words.append(ans)
    
for word in words:
    if is_cont(word):
        print("continuous word!")
    else:
        not_cont(word)