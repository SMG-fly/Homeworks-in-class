#반복문

#무한루프 - 종료는 Crtl+C
'''
i = 0
while i < 3 :
    print("Hello World!!")
    i = i-1
'''

#0-9 출력하기
i = 0
while i < 10 :
    print (i, end=" ") #default는 \n, end = " "로 숫자들을 한 줄에 정렬해준다.
    i +=1

#실습 - Hello World 반복
i = 1
while i < 8 :
    print (i, "번째 Hello World!!") #default가 \n이기 때문에 따로 \n 붙일 필요 X
    i +=1                           #i=0부터 하고 print i + 1 할 수도 있겠지.

i = 0
while i < 7 :
    i +=1
    print (i, "번째 Hello World!!") 
   
#실습 - 구구단
num = int(input("출력하고 싶은 단: "))
i = 1
while i < 10 :
    ans = num * i
    print(num, "*", i, "=", ans)
    i += 1

#실습~
num = int(input("양의 정수 입력"))
i = 1
if num > 0 :
    while i <= num :
        print(i, end = " ")
        i += 1
    print()

num = int(input("양의 정수 입력"))
if num > 0 :
    while num > 0 :
        print(num, end = " ")
        num -= 1
    print()

#
num = int(input("양의 정수 입력: "))
i = 2
while i <= num :
    print (i, end = " ")
    i *= 2
print()

num = int(input("양의 정수 입력: "))
i = 1
three = 1
while i <= num :
    three = 3 * i
    print (three, end = " ")
    i += 1
print()
#교수님 답
num = int(input("양의 정수 입력: "))
i = 0
cnt = 0
while cnt < num :
    cnt += 1
    i += 3
    print(i)
print()

num1 = int(input("정수 입력: "))
num2 = int(input("정수 입력: "))
if num1 <= num2 :
    small = num1
    big = num2
else : 
    small = num2
    big = num1
while small <= big : #my tip: 틀린 조건이 아니라 맞는 조건이 들어가야 함. 
    print(big)
    big -= 1
print() 


#예제 - 누적합 구하기
num = int(input("양의 정수 입력: "))
i = 1
sum = 0 #밖에서 변수 지정 꼭 해줄 것
while i <= num :
    sum += i
    i += 1
print ("1부터", num, "까지의 합은", sum, "입니다.")

#실습
num1 = int(input("몇 개의 정수를 입력할까요? "))
i = 1
sum = 0

while i <= num1 :
    num2 = int (input("정수 입력: "))
    i += 1
    sum += num2

print("합계는", sum, "입니다.")

#실습 - 정수의 각 자리수의 합 구하기
num = int(input("정수 입력: "))

sum = 0
digit = 1

while num > 0 :
    digit = num % 10 #1의 자리 빼내기
    sum += digit    
    num = num // 10 # 10의 자리로 자리 이동
print ("합계는", sum, "입니다.")
#교수님 - string으로 받아서 나누기
num = input("정수 입력: ")
total = len(num)
sum = 0
i = 0
while i < total :
    sum += int(num[i]) 
    i += 1
print ("합계는", sum, "입니다.")


#종료 보초값 이해하기 
n = 0 #학생 수
sum = 0
score = 0
avg = 0
print ("종료하려면 음수를 입력하세요")
#score가 0이상이면 반복
#성적을 입력받아서 합계를 구하고 학생 수를 센다.
while score >= 0 :  #종료 보초값은 음수
    score = int(input("성적 입력: "))
    if score > 0:
        sum += score
        n += 1
#평균을 계산하고 화면에 출력한다.
if n > 0 :
    avg = sum / n
print("성적의 평균은 %f입니다." % avg)

#최대값 구하기 알고리즘
max = -1 #나올 수 없는 최저값을 임시로 저장
n = int(input("양의 정수 입력: "))
while n >= 0 :  #종료보초값(음수)를 넣으면 작동 종료
    if n > max :
        max = n
    n = int(input("양의 정수 입력: "))
if max != -1 :
    print("최대값은", max, "입니다.")

