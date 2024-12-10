your_num = []
for i in range(1,7):
    n = int(input("Lottery Number(%d): "% i))
    if n in your_num:
        print("중복된 숫자입니다. 다시 입력해주세요.")
        break
    else:
         your_num.append(n)
            
        
win = [15, 23, 29, 34, 40, 44]
bonus = 20

def lotto(prize, money):
    print (prize,"prize:", money, "won")

if len(your_num) < 6:
    pass

else: 
    Cnt = 0
    for i in range(6):
        if your_num[i] in win:
            Cnt += 1
        
    print("Your numbers:", your_num)    
    print("Winning numbers:", win, "+", bonus)

    if Cnt == 6 :
        lotto("1st","3,000,000,000")
    elif Cnt == 5 and bonus in your_num:
       lotto("2nd","50,000,000")
    elif Cnt == 5:
        lotto("3rd","1,500,000")
    elif Cnt == 4:
        lotto("4th","50,000")
    elif Cnt == 3:
        lotto("5th","5,000")
    elif Cnt <= 2:
        print("no prize")
        