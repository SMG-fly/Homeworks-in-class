print(100)
print(30+70)

print("가나다라")
print("Hello World")

print("Hello World")
print('Hello World')
print('가나다')

print(1, 2, 3)
print('Hello', 'Python')

print(1, 2, 3, sep=', ')
print(4, 5, 6, sep=',')
print('Hello', 'Python', sep='')
print("010", "1234", "5678", sep="-")

print('Hello')
print('World')
print('Good')
print('Job')

print('Hello', end='') #end의 기본값은 \n
print('World', end='')
print('Good', end='')
print('Job')

print('Hello'); print('1234') #한 줄에 여러 구문 사용 시 ; 사용

print(15+37)
print("15에서 37을 뺀 값은", 15-37, "입니다")
print('동\n서\n남\n북')
print('동', '서', '남', '북', sep='\n')
print('여보세요\n안녕하세요\n\n그럼 이만.')

no=75 #변수 지정
print('no의 값은', no, '입니다')
no='75' 
print('no의 값은', no, '입니다')

print(2023, 10, 31, sep='/', end=' ') 
print(11, 29, 52, sep=":")

year=2023
month=10
day=31
time="11:29:42"
print(year, month, day, sep='/', end=' ')
print(time) 

#input 함수
year=input("년도를 입력해 주세요")

name = input("이름이 무엇인가요? ")
print("만나서 반갑습니다. " + name + "씨!")
age = input("몇 살인가요? ")
print("네, 그러면 당신은 " + age + "살이시군요, " + name + "씨!")

x = input("첫 번째 정수: ") #숫자를 문자로 인식해버렸네요~
y = input("두 번째 정수: ")
sum = x + y
print("합은 ", sum)

#그러니 int()를 사용해 숫자로 인식해봅시다.
x = int(input("첫 번째 정수: ")) 
y = int(input("두 번째 정수: "))
sum = x + y
print("합은 ", sum)

no = int(input("no의 값을 입력해주세요 :")) #int는 선택사항
print("no의 값은", no, "입니다")

num = int(input("정수를 입력해주세요 : ")) #int 필수
print("이 값에서 10을 빼면", num-10, "입니다")

print("두 개의 정수를 입력해주세요.")
a = int(input("정수1: "))
b = int(input("정수2: "))
print("이들의 곱은", a*b, "입니다.")

print("세 개의 정수를 입력해주세요.")
a = int(input("정수1: "))
b = int(input("정수2: "))
c = int(input("정수3: "))
print("이들의 곱은", a*b*c, "입니다.")

#주석 달기(이미 달고 있지만)
#사각형의 가로 길이
width = 10
#사각형의 세로 길이
height = 20
#사각형의 면적 계산
area=width*height
#print(area)

#주석은 테스트용으로 사용해볼 수 있다.
x=int(input('첫 번째 정수: '))
y=int(input('두 번째 정수: '))
sum = x + y
#diff = x - y
print("합은 ", sum)
#print("차는 ", diff)

#블록 주석 - ''' 또는 """ 
#특정구역 전체 주석처리, 줄 바꿈도 문제 없다.
'''블록 주석 시작 
d = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
print(d) 
블록 주석 끝'''

#if의 다음 줄은 들여쓰기, 4칸 공백 권장

# 여러 줄로 나누어 코드 작성
# 괄호로 묶기
s = ('Hello'
     +'World')
print(s)
#줄의 마지막에 \ 사용
s = 'Hello' \
+ 'World'
print(s)
