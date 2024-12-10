# dir() #모듈 안의 함수들과 변수들 리스트 출력
import math
print(dir(math))

#factorial
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print('5! =', factorial(5))

#factorial -> math 모듈 사용
import math
print('5 != ', math.factorial(5))

#모듈 안에서 특정 함수만 불러오기
#import된 함수 호출 시 "함수이름" 만 사용한다.
from math import factorial
print('5 != ', factorial(5)) 
#math.factorial(5) 사용 시 오류
#factorial만 가져왔지 math를 import한 적은 없기 때문

#모듈에 동시에 여러 함수 불러오기
from math import pow, sqrt
a = pow(2, 3) #제곱수
b = sqrt(4) #제곱근
print(a) #8.0
print(b) #2.0

#모듈 안의 모든 함수, 변수 클래스 가져오기
#from 모듈이름 import *
from math import *
print(pi) #변수
print(factorial(5)) #함수

#모듈/함수 이름에 별명 붙이기
'''
모듈 이름에 별칭 사용
import 모듈이름 as 별칭
모듈 안의 함수 이름에 별칭 사용
from 모듈이름 import 함수이름 as 별칭
'''
import math as m
a = m.pow(2,3)
b = m.sqrt(4)
print(a)
print(b)
print(m.factorial(5))

from math import pow as p, sqrt as s #코드 읽기 어려우므로 추천하지는 않음
a = p(2,3)
b = s(4)
print(a) #8.0
print(b) #2.0

#del : import로 가져온 모듈 지우고 싶을 때 
import math
a = math.pow(2,3)
print(a)

del math
a = math.pow(2, 3) #지웠기 때문에 error

#모듈 만들기
'''
main.py : 실행하는 스크립트
my_mod : 모듈로 사용할 스크립트
'''
#main.py
import my_mod
a = my_mod.add(5, 3)
b = my_mod.sub(5, 3)
print(a)
print(b)
print(my_mod.PI)

#표준 모듈 - random 모듈
import random

#randint(start, stop) : start~stop 사이 랜덤정수 반환(start, stop 포함)
print( random.randint(1, 6)) #6

#random() : 0 ~ 1.0 사이의 랜덤 실수를 반환
print(random.random()) #0.8377902389252208

#choice(list) : 리스트 항목을 랜덤하게 반환
color = ['red', 'green', 'blue']
print( random.choice(color) ) #blue

#shuffle(list) : 리스트 항목을 랜덤하게 섞음
color = ['red', 'green', 'blue']
random.shuffle(color)
print(color) #['green', 'red', 'blue']

#sample(population, k)
color = ['red', 'green', 'blue']
ans = random.sample(color, 2)
print(ans)


#표준 모듈 - os 모듈
#listdir() : 현재 경로의 파일과 디렉토리 리스트 반환
import os
print( os.listdir () )

#mkdir('디렉토리_이름') : 새로운 디렉토리 생성
import os
os.mkdir("TEST")
print(os.listdir()) #TEST 라는 폴더까지 나온 것 확인

#getcwd(): 현재 경로를 return
#chdir("../") : 현재 경로를 상위 경로로 변경(다른 경로도 가능)
import os
print(os.getcwd())
os.chdir("../")
print(os.getcwd())

#절대경로 vs 상대경로
'''
절대경로: 최상위 디스크부터 시작
C:\Users\kim\ab\apple.jpg
상대경로: 현재 작업 디렉토리부터 시작
./apple.jpg (현재 폴더에 apple.jpg 파일이 있을 때)
../cd/titanic.csv (상위폴더에서 거슬러 가야하는 경우)
'''
#다만 절대경로를 코드에 그대로 적을 경우 \(역슬래시)를 이스케이프로 인식
# -> / 또는 \\ 또는 r"경로" 형식으로 적어주어야 한다.
os.chdir("C:/Users/신민경/OneDrive - UOS/바탕 화면")
print(os.getcwd())
os.chdir("C:\\Users\\신민경\\OneDrive - UOS\\바탕 화면")
print(os.getcwd())
os.chdir(r"C:\Users\신민경\OneDrive - UOS\바탕 화면")
print(os.getcwd())

#하위폴더 들어가기
os.chdir("./TEST")
print(os.getcwd())

#time 모듈
#time(): 기준 시간 이후 경과한 시간을 초 단위 반환
import time
t = time.time()
print(t)

#localtime(경과한 초): 현재 지역의 시간대 출력
import time
t = time.time()
time_local = time.localtime(t)
print(time_local)

#strftime(시간 객체)
import time
t = time.time()
time_local = time.localtime(t)

print(time.strftime('%Y-%m-%d', time_local)) #2023-06-15
print(time.strftime('%c', time_local)) #Thu Jun 15 00:32:36 2023

#sleep(초): 해당 초 만큼 시간을 지연하는 함수
import time 
time.sleep(3) #3초 기다려(센서의 반응 등 기다릴 때)
print('3초 지남')

#응용 - 알고리즘 동작에 시간이 얼마나 걸리는지 측정
import time
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end = ' ')
        a, b = b, a+b
    print() #그냥 한 줄 띄워주기

start = time.time()
fib(10000)
end = time.time()
print(end-start)

#datetime 모듈
#datetime.today() : 현재의 날짜와 시간 반환
import datetime
print(datetime.datetime.today()) #2023-06-09 19:27:38.739140

#특정 날짜와 시간으로 객체를 만들 수 있다. 
#datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0)
import datetime
d = datetime.datetime(2022, 1, 6)
print(d) #2022-01-06 00:00:00

#datetime 모듈 응용 - 제대 날짜(2023.9.30) 알아보기
import datetime
today = datetime.datetime.today()
end_day = datetime.datetime(2023, 9, 30)
d_day = end_day - today
print(d_day)

#calendar - 달력 모듈, 달력 기능을 제공    
#month(연도, 월): 해당 월의 달력을 문자열로 반환
import calendar
cal = calendar.month(2051, 5)
print(cal)

#3rd Party 모듈

#numpy
#numpy 설치 
# pip install numpy #터미널에 입력

import numpy as np
a = np.array([1, 2, 3])
b = np.array ([[1, 2, 3], [4, 5, 6]]) #[[],[]] 이런식으로 대괄호로 한 번 더 씌워줘야 함.
print(np.shape(b)) #(2, 3) #크기 확인
print(np.size(b)) #6 #element 수

print(b.shape) #(2, 3)
print(b.size) #6
print(b.dtype) #int32 #data_type

#3차원 배열은 Tensor (0차원-스칼라, 1차원-벡터, 2차원-matrix)
c = np.array([[[1, 2, 4], [4, 5, 6]],
              [[7, 8, 9], [10, 11, 12]]])

print(np.shape(c)) #(2, 2, 3)

#zeros(), ones()
a = np.zeros(shape=(3,5))
print(a)
b = np.ones(shape=(2,3))
print(b)

#full(shape, 채울 값)
a = np.full(shape = (3,3), fill_value=5)
print(a)

#eye(N) : 대각 방향 1로 채워진 N*N 행렬 생성
a = np.eye(N=3)
print(a)

#pad(array, pad_width, mode='constant', constant_values=0)
A = np.array ([[1, 2, 3], [4, 5, 6]])
a = np.pad(A, ((1,2), (0,1)), 'constant', constant_values=2) #((위 행, 아래 행), (왼쪽 열, 오른쪽 열)) // 2(constant_values)로 채워라.
print(a)


