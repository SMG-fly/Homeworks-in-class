#리스트 == 어레이 같은 느낌

#예제 - 성적의 합계와 평균 출력
score = [100, 80, 95, 90, 70]
sum = score[0] + score[1] + score[2] + score[3] + score[4]
print('성적합계:', sum)
print('성적평균:', sum/5)

#예제 - for문과 같이 사용하기
score = [100, 80, 95, 90, 70]
sum = 0
for i in range(5):
    sum += score[i]
print('성적합계:', sum)
print('성적평균:', sum/5)

#리스트 슬라이싱
'''
특정 범위를 정해서 추출해 내어 새로운 리스트로 만든다.
형식 : 리스트 이름 [시작 인덱스 : 종료 인덱스 : step]
step은 생략 가능(default == 1)
종료 인덱스의 요소는 포함하지 않고 바로 앞 요소까지
'''
score = [100, 80, 95, 90, 70]
a = score[2:4] 
print(a) #[95, 90]
print(score[:2]) #[100, 80]
print(score[2:]) #[95, 90, 70] 

#리스트 요소값 수정
score = [100, 80, 95, 90, 70]
score[2] = 50
print(score) #[100, 80, 50, 90, 70]

#리스트 연산 - 덧셈
a = [101, 102, 103]
b = [201, 202, 203]
print (a + b) #[101, 102, 103, 201, 202, 203]

#리스트 연산 - 곱셈
a = [101, 102, 103]
print(a * 2) #[101, 102, 103, 101, 102, 103]

#리스트 연산 - 비교 연산자
c = [10, 20, 30]
d = [10, 20, 30, 40]
e = [10, 20, 30]
print (c == e) #True
print (c != d) #True
print (c < d) #True
print (c > d) #False

#리스트에 사용 가능한 파이썬 내장 함수
#len() : 리스트의 길이
score = [100, 80, 95, 90, 70]
print(len(score)) #5

#sum() : 리스트 요소의 합
score = [100, 80, 95, 90, 70]
print (sum (score)) #435
print (sum (score) / len(score)) #평균 구하기: 87.0

#max(): 리스트 요소 중 최대값 반환
score = [100, 80, 95, 90, 70]
print(max(score)) #100

#min(): 리스트 요소 중 최소값 반환
score = [100, 80, 95, 90, 70]
print(min(score)) #70

#list(): 시퀀스 자료형(리스트, 튜플, range, 문자열 등)을 리스트로 만들어 줌.
a = range(1, 5) #range(1, 5)
b = list (range (1, 5)) #[1, 2, 3, 4]
c = list("test") #['t', 'e', 's', 't']
print(a, b, c)

#빈리스트 만들기
'''보통 빈 리스트를 만들어 두고 뒤에 새로운 값을 추가하는 방식을 사용함'''
a = [] 
print(a) #[]
b = list()
print(b) #[]

#리스트 메소드
'''
메소드: 객체에 속한 함수를 뜻한다. 
리스트 객체 안에서는 여러가지 유용한 메소드가 제공된다.
score.append(x) --> 이런 식으로 사용한다.

index(x) : 요소 x를 찾아서 해당 '인덱스'를 반환
append(X) : 요소 x를 리스트의 끝에 추가
count(x) : 리스트 내의 '요소의 개수'를 반환
extend[x1, x2] : 리스트[x1, x2]를 기존 리스트 뒤에 추가
insert(index, x) : index 위치에 x를 삽입
remove(x) : 요소 x를 찾아서 리스트에서 삭제
pop(index) : index 위치의 '요소'를 찾아서 반환 후, 해당 요소를 삭제
sort() : 리스트 안의 요소들을 정렬(default: 오름차순, reverse = True 내림차순)
reverse() : 리스트의 요소들을 역순으로 만들어 줌.
clear() : 리스트의 모든 요소들을 삭제하고 빈 리스트가 됨.
copy() : 리스트를 복사해서 또 다른 리스트를 만든다.(깊은 복사<-> a = b 얕은 복사(참조만 복사))
'''
#리스트 요소 추가
a = [1, 2, 3]
a.append(45) 
print (a) #[1, 2, 3, 45]

a = [1, 2, 3] #리스트 안에 리스트 추가 - 중첩 리스트, 길이는 1 증가
a.append([40,50]) 
print (a) #[1, 2, 3, [40, 50]]
print (len(a)) #4

#리스트 확장
a = [1, 2, 3]
a.extend([40, 50])
print(a) #[1, 2, 3, 40, 50]
print(len(a)) #5

#리스트 특정 인덱스에 요소 추가
a = [1, 2, 3]
a.insert (2, 100)
print(a) #[1, 2, 100, 3]
print(len(a)) #4
a.insert(0, 100) #제일 처음에 요소 추가
a.insert(len(a), 100) #제일 마지막에 요소 추가

#리스트 특정 값 삭제
'''해당 값이 없으면 에러 / 해당 값이 두 개 이상이면 첫번째 값 삭제'''
a = [1, 2, 3]
a.remove(2)
print(a) #[1, 3]

