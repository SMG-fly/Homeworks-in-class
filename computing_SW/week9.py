#요세푸스 - 내가 푼 건데, 4번째부터 제대로 안 나와...ㅎㅎ
n = int(input("1번부터 N번까지: "))
k = int(input("k번째 사람: "))

list = []
for i in range(1, n+1):
    list.append(i)
    
list_new = []
for i in range(1, n+1):
    k_new = ((k-1)*i) % len(list) #이런 식으로 계산 X, len 넘을 때만 한 번 다음 사이클 돌도록 pivot 쓰는 게 맞음
    new_one = list[k_new]
    list.remove(new_one)
    list_new.append(new_one)
    
print (list_new)

#교수님 플이
N = 7
K = 3

member = list(range(1, N+1)) # 1 2 3 4 5 6 7 
removed = []

pivot = 0
while True:
    if len(member) == 0:
        break
    
    pivot = pivot + K - 1
    if pivot >= len(member):
        pivot = pivot % len(member)
    removed.append(member.pop(pivot))
    
print(removed)

print("<", end='')
for i in range(len(removed)):
    if not i == len(removed)-1: #removed 리스트에 있는 마지막 숫자가 아니면
        print(removed[i], end = ', ')
    else:
        print(removed[i], end= '>')
        
#익명 함수(lamda)
'''
lambda 인자 : 표현식
'''
def add(x, y):
    return x + y
print( add(5, 3) ) #8

print( (lambda x, y: x+y)(5, 3) ) #8 #위 함수와 같은 효과

add = lambda x, y: x+y #변수에 람다 표현식 할당 가능 
print( add(5, 3) )

#map
'''
반복 가능한 객체를 지정된 함수로 처리해주는 함수
map(함수, 반복 가능한 자료형(리스트, 튜플 등))
map 함수의 반환값은 map 객체이기 때문에 list 또는 tuple로 변환해주어야 함. 
'''
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
print (a) #[1, 2, 3, 4]

a = [1.2, 2.5, 3.7, 4.6] #위 함수를 아래와 같이 map으로 간단히 표현 가능!
a = list(map(int, a))
print(a)

a = list(map(str, range(10))) #list외에 모든 반복 가능한 객체를 넣을 수 있다. 
print(a) #['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

a, b = map(int, input('숫자 두 개를 입력하세요: ').split()) 
print(a, b)

a, b = input('숫자 두 개 입력: ').split() #위와 같은 함수(풀어서) #이렇게 하면 띄어쓰기로 숫자 두 개 받을 수 있겠다!
a = int(a)
b = int(b)

#lambda & map
a = list(map(lambda x: str(x) if x % 3 == 0 else x, range(1,11)))
print(a) #[1, 2, '3', 4, 5, '6', 7, 8, '9', 10]

a = list(map(lambda x: str(x) if x % 3 == 0 else x+10 , range(1,11))) #lambda x: 없으면 x가 (인자로) 선언이 안 됨.
print(a) #[11, 12, '3', 14, 15, '6', 17, 18, '9', 20]

#딕셔너리
'''
딕셔너리 = {키1:값1, 키2:값2, ..., 키n:값n}
자료의 순서 X -> 인덱스로 접근 X
'''
contacts = {'홍길동':'010-1234-1234',
            '최민우':'010-5678-5678',
            '김경태':'010-1357-5621'}
print(contacts) #{'홍길동': '010-1234-1234', '최민우': '010-5678-5678', '김경태': '010-1357-5621'}
print(contacts['최민우']) #010-5678-5678

#항목 추가하기
person = {'name':'홍길동', 'phone':'010-1234-5678'}
print(person) #{'name': '홍길동', 'phone': '010-1234-5678'}

person['age'] = 23
print(person) #{'name': '홍길동', 'phone': '010-1234-5678', 'age': 23}

person['score'] = [100, 90, 95] #튜플도 넣어지고, 딕셔너리도 넣어짐
print(person) #{'name': '홍길동', 'phone': '010-1234-5678', 'age': 23, 'score': [100, 90, 95]}