#난수
'''
파이썬에서 난수를 생성하려면 random 모듈이 필요 -> import random
random.randint(시작 값, 끝 값) 사용하면 정수로 난수 발생
'''

#예제
import random
num = random.randint(1,10) #1~10까지 중에서 랜덤 / 1, 10도 포함
print(num)

#실습 - 주사위 굴리기
import random 
num = 0

while num != 3 : 
    num = random.randint(1, 6)
    print("주사위를 굴렸다.", num, "나옴")

print("드디어 3 나와서 종료")

#실습 - 구구단 게임
print("구구단 게임입니다.")

import random

i = 1
Cnt = 0 #Score
while i <=3 :
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    
    gob = num1 * num2
    print(num1, "*", num2, "=", end = " ")
    ans1 = int(input())
    if (ans1 == gob) :
        print("맞습니다.")
        Cnt += 1
    else :
        print("틀렸습니다.")
    i+=1
print("총 3문제 중", Cnt, "문제 맞추셨습니다.")

#실습 - 가위바위보 게임
import random
print ("이길 때까지 계속합니다.")
user_num = -1
outcome = -500
win = 0

while win == 0:
    user = input("가위, 바위, 보 중 하나를 선택: ")

    computer_num = random.randint(1,3)
    if computer_num == 1 :
        print("컴퓨터: 가위")
    elif computer_num == 2 :
        print("컴퓨터: 바위")
    elif computer_num == 3 :
        print("컴퓨터: 보")

    if user == "가위": #가위
        if computer_num == 1:
            print("비겼다")
        elif computer_num == 2:
            print("졌다")
        elif computer_num == 3:
            print("이겼다")
            win += 1
    elif user == "바위": #바위
        if computer_num == 1:
            print("이겼다")
            win += 1
        elif computer_num == 2:
            print("비겼다")
        elif computer_num == 3:
            print("졌다")
    elif user == "보": #보
        if computer_num == 1:
            print("졌다")
        elif computer_num == 2:
            print("이겼다")
            win += 1
        elif computer_num == 3:
            print("비겼다")
            

#for
for i in [0, 1, 2] :
    print(i)    #0 \n 1 \n 2 \n

for i in "Hello" :
    print(i)    #H \n e \n l \n l \n o

fruits = ('apple', 'orange', 'grape')
for i in  fruits :
    print (i)   #apple \n orange \n grape

#실습 - 5단 출력
for i in [1, 2, 3, 4, 5, 6, 7 ,8, 9] :
    ans = 5 * i
    print ("5 *", i, "=", ans)

#실습 - 합격/불합격 프로그램
score = [90, 35, 75, 69, 80]
num = 1
ans = ""

for s in score :

    if s >= 70 :
        ans = "합격"
    else :
        ans = "불합격"

    print(num,"번 학생 점수는", s, "이고", ans)
    num += 1

#for문과 range() 사용하기
for i in range(3):
    print (i)   # 0 \n 1 \n 2

#range(start, stop, step) 
'''
시작, 끝, 증감값 
start, step 생략 가능 / stop은 반드시 지정해야 함
start 부터 stop-1까지의 숫자 생성
생성하는 값을 실제로 리스트 자료형을 보고 싶으면 list(range(3)) 이런 식으로 사용
'''
for i in range(0, 10, 2) :
    print(i, end = " ")     # 0 2 4 6 8

for i in range(10, 0, -1) : #숫자를 감소시키고 싶을 때는 step에 음수를 넣어준다. range(start = 10, stop = 0) 이런식으로 하면 결과 없음
    print(i, end = " ")     # 10 9 8 7 6 5 4 3 2 1

for i in reversed(range(3)) : #숫자를 감소시키는 방법2, 순서를 뒤집는다.
    print(i, end = " ")     # 2 1 0
  
#예제 - 1부터 10까지 모든 수의 합
sum = 0 #변수 미리 지정하기, 잊지 말자!
for i in range(10) :
    sum += (i+1)
print (sum)

