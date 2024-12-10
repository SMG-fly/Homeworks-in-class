weight = 75.3
print(weight)

x= 100
y= 200 
print(x,y) #터미널에서 하는 거랑 다르네
#변수의 개념

x, y = 10, 20
x, y = y, x #자리 바꾸기
print(x)
print(y)

x = 10
del x #선언한 변수 삭제하기
#print(x)

x = None #빈 변수 만들기
print(x)

#변수명 규칙
''' 
1. 숫자로 시작X
2. 공백 포함X
3. 공백 대신 _로 연결
4. 대문자와 소문자 구분
5. 파이썬의 예약어와 함수 이름 사용X (***) (터미널에서 import keyword \n keyword.kwlist 로 확인)
6. 의미있는 단어 권장
7. 특수문자(_제외) 사용X
 '''

#자료형

#type함수: 변수의 자료형 알아내기 (터미널에서 해야 함)
x = 10 
y = 'Hello world'
type(x)
type(y)

a = 0xFA #0x 또는 0X로 16진수임을 알려줘야함
print(a)

100_000_000 #파이썬에서는 콤마(,) 대신 _로 큰 자리 숫자를 표시한다. 
#05 #0을 다른 숫자 앞에 넣으면 오류 발생

#컴퓨터식 지수 표현 방식
b = 3.23E8 #대문자, 소문자는 중요하지 않은 것으로 추정 #3.23*(10^8) 
c = 23e-10
print(b)
print(c)

#부울평(bool)
a = (100 < 100)
print(a)
a = (100 <= 100)
print(a)
b = (300 == 300)
print(b)

#None
a = None
print(a)
type(a) #터미널에서 확인

#실습
r = int(input("반지름을 입력하세요: "))
circle = 3.141592 * (r**2)
print('원의 면적은', circle)

weight = float(input("체중을 입력하세요: ")) #체중과 몸무게 값은 실수이므로 float 함수로
height = float(input("키를 입력하세요(m로): ")) #cm가 아니라 m로 넣어야 함
BMI = weight / (height**2)
print('BMI는', BMI)

b1 = True
b2 = False
print(b1)
print(b2)
print(3<4)
print(3>4)

#문자열 자료형과 형변환

s = '그가 \'좋아\'라고 답했다' #문자열에 \(백슬러시) 사용시 바로 뒷 문자 문자열 예외 처리
print(s)

#이스케이프 문자
print('Hello\nworld')
print('Hello\tworld')
print('Hello\\world')
print('Hello\\nworld')

#문자열 포맷팅 : 문자열 안의 특정 위치에 원하는 값을 사용하고자 할 때
name = '홍길동'
print('제 이름은 %s 입니다.'% name)
age = 22
print('나이는 %d살 입니다.' % age)
height = 176.5
print('키는 %fcm 입니다.' % height)
print('키는 %.1fcm 입니다.' % height) # %f 자리수 정하기

msg = '현재 시간은 %s입니다.'
time = '12:00pm'
print(msg % time)

print("전공은 %s이고 현재 %d학년입니다." % ('환원', 3))

msg = "오늘은 %s월 %s일입니다."
print(msg % (5, 15))

star = "*"
print(star * 50) #star 50번 반복

s1 = '인공'
s2 = '지능'
s3 = (s1 + s2 + '!!') * 3
print(s3)

#인덱스([])
s = 'hello'
print(s[0]) #인덱스 번호는 0부터 시작
print(s[4])
print(s[-1]) #음수일 때는 가장 오른쪽이 -1

#s[0] = 'K' #한 번 작성된 문자열은 변경이 불가함. 인덱스로 문자 변경 불가
print(s)

s='Hello'
print(s[0]+s[1]+s[2]+s[3]+s[4])
print(s[-5]+s[-4]+s[-3]+s[-2]+s[-1])
print(s[3]+s[1]+s[2])

#슬라이싱 
'''
끝 번호는 포함하지 않고 그 전까지 추출함
ex) a[0:2] -> 인덱스 0,1까지 추출됨.
'''
s = 'Hello world'
print(s[0:2])
print(s[0:5])
print(s[5:8])
print(s[6:11])

#print(s[200]) #에러
print(s[0:200]) #에러나지 않음

print(s[:5])
print(s[6:])
print(s[:])

#실습
s = '20210514Friday'
print(s[0:4]+'년', s[4:6]+'월', s[6:8]+'일', s[8:])