#항목 삭제하기
del person['age'] #key 넣어서 삭제하기 #만약 없는 키를 넣는다면? KeyError
print(person) #{'name': '홍길동', 'phone': '010-1234-5678', 'score': [100, 90, 95]}

person.pop('score') #key에 해당하는 value값을 '반환(return임, 출력 아님)'하고 해당 항목을 삭제
print(person) #{'name': '홍길동', 'phone': '010-1234-5678'}

#항목 접근하기
'''
리스트나 튜플은 인덱싱 or 슬라이싱 기법 중 하나를 사용
딕셔너리는 key를 사용하는 방법만 가능
'''
person = {'name':'홍길동', 'phone':'010-1234-5678'}
print(person['name']) #홍길동
print(person['a']) #KeyError(이런 key가 없어서)

person = {'name':'홍길동', 'phone':'010-1234-5678'} #get() 메소드로 항목 접근하기
print(person.get('phone')) #010-1234-5678
print(person.get('a')) #None #key가 없어도 keyerror가 나지 않는다.
print(person.get('a', '1234')) #1234 #key가 없을 때 None이 아닌 default값을 반환하고 싶으면 두번째 인자 사용

#항목 수정하기
'''
update() 메소드 사용
이때, key의 ''은 빼야한다. 
'''
person = {'name':'홍길동', 'phone':'010-1234-5678'}
person.update(name = '최민우')
print(person) #{'name': '최민우', 'phone': '010-1234-5678'}

#빈 딕셔너리 생성
a = {} 
b = dict()
print(a, b) #{} {}

#딕셔너리 주의사항 1 - 중복된 key를 사용하면 하나만 사용되고 나머지는 무시
a = { 1:'one', 1:'two'}
print(a[1]) #two #그리고 웬만하면 key에 int 넣지 않기
print(a) #{1: 'two'}

#딕셔너리 주의사항 2 - key는 변하지 않는 값이어야 한다.
#a = {[1,2]:'one two'} #리스트 자료형은 사용 불가능하지만
a = {(1, 2):'one two'} #튜플 자료형은 사용 가능~
print(a) #{(1, 2): 'one two'}

#key 리스트 만들기 - key() 메소드
a = {1:'one', 2:'two', 3:'three'}
print(a.keys()) #dict_keys([1, 2, 3]) #dict_keys 객체로 반환(이게 리스트로 반환하는 거 보다 메모리 사용을 덜 한대~)

for i in a.keys(): #dict_keys는 이렇게 사용할 수 있음
    print(i) # 1 \n 2 \n 3

a_list = list(a.keys()) #dict_keys 객체를 리스트로 변환하기 - list() 
print(a_list) #[1, 2, 3]


#value 리스트 만들기 - value() 메소드
a = {1:'one', 2:'two', 3:'three'}
print(a.values()) #dict_values(['one', 'two', 'three'])
print(list(a.values())) #['one', 'two', 'three']

#key-value 리스트 만들기 - items() 메소드
a = {1:'one', 2:'two', 3:'three'}
print(a.items()) #dict_items([(1, 'one'), (2, 'two'), (3, 'three')])
print(list(a.items())) #[(1, 'one'), (2, 'two'), (3, 'three')]

for key, value in a.items():
    print(key, value) #1 one \n 2 two \n 3 three
    
#key가 존재하는지 확인 - in 연산자
a = {1:'one', 2:'two', 3:'three'}
print(1 in a) #True
print(4 in a) #False
print(4 not in a) #True

#모든 항목 지우기 - clear() 메소드
a = {1:'one', 2:'two', 3:'three'}
a.clear() 
print(a) #{}

#실습1
score_K = int(input("국어: "))
score_E = int(input("영어: "))
score_M = int(input("수학: "))

print("---------")

score = {"국어":score_K, "영어":score_E, "수학":score_M }
for key, value in score.items() :
    print(key, ':', value)