#예제 - 입력한 횟수대로 반복하는 프로그램
count = int(input("반복할 횟수를 입력하세요: "))
for i in range(count):
    i = i+1
    print('Hello World', i)

#실습 - 1부터 num까지 합
sum = 0 #변수 미리 지정하기, 잊지 말자!
num = int(input("어디까지 계산할까요? "))
for i in range(num):
    i = i+1
    sum += i
print("1부터", num, "까지의 정수의 합:", sum)

#예제 - 구구단
dan  = int(input("단: "))
for i in range(9):
    i = i + 1
    ans = dan * i
    print (dan, "*", i, "=", ans)
#짧은 버전
dan = int(input("단: "))
for i in range(1, 10) :
    print(dan, "*", i , "=", dan*i)

#실습 - 작은 수부터 큰 수까지의 합
num1 = int(input('정수 입력: '))
num2 = int(input('정수 입력: '))
if num1 > num2 :
    big = num1
    small = num2
else :
    big = num2
    small = num1

sum = 0 #변수 지정, 잊지 말자!
for i in range(small, big+1) :
    sum += i
print(small, "에서", big, "까지 더하면", sum)

#반복문의 변수 i값을 임의로 변경해도 다시 반복되면서 정상 값이 들어간다. -> 전체 반복에 영향을 끼치지 않는다.
for i in range(10):
    print(i , end=' ')
    i = 10      # 0 1 2 3 4 5 6 7 8 9 

#break, continue로 반복문 제어하기
'''
#break
반복문 동작 중간에 종료하고 나오고 싶을 때 사용
제어 흐름 중단
while True: 로 무한루프 만들고 특정 조건 만족 시 break로 빠져나오는 방식을 사용할 수 있다.

#continue
반복문을 실행할 때 입력 조건을 검사해서 조건에 맞지 않으면 맨 처음으로 다시 돌아가게 할 때 사용
제어 흐름 유지 
'''
#break
#while에서 break 사용하기 - 무한루프 탈출
i = 0
while True:     #무한루프
    print(i, end = " ")
    i += 1
    if i == 10:     #특정조건 만족 시
        break       #반복문 종료
print()
print('무한루프 탈출')

#for에서 break 사용하기
for i in range(10000) :
    print(i, end = " ")
    if i == 10 :
        break
print()
print("반복문 탈출")

#continue
#while 반복문에서 continue로 코드 실행 건너뛰기
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue #i가 2의 배수이면(조건 충족) continue 실행(아래 코드를 실행하지 않고 건너뜀)
    print(i, end = " ")
    # 1 3 5 7 9 

#for 반복문에서 continue로 코드실행 건너뛰기
for i in range(10):
    if i % 2 == 0:
        continue # 아래 코드를 실행하지 않고 건너 뜀
    print(i, end = " ") 
    # 1 3 5 7 9 

#pass문
'''
for, while의 반복할 코드에서는 아무 일도 하지 않지만 반복문의 형태는 유지하고 싶을 때 사용
나중에 작성해야할 코드를 표시하는 용도
if문에서도 사용했다!
'''
for i in range(10):
    pass    #아무 일도 일어나지 않음
'''
while True:
    pass #무한루트 종료하려면 Ctrl + C
'''

#중첩 반복문 - 반복문 안에 반복문이 들어가는 형태
for i in range(3) :
    for j in range(2) :
        print (i, end =' ') #세로 1이 i, 2는 j
        print(j)
    print() #그냥 줄바꿈

#사각형 모양 출력하기
for i in  range(3) :
    for j in range(5):
        print('*', end = ' ')
    print()

#실습
floor = int(input("층수: "))
for i in range(floor):
    i += 1
    for j in range(i):
        print('*', end = '')
    print()

floor = int(input("층수: "))
for i in range(floor, 0, -1):
    for j in range(i):
        print('*', end = '')
    print()

for i in range(2, 10):
    for j in range(1, 10):
        print(i,"*",j,'=',i*j)
    print() #2단과 3단 사이 띄기
    







