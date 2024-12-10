#리스트 함축
#s = [i*2 for i in range(10)]
x = []
for i in range(10):
    x.append(i*2)
print(x) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#위 코드가 아래와 같이 함축된다. 
x = [i*2 for i in range(10)]
print(x) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#리스트의 함축 - 조건식 붙이기
s = [i for i in range(10) if not i % 2 == 0]
print(s) #[1, 3, 5, 7, 9]
s = [i**2 for i in range(10) if i % 2 == 0]
print(s) #[0, 4, 16, 36, 64]

#실습 - 구구단의 각 string을 리스트에 담기
s = []
for i in range(2, 10):
    for j in range(1, 10):
        s.append("%d * %d = %d" % (i, j, i*j))
print(s) #['2 * 1 = 2', '2 * 2 = 4', ..., '9 * 9 = 81 ']

s = ["%d * %d = %d " % (i, j, i*j) for i in range(2,10) for j in range(1, 10)]
print(s) #['2 * 1 = 2', '2 * 2 = 4', ..., '9 * 9 = 81 ']

#교수님 답
s = ['{}*{}={}'.format(x, y, x*y) for x in range(2,10) for y in range(1, 10)]
print(s)

#튜플 
'''
리스트와 유사히지만 불가변성 객체 자료형
요소를 저장할 순 있지만 요소 변경, 추가, 삭제는 할 수 없다.
형식)
튜플 = (요소1, 요소2, ..., 요소n)
튜플 = 요소1, 요소2, ..., 요소n
'''
#튜플 선언
a = (1, 2, 3, 4, 5)
print(a) #(1, 2, 3, 4, 5)
b = 10, 20, 30, 40, 50
print(b) #(10, 20, 30, 40, 50)

#요소 하나인 튜플 - ','가 있어야 튜플이구나를 인식, 없으면 일반 변수(ex. int)로 인식
a = (10)
print(a) #10
print(type(a)) #<class 'int'>

a = (10,)
print(a) #(10,)
print(type(a)) #<class 'tuple'>
a = 10,
print(a) #(10,)
print(type(a)) #<class 'tuple'>

#tuple() : tuple로 converting 하기
a = tuple(range(5))
print(a) #(0, 1, 2, 3, 4)
b = tuple(range(5, 10)) #(5, 6, 7, 8, 9)
print(b)

#리스트를 튜플로 변환하기
a = [1, 2, 3]
a = tuple(a) 
print(a) #(1, 2, 3)

#튜플을 리스트로 변환하기
b = (1, 2, 3)
b = list(b) 
print(b) #[1, 2, 3]

#팩킹 / 언팩킹
#팩킹 - 변수에 리스트나 튜플을 할당하는 과정
a = [1, 2, 3]
b = (1, 2, 3)

#언패킹 - 리스트나 튜플의 요소를 변수 여러 개에 할당하는 것
a, b, c = [1, 2, 3]
d, e, f = (1, 2, 3)
print(type(d)) #<class 'int'>

#튜플 인덱싱
t = (100, 200, 300, 400, 500)
b = t[0] #튜플이라고 t(0) 이렇게 쓰는 것 아님!! 주의하자.
print (b) #100 
print(type(b)) #<class 'int'>
# + 끝자리 인덱스 조심(t[5]하면 indexerror), 튜플의 요소 값은 변경 불가(a[1] = 100 이런 거 불가능!)

#튜플 슬라이싱
t = (1, 2, 'three', 'four')
print(t[2:]) #('three', 'four')
a = t[1:2]
print(a) #(2,)
print(type(a)) #<class 'tuple'> #인덱싱에서는 int로 나왔지만 슬라이싱에서는 튜플로 나오는 것 확인

#튜플 메소드 
'''
a.index(x) : 특정 값의 '인덱스' 반환, 여러 개 있으면 첫 번째 인덱스 반환, 없으면 에러
a.count(x) : 튜플 특정 값의 개수를 반환, 없으면 0
'''
a = (10, 20, 30, 20, 10)
print(a.index(20)) #1
print(a.count(20)) #2

#파이썬 내장함수
#len(): 튜플의 전체 길이
a = (1, 2, 3, 4)
print(len(a)) #4

#sum(): 튜플의 모든 요소의 합
print(sum(a)) #10

#max(): 튜플 요소의 최대값
print(max(a)) #4

#min(): 튜플 요소의 최소값
print(min(a)) #1

#튜플 연산 - 더하면 붙고, 곱하면 뻥튀기 된다!
a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 10)
print(a+b) #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a*2) #(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

#반복문에 사용하기 - for문과 같이 사용
a = (1, 2, 3, 4, 5)
for i in a :
    print(i, end = ' ') #1 2 3 4 5

for i in (1, 2, 3, 4, 5) :
    print(i, end = ' ') #1 2 3 4 5

#튜플의 함축
'''
튜플도 리스트처럼 함축이 가능
단, tuple이라고 적어줘야 함. (리스트처럼 그냥 괄호로 묶는 거 안됨. 제너레이터 객체가 되어버림. )
'''
a = tuple(i for i in range(10) if i % 2 == 0)
print(a) #(0, 2, 4, 6, 8)

#실습 - 더하기 사이클
print("(0~99)의 정수를 입력하세요!")
while True:
    num = int(input("Input: "))
    if num >= 0 and num < 100 :
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")

test = num
Cnt = 0
while True :
    a = test // 10
    b = test % 10
    c = (a + b) % 10
    test = (b*10) + c
    Cnt += 1
    if test == num :
        break
print ("Output: %d" % Cnt)

#실습 - 교수님 답
print ("0~99의 정수를 입력하세요!")

while True:
    num = int(input("Input: "))
    if num >= 0 and num < 100:
        break
    else:
        print ("조건에 맞게 다시 입력해주세요.")

target = num #26
count = 0
while True:
    a = target // 10 #2
    b = target % 10 #6
    c = (a + b) % 10 #8
    target = (b * 10) + c
    count += 1

    if target == num:
        break

print ("Output:{}".format(count))

#실습+@ cycle이 최대 얼마나 도는지 알아보기
s = []
for i in range(100):
    test = i
    Cnt = 0
    while True :
        a = test // 10
        b = test % 10
        c = (a + b) % 10
        test = (b*10) + c
        Cnt += 1
        if test == i :
            break
    print ("Output: %d" % Cnt)
    s.append([Cnt, i])

print(max(s)) #최대 cycle 알아보기
for Cnt, i in s :
    print(i, ":", Cnt, sep = '', end = '  ') #전체 리스트 뽑아보기

#실습 - 오늘은


#교수님 답(option으로 2023까지!)
year = input("2007 or 2023: ")
if year == "2007" :
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
elif year == "2023" :
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week_list = ["SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"]
else :
    print('error')

target = input("Month Day: ") #공백으로 나누려면 입력을 string으로 받아야겠지.
m, d = target.split(' ') #공백으로 나눈 리스트 --> 언팩킹 
m = int(m)
d = int(d) 
if m < 1 or m > 12 :
    print("ERROR(month)")
elif d < 1 or d > month_list[m-1] :
    print("ERROR(day)")
else :
    current = 0 #현재를 1월 0일로 보고 일요일부터 센다. 
    for i in range(m-1):
        current = current + month_list[i]
    current = current + d
    remain = current % 7
    print(week_list[remain])

