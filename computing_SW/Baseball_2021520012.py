print ("숫자 야구 게임을 시작합니다!")

#컴퓨터의 답
import random
while True:
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    num3 = random.randint(1,9)
    if (num1 != num2) and (num1 != num3) and (num2 != num3):
        break
num = (num1, num2, num3)

# print(num) #답 확인용

Cnt_S = 0
Cnt_B = 0
Cnt_A = 0
Cnt_O = 0

for i in range(1, 11): 
    Cnt_S = 0
    Cnt_B = 0
    Cnt_O = 0

    #사용자의 답
    pred = input("예상 숫자를 입력하세요: ")
    pred_split = pred.split(",")
    pred_num1 = int(pred_split[0])
    pred_num2 = int(pred_split[1])
    pred_num3 = int(pred_split[2])
    pred_num = (pred_num1, pred_num2, pred_num3)

    #정답 대조
    for j in range(3): 
        if pred_num[j] == num[j] :
            Cnt_S += 1
            Cnt_O += 1
        elif (pred_num[j] == num[0]) or (pred_num[j] == num[1]) or (pred_num[j] == num[2]):
            Cnt_B += 1
            Cnt_O += 1 
    
    #대조 결과
    if (num1 == pred_num1) and (num2 == pred_num2) and (num3 == pred_num3) :
        Cnt_A += 1
        print(i, '회 시도 만에 정답을 맞추셨습니다!')
        break
    elif Cnt_O == 0:
        print(i, "회 시도: 아웃!")
    else: 
        print(i, "회 시도:", Cnt_S, "스트라이크", Cnt_B, "볼!!")

#10회 안에 정답 못 맞출 시 프로그램 종료
if Cnt_A == 0 :
    print("안타깝게도 기회를 모두 사용하셨습니다.")