#리스트 특정 인덱스 요소 삭제
'''인덱스를 쓰지 않으면 마지막 요소 반환 후 삭제'''
a = [1, 2, 3]
a.pop(1) #터미널에서 치면 무슨 값이 사라지는지 반환 해줌.
print(a) #[1, 3]

a = [1, 2, 3] #pop 대신 del를 사용하는 방법
del a[1]
print(a) #[1, 3]

#실습
list = []
for i in range(5):
    list.append(i)
for i in range(5):
    print("list[%d] = %d" % (i, list[i]))

#실습2
list = []
for i in range(5):
    list.append(5-i)
for i in range(5):
    print("list[%d] = %d" % (i, list[i]))

list = [] #list라는 함수가 있으므로 list라는 변수명을 사용하는 것은 권하지 않는다.
for i in range(11):
    list.append(i/10)
for i in range(11):
    print("list[%d] = %.1f" % (i, list[i])) #소수점 첫째자리까지 =

#리스트 응용
#리스트와 반복문
a = [1, 2, 3, 4, 5]
for i in a:
    print(i) #1 2 3 4 5

#enumnerate()
'''
리스트 요소에 -순서 값을- 부여해주는 함수
시퀀스형(리스트, 튜플, 문자열 등)을 받으면 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
'''

num = ['one', 'two', 'three', 'four']
data = enumerate(num)
print(data) #배열 참조 비슷한 게 뜸 -> for문으로 돌려줘야 한다.
for value in enumerate(num) :
    print(value) #(0, 'one') (1, 'two') (2, 'three') (3, 'four')

for index, value in enumerate(num) : #인덱스와 요소를 같이 출력하려면
    print(index, value) #0 one  1 two   2 three    3 four

#while 반복문으로 요소 출력하기
a = [1, 2, 3, 4, 5]
i = 0
while i < len(a) : # i<=len(a) 으로 사용하면 리스트 범위를 1 넘어감
    print(a[i]) #1  2   3   4   5
    i += 1

#실습
a = []
for i in range(5):
    score = int(input("성적 입력: "))
    a.append(score)
for i in range(5):
    print(i+1, "번째 성적: ", a[i])

a = [[1,2], [3,4], [5,6]]
for i in a:
    for j in i:
        print(j, end = " ")
    print()

#리스트에서 최소값 구하기
score = [100, 80, 95, 90, 70] #최소값 알고리즘 보고 내가 구현한 것
min = score[0]
for i in range(5):
    if min > score[i]:
        min = score[i] 
print(min) #70

score = [100, 80, 95, 90, 70] #책에 적혀있는 것
min = score[0]
for i in score:
    if i < min:
        min = i 
print("최소값:", min) #최소값: 70

#리스트에서 최대값 구하기
score = [100, 80, 95, 90, 70]
max = score[0]
for i in score:
    if i > max:
        max = i
print ("최대값:", max) #최대값: 100

#정렬 이용해서 최소값, 최대값 구하기
score = [100, 80, 95, 90, 70]
score.sort()
min = score[0]
max = score[-1] #방법 1
score.sort(reverse=True) #방법 2
max = score[0]
print("최소값:", min) #최소값: 70
print("최대값:", max) #최대값: 100

#min, max 함수 이용하기
score = [100, 80, 95, 90, 70]
min = min(score)
max = max(score)
print("최소값:", min) #최소값: 70
print("최대값:", max) #최대값: 100

#sum 함수로 요소의 합 구하기
score = [100, 80, 95, 90, 70]
sum = sum(score)
print("성적합계:", sum) #성적합계: 435
print("성적평균:", sum / len(score)) #성적평균: 87.0

#2차원 리스트
'''
a[0][0] a[0][1]
a[1][0] a[1][1]
'''
#2차원 리스트 만들기
a = [[1,2], [3,4], [5,6]]
print(a) #[[1, 2], [3, 4], [5, 6]]
a = [[1,2],
     [3,4], 
     [5,6]] #보기 쉽게
print(a) #[[1, 2], [3, 4], [5, 6]]

#반복문으로 2차원 리스트 요소 출력하기
a = [[1,2], [3,4], [5,6]]
for x,y in a :
    print(x, y) #1 2    3 4    5 6 

a = [[1,2], [3,4], [5,6]] #중첩 for문 사용하기 
for i in a :
    for j in i : 
        print(j, end = ' ')
    print() 
    #1 2    3 4    5 6 

a = [[1,2], [3,4], [5,6]] #while문 한 번 사용하기 
i = 0
while i < len(a) :
    x, y = a[i]
    print(x, y) #1 2    3 4    5 6 
    i += 1

#여기서부터 다시 보기 - for문과 다른 점 유의하기!!
a = [[1,2], [3,4], [5,6]] #중첩 while문 사용하기 
i = 0
while i < len(a):
    j = 0 
    while j < len(a[i]):
        print (a[i][j], end=' ') 
        j += 1
    print()
    i += 1 
    #1 2    3 4     5 6