avg = (score_K + score_E + score_M) / 3
print('평균', ':', avg)

#실습1 - 소스코드
kor = int(input("국어: "))
eng = int(input("영어: "))
math = int(input("수학: "))
print('---------------')

scores = {"국어":kor, "영어":eng, "수학":math }
avg = sum(scores.values()) / len(scores) #dict_values여도 sum함수는 먹는 구나!

for key, value in scores.items():
    print (key, ':', value)
    
print('평균 :', avg)

#실습2
print("사전 프로그램 시작, 종료는 q 입력")

sajeon = {'one':'하나', 'two':'둘', 'three':'셋'}

while True:
    eng = input("입력: ") #습관처럼 int 붙이지 말 것
    if eng == 'q' :
        break
    else: 
        print(sajeon.get(eng, '없음'))
    
print('사전 프로그램 종료')

#실습2 - 소스코드 방법 2(방법 1은 위와 똑같음)
eng_dict = {'one':'하나', 'two':'둘', 'three':'셋'}

print("사전 프로그램 시작, 종료는 q 입력")   

while True: 
    str = input('입력: ')
    if str == 'q':
        break
    else:
        if str in eng_dict: #in 으로 key값 중에 str이 존재하는지 확인
            print(eng_dict[str])
        else:
            print('없음')
     
print('사전 프로그램 종료')       
    
#세트
'''
수학의 집합과 비슷한 자료형
합집합, 교집합, 차집합 등의 집합연산이 가능하다.
세트 = {값1, 값2, ..., 값n}
요소 순서가 없으며, 요소의 중복을 허용하지 않는다. 
'''
a = {1, 2, 3, 4}
print(a) #{1, 2, 3, 4}

a = {1, 'two', 3} #요소 순서는 고려되지 않는다. 
print(a) #{'two', 1, 3} or {1, 3, 'two'} or {1, 'two', 3} (할 때마다 달라짐)

a = {1, 2, 3, 3}
print(a) #{1, 2, 3}

#세트 요소로 변경 가능한 값은 쓸 수 없다.(리스트 불가능, 튜플 가능)
# a = {1, 2, [3, 4, 5]} #TypeError
a = {1, 2, (3, 4, 5)}
print(a)   #{1, 2, (3, 4, 5)}
a = {1, 2, range(5)}
print(a)   #{1, 2, range(0, 5)}

#세트 생성 함수 - set() 함수
a = set([1, 2, 3, 4])
print(a) #{1, 2, 3, 4}

str = set('HELLO')
print(str) #{'E', 'L', 'H', 'O'} #L은 중복이라 한 번만 표현, 순서 고려 X

#빈 세트 생성
a = {}
print(a) #{} #빈 세트처럼 보이지만 빈 세트가 아님!! 빈 딕셔너리(dict)임!!

a = set()
print(a) #set()

#요소에 접근하기
'''
세트는 리스트, 튜플, 딕셔너리와 달리 []로 특정 요소에 직접 접근할 수 없다. 
a = {1, 'two', 3}
a[1] #TypeError: 'set' object is not subscriptable
a['two'] #TypeError: 'set' object is not subscriptable
'''

#요소가 존재하는지 확인 - in 연산자
a = {1, 2, 3}
print(1 in a) #True
print(4 in a) #False
print(4 not in a) #True

a = {1, 2, 3}
if 1 in a:
    print('집합 안에 1이 있음') #집합 안에 1이 있음
    
for i in a:
    print(i, end = ' ') #1 2 3
    
#요소 추가하기 
'''
add()
update()
'''
#add() - 요소 하나 추가
a = {1, 2, 3, 4}
a.add(5)
print(a) #{1, 2, 3, 4, 5}

a.add((123,2))
print(a) #{1, 2, 3, 4, 5, (123, 2)}

#update() - 리스트로 요소 여러 개 추가
a = {1, 2, 3, 4}
a.update([6, 7])
print(a) #{1, 2, 3, 4, 6, 7}