s = '20210514Friday'
year = s[:4]
month = s[4:6]
day = s[6:8]
week = s[8:]
print('%s년 %s월 %s일 %s' % (year, month, day, week) )

s = 'Wokld' #오타 고치기(슬라이싱 이용)
s2 = s[:2] + 'r' + s[3:]
print(s2)

#문자열 함수
'''
문자열 처리는 상당히 중요하고 자주 있는 일
내장함수 사용 방법 : 변수이름.함수명
'''

s = 'Hello World' #count(): 문자열에서 특정 문자의 개수를 카운트 
sl = s.count('l')
sw = s.count('w')
print (sl, sw)

s = 'Hello world' #find(): 특정 문자의 위치 값(인덱스)를 반환, 대소문자 구분
sH = s.find('H') #인덱스 시작은 0
so = s.find('o') #여러 개 있으면 첫번째 위치만 반환
sp = s.find('p') #없으면 -1 반환
print(sH, so, sp)

s = 'Hello World' #index() : 특정 문자의 위치 값 반환, find와 달리 찾는 문자가 없으면 오류 발생
sH = s.index('H') 
sWo = s.index('Wo') 
#sp = s.index('p')
print(sH, sWo)

s = '   Hello   '
s1 = s.strip() #strip() : 문자열 왼쪽, 오른쪽에 포함된 모든 공백 제거
s2 = s.lstrip() #lstrip() : 문자열의 왼쪽에 포함된 공백 제거
s3 = s.rstrip() #rstrip() : 문자열의 오른쪽에 포함된 공백 제거
print(s1, s2, s3, sep = '\n')

s = 'Hello World'
su = s.upper() #upper() : 문자열의 알파벳을 모두 대문자로 변환
sl = s.lower() #lower() : 문자열의 알파벳을 모두 소문자로 변환
print(su, sl)

s = 'Hello' #join() : 구분자를 사용하여 문자열의 각각 문자 사이에 삽입
s_ = '/'.join(s)

s = 'Hello'
k='/'
sk = k.join(s)
print(s_, sk)

sep = '-'
sep_ = sep.join('ABCDE')
print(sep_)

s = 'Hello World' #replace(인수1, 인수2) : 문자열에서 인수1 문자열을 인수2 문자열로 치환하는 함수
sr = s.replace('o', 'a') 
sp = s.replace('World', 'Python') #특정 단어를 교환하는 용도로도 기능함.
print(sr, sp)

s = 'Hello world' #split(공백 또는 구분자) : 문자열을 공백 또는 구분자로 나누는 함수 **
ssp = s.split() #공백으로 나누기
w = 'www.nrf.re.kr'
wsp = w.split('.') #구분자('.')로 나누기
print(ssp, wsp)

s = 'Hello {}' #format(): {} 포멧 코드를 사용하여 포멧팅 문자열 내용을 나중에 바꿔줄 수 있음
sw = s.format('World')
sp = s.format('Python')
print(sw, sp)

s1 = 'Hello {0} {1}' #{인덱스} 포멧 사용하면 순서도 변경 가능
s1wp = s1.format('World', 'Python')
s2 = 'Hello {1} {0}'
s2wp = s2.format('World', 'Python') #format({0}, {1}, {2}, ...) 이런 느낌으로 대입되는 거임 -> Hello Python World
s3 = 'Hello {} {}'
s3wp = s3.format('World', 'Python')
print(s1wp, s2wp, s3wp)

s = 'Hello {s1} {s2}' #{이름} 포멧 사용하면 {} 내에 이름 지정 가능
sf = s.format(s2 = 'World', s1 = 'Python')
print(sf)

s = 'hello' #len() : 문자열의 길이를 반환
sl = len(s)
print(sl)

col = [1,2,3] #시퀀스 자료형을 넣으면 자료의 개수를 반환 (*col.len()이 아님 -> 문자열에 국한 X)
coll = len(col)
print(coll)

#자료형 변환

#int() : 실수, 문자열, 계산식을 강제로 정수로 변환해주는 함수
#float() : 정수, 문자열, 계산식을 강제로 실수로 변환해주는 함수
#str(): 정수나 실수를 강제로 문자열로 변환해주는 함수 / 정수나 실수를 문자열과 연산하면 오류 발생하므로 사용
'''ex) score = 100; print(str(score)+'점입니다.')'''
