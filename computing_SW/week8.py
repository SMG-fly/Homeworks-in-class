#크로아티아 알파벳
croatia_ab = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
target = input("Write word:")

#ljes=njak
count = 0 #글자수 세기
pivot = 0 #검사 글자 위치
while True:
    if pivot >= len(target):
        break
    
    is_croatia = False 
    for cab in croatia_ab:
        l_cab = len(cab)
        if target[pivot:pivot+l_cab] == cab: #pivot위치 문자가 크로아티아인지 검사 #3개짜리 크로아티아도 고려
            count += 1
            pivot += l_cab
            is_croatia = True
            break
    if not is_croatia:    
        count += 1
        pivot += 1
    
print('length of word is :{}'.format(count))
print(f'length of word is :{count}') #이렇게 써도 됨 #python 3.6부터가능

#함수
'''
def 함수이름 (매개변수1, 매개변수2, ..., 매개변수n):
    실행할 명령문
    ...
    return 반환값
'''

def show(age): #age: 매개변수
    print('저는', age, '살입니다.')
print('안녕하세요.')
show(23) #23: 인자
#안녕하세요.
#저는 23 살입니다.

def show(age, height):
    print('저는', age, '살입니다.')
    print('키는', height, 'cm 입니다.')
show (23, 181.5)
#저는 23 살입니다.
#키는 181.5 cm 입니다.

#실습
def sachik(a,b):
    print('%d+%d=%d'%(a,b,a+b))
    print('%d-%d=%d'%(a,b,a-b))
    print('%d*%d=%d'%(a,b,a*b))
    print('%d/%d=%f'%(a,b,a/b)) #나누기 결과는 실수

num1 = int(input('정수1:'))
num2 = int(input('정수2:'))
sachik(num1, num2)

#실습2 - 방법1
def star(a):
    print('*'*a) 
num = int(input())
star(num)

#실습2 - 방법2
def show_star(x):
    for i in range(x):
        print('*', end = ' ')
n = int(input("입력: "))
show_star(n)

#실습3
def gugu(a):
    for i in range(1,10):
        print("{}*{}={}".format(a,i,a*i))
dan = int(input("단: "))
gugu(dan)
        
#실습4 - 방법 1
def square(a):
    for i in range(a):
        print("*"*a)     
num = int(input("입력: "))
square(num)

#실습4 - 방법2
def draw_rect(side):
    for i in range(side):
        for j in range(side): 
            print('*', end='')
        print()
n = int(input("입력: "))
draw_rect(n)

#함수의 결과 반환
def add(n1, n2):
    return n1 + n2
ans = add(5, 3)
print(ans) 
#앞에서는 함수에 print가 내장되어 있었지만 이번 함수는 반환값으로 돌려주기만 하는 것임!
#ans = add(5,3) = 8(return)

def calculate_area(radius):
    area = 3.14 * radius**2
    return area
ans = calculate_area(3)
print(ans)

#실습 1
def square(n):
    return n**2
ans = square(5)
print(ans) #25

#실습2 - 방법 1
def get_max(x,y):
    return max(x,y)
print(get_max(9,5)) #9

#실습2 - 방법 2
def get_max(x, y):
    if x > y :
        result = x
    else:
        result = y
    return result
ans = get_max(5, 3)
print(ans) #5

#실습3
def get_sum(start, end):
    s = 0
    for i in range(start, end+1):
        s += i
    return s
print(get_sum(1, 10)) #55

#실습4: 팩토리얼 - 방법1
def factorial(n):
    dap = 1
    for i in range(n, 0, -1):
        dap *= i
    return dap
print(factorial(4)) #24

#실습4 - 방법2
def factorial(n): 
    dap = 1
    for i in range (1, n+1):
        dap *= i
    return dap 
print(factorial(4)) #24

#실습5
def hap(x, y):
    print("두 수의 합:", x + y)
def diff(x, y):
    print("두 수의 차:", x - y)
n1 = int(input("정수 n1:"))
n2 = int(input("정수 n2:"))
hap(n1, n2)
diff(n1, n2)

#실습 5 - 소스코드
def sum(x, y):
    return x+y
def diff(x, y):
    if x > y :
        return x - y
    else :
        return y - x
n1 = int(input("정수 n1: "))
n2 = int(input("정수 n2: "))
print ('두 수의 합:', sum(n1, n2))
print ('두 수의 차: ', diff(n1, n2))

#매개변수는 없지만 반환값만 있는 함수도 가능하다!
def one():
    return 1
ans = one()
print(ans) #1

#반환값 없이 return만 쓸 경우 함수 중간에서 바로 종료
def check_not_ten(n):
    if n == 10:
        return #n=10이면 여기서 함수 종료
    print(n, '입니다.')
check_not_ten(5) #5 입니다.
check_not_ten(10) #아무것도 출력 안 함.

#여러 개 값 반환하기
def add_sub(x, y):
    return (x+y, x-y) #튜플 -> 괄호 없어도 됨. 
a, b = add_sub(5, 3) #언패킹
print(a) #8
print(b) #2

#실습1
def big_small(a, b):
    if a > b :
        big = a
        small = b
    else :
        big = b
        small = a
    print('큰 수:', big)
    print('작은 수:', small)
n1 = int(input('정수1: '))
n2 = int(input('정수2: '))
big_small(n1, n2)

#실습1 - 소스코드(교재 의도)
def big_small(x, y): 
    if x > y: 
        return x, y
    else :
        return y, x #큰 게 앞에 오도록
n1 = int(input('정수n1: '))
n2 = int(input('정수n2: '))
big, small = big_small(n1, n2)
print('큰 수:', big)
print('작은 수:', small)    

#실습2
def circle(r):
    nul = 3.14*(r**2)
    dul = 2*3.14*r
    return nul, dul
ri = float(input("원의 반지름: "))
nulbi, dulle = circle(ri)
print('원의 넓이:', nulbi)
print('원의 둘레:', dulle)

#매개변수에 기본값(default) 설정하기
#default값은 반드시 매개 변수 마지막 부분에 사용해주어야 한다. 
def student(name, phone, stu_no='비공개'):
    print('이름:', name)
    print('전화번호:', phone)
    print('학번:', stu_no)
student('홍길동', '010-1234-5678')
student('홍길동', '010-1234-5678', '220104')

#가변 매개변수
#매개변수가 몇 개인지 모를 때, 마음대로 넣을 수 있도록
'''
def 함수이름(*매개변수):
    코드
'''
def print_num(*args):
    for i in args:
        print(i)
print_num(10) #10
print_num(10, 20, 30) # 10 \n 20 \n 30

#가변 매개변수를 일반 매개변수와 함께 사용할 경우
#가변 매개변수를 마지막에
def print_num(m, *args):
    for i in args:
        print(m*i)
print_num(2, 10) #20
print_num(2, 10, 20, 30) #20 \n 40 \n 60

#전역변수와 지역변수
#지역변수가 전역변수를 변화시킬 수는 없지만, 우선순위는 지역순위가 높다.
def a():
    x = 100
    print('x=', x)
x = 10
a() #x= 100
print(x) #10

#global()
#함수 내부에서 전역변수를 사용하고 싶을 때 사용
def a():
    global x
    x = 100
    print('x =', x)
x = 10
a() #global x 실행 
print(x) #100