a = {1, 2, 3, 4}
a.update([6, 7])
print(a) #{1, 2, 3, 4, 6, 7}

a.update((89,8))
print(a) #{1, 2, 3, 4, 6, 7, 8, 89}

a.update(((98798, 3987987), 83)) #보라색 괄호가 []여도 똑같은 결과
print(a) #{1, 2, 3, 4, 6, 7, 8, 83, (98798, 3987987), 89}

#요소 삭제하기
'''
remove()
discard()
pop()
'''
#remove(요소) - 요소가 없으면 error
a = {1, 2, 3, 4}
a.remove(4)
print(a) #{1, 2, 3}
#a.remove(4) #요소가 없으면 error

#discard() - 특정 요소를 삭제하고 요소가 없으면 그냥 넘어감
a = {1, 2, 3, 4}
a.discard(4)
print(a) #{1, 2, 3}

a.discard(8)
print(a) #{1, 2, 3}

#pop() - 임의의 요소 반환 후 삭제, 요소 없으면 error, 괄호 안에는 아무것도 넣지 않는다(넣으면 TypeError)
a = {1, 2}
print(a.pop()) #1
print(a.pop()) #2
# print(a.pop())

#기타 함수
'''
a.clear()
len(a)
max(a) / min(a) / sorted(a) / sum(a)
'''
#clear() - 모든 요소 삭제
a = {1, 2, 3}
a.clear()
print(a) #set()

#len(a) - 세트의 요소 개수
a = {1, 2, 3}
len(a) #3

#max(a) / min(a) / sorted(a) / sum(a)
a = {1, 2, 3, 4, 5}
print(max(a)) #5 #요소 중 제일 큰 수 
print(min(a)) #1 #요소 중 제일 작은 수 
print(sorted(a)) #[1, 2, 3, 4, 5] #요소를 정렬하여 리스트를 만든다
print(sum(a)) #15 #요소들의 합

#집합연산
#합집합
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B) #{1, 2, 3, 4, 5}
print(A.union(B)) #{1, 2, 3, 4, 5}

#교집합 
print(A & B) #{3}
print(A.intersection(B)) #{3}

#차집합
print(A - B) #{1, 2}
print(A.difference(B)) #{1, 2}

#대칭차집합 - 합집합에서 교집합을 뺀 집합
print(A ^ B) #{1, 2, 4, 5}
print(A.symmetric_difference(B)) #{1, 2, 4, 5}

#부분집합
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(A < B) #True
print(A.issubset(B)) #True

#상위집합
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(B > A) #True
print(B.issuperset(A)) #True

#같은 집합인지 비교
A = {1, 2, 3}
B = {1, 2, 3}
print(A == B) #True
print(A != B) #False

#실습1
A = {'Kim', 'Lee', 'Park', 'Choi'}
B = {'Choi', 'Jung'}
all_class = A & B
A_only_class = A - B
print(all_class)
print(A_only_class)

#실습1 - 소스코드
A = {'Kim', 'Lee', 'Park', 'Choi'}
B = {'Choi', 'Jung'}

C = A & B
print("A, B 수업을 모두 수강한 사람: ", end = '')
for i in C :
    print(i, end = ' ')

print() #줄 바꿈

D = A - B
print("A수업만 수강한 사람: ", end = ' ')
for i in D: 
    print(i, end = ' ')

#실습2
four = set()
seven = set()
for i in range(1,101):
    if i % 4 == 0 :
        four.add(i)
    if i % 7 == 0 :
        seven.add(i)
print(four & seven) #{56, 84, 28}

#실습2 - 소스코드
four = set()
seven = set()

for i in range(1,101):
    if i % 4 == 0 :
        four.add(i)
    if i % 7 == 0 :
        seven.add(i)

C = four & seven
print("4와 7의 공배수:", sorted(C)) #4와 7의 공배수: [28, 56, 84]