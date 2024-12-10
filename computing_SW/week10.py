#open() - 파일 열기
'''
파일객체 = open('파일 이름', '열기 모드')
r: 읽기 모드(기본값, 생략 가능)
w: 쓰기 모드(새로운 파일 생성 or 기존 파일 내용 덮어쓰기)
a: 추가 모드
x: 배타적 쓰기 모드(새로운 파일 생성, 파일이 존재하면 오류 발생)
'''
#open() 함수의 열기모드: w
f = open ('hello.txt', 'w')
f.write('Hello Python')
f.close()

#여러 줄 작성해보기
f = open ('hello.txt', 'w')
f.write('Hello Python(1)')
f.write('Hello World(2)')
f.close()
#Hello Python(1)Hello World(2)

#개행문자 포함
f = open ('hello.txt', 'w')
f.write('Hello Python(1)\n')
f.write('Hello World(2)\n')
f.close()

#반복문 사용
f = open('hello.txt', 'w')
for i in range(1, 4):
    data1 = 'Hello Python 1: %d \n' % i #이럴 때는 문자열 포맷팅을 사용해야 한다. 
    data2 = f"Hello Python 2: {i} \n" #같은 거임
    # f.write(data1, data2) #TypeError: TextIOWrapper.write() takes exactly one argument (2 given)
    f.write(data1)
    f.write(data2)
f.close()

#open() 함수의 열기모드: r

#파일 객체.read() 메소드
#파일의 내용 전체를 "문자열"로 돌려줌.
f = open('hello.txt', 'r')
data = f.read()
print(data)
print(type(data)) #<class 'str'>
f.close()

#파일객체.readline() 메소드 (* readlines랑 다름!! 조심하기)
#파일의 내용을 "한 줄 씩" 순차적으로 읽음
f = open ('hello.txt', 'r')
data = f.readline() #첫 번째 줄
print(data, end = "") #Hello Python 1: 1  #print함수에 end="" 안 하면 개행문자 + 기본 줄바꿈 때문에 \n\n이 됨.
data = f.readline() #두 번째 줄
print(data, end = "") #Hello Python 2: 1
f.close()

#모든 줄을 읽어서 화면에 출력하려면
f = open('hello.txt', 'r')
data = f.readline() 
while data != "": #readline()은 더 이상 읽을 줄이 없으면 빈 문자열("")을 반환
    print(data, end = "")
    data = f.readline() #다음 줄로~
f.close()
    
#파일 객체.readlines() 메소드
#모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트를 반환
f = open ('hello.txt', 'r')
data = f.readlines()
print(data)
f.close()
#['Hello Python 1: 1 \n', 'Hello Python 2: 1 \n', 'Hello Python 1: 2 \n', 'Hello Python 2: 2 \n', 'Hello Python 1: 3 \n', 'Hello Python 2: 3 \n']

#strip() 메소드: 개행문자(\n) 제거
f = open ('hello.txt', 'r')
data = f.readlines()
for line in data:
    line = line.strip() #줄 끝에 개행문자 제거
    print(line)
f.close()
    
#strip() 탐구하기 
#문자열의 시작과 끝에 있는 문자 or 공백 or 개행문자만 인식
#가운데에 있는 문자를 ()안에 넣어봤자 아무 일도 일어나지 않음
#시험에 내기 좋으신가봐
a = "       Hello       "
a = a.strip()
print(a) #Hello

a = "****Hello****"
a = a.strip()
print(a) #Hello

a = "       Hello       "
a = a.strip('H')
print(a) #       Hello       

a = "Hello       "
a = a.strip('H')
print(a) #ello   

#open 함수의 열기모드: a
'''
쓰기모드(w)로 파일을 열면 이미 존재하던 파일의 내용이 사라짐
원래 값을 유지하면서 새로운 값을 추가하고 싶으면 추가(append) 모드로 파일을 열어야 함.
즉, 기존 파일에 내용 덧붙이기!
'''  
f = open('hello.txt', 'a')
for i in range(4, 7):
    data = "Hello Python : %d \n" % i
    f.write(data)
f.close() 
    
# with as : 자동으로 파일 객체 닫기
# f.close() 안 해줘도 됨.
'''
with open(파일이름, 열기모드) as 파일객체:
    코드
'''
with open('hello.txt', 'r') as f :
    data = f.read()
    print(data) 

#csv 파일 열기
import csv
f = open('file_name.csv', 'r', encoding = 'utf-8') #file.name.csv 있는 걸로 바꾸기
rdr = csv.reader(f) #<_csv.reader object at 0x000001F6220861A0>
header = next(rdr)
for line in rdr:
    print(line)
f.close()

#csv 파일 쓰기
import csv 
f = open('output.csv', 'w', encoding='utf-8') #newline='' 옵션 추가하면 자동 줄바꿈 사라짐. 
wr = csv.writer(f)
wr.writerow([1, "Alice", True]) #근데 이거 \n\n 으로 되네.
wr.writerow([2, "Bob", False])
f.close() 

#csv 파일을 딕셔너리로 읽기
import csv
with open('./file_name.csv') as csvfile:
    rdr = csv.DictReader(csvfile)
    for i in rdr:
        print(i)

#실습 - 타이타닉 - 1)
import csv

Cnt_male = 0
Cnt_male_safe = 0
Cnt_female = 0
Cnt_female_safe = 0

f = open('titanic.csv', 'r', encoding='UTF-8')
rdr = csv.reader(f)
# 0: 생존여부, 1:성별, 6: 클래스

header = next(rdr) 

for line in rdr:
    print(line)
    if line[1] == 'male':
        Cnt_male += 1
        if line[0] == '1':
            Cnt_male_safe += 1
    elif line[1] == 'female':
        Cnt_female += 1
        if line[0] == '1':
            Cnt_female_safe += 1
        
f.close()

print('남성 생존 확률:', Cnt_male_safe/Cnt_male)
print('여성 생존 확률:', Cnt_female_safe/Cnt_female)

print(f"남성 생존률:{(Cnt_male_safe/Cnt_male)*100:.2f}%")
print(f"여성 생존률:{(Cnt_female_safe/Cnt_female)*100:.2f}%")
print(f"총인원수:{Cnt_male + Cnt_female} (남성:{Cnt_male}/여성:{Cnt_female})")

#실습 - 타이타닉 - 2)

Cnt_first = 0
Cnt_first_safe = 0
Cnt_second = 0
Cnt_second_safe = 0
Cnt_third = 0
Cnt_third_safe = 0

f = open('titanic.csv', 'r', encoding='UTF-8')
rdr = csv.reader(f)
header = next(rdr) 
for line in rdr:
    print(line)
    if line[6] == 'First':
        Cnt_first += 1
        if line[0] == '1':
            Cnt_first_safe += 1
    elif line[6] == 'Second':
        Cnt_second += 1
        if line[0] == '1':
            Cnt_second_safe += 1
    elif line[6] == 'Third':
        Cnt_third += 1
        if line[0] == '1':
            Cnt_third_safe += 1
        
f.close()

print('first class 생존 확률:', Cnt_first_safe/Cnt_first)
print('second class 생존 확률:', Cnt_second_safe/Cnt_second)
print('third class 생존 확률:', Cnt_third_safe/Cnt_third)

#교수님

class_name = ['First', 'Second', 'Third']

#교수님 22
names = ['male', 'female', 'First', 'Second', 'Third']
att = [1, 1, 6, 6, 6] #이렇게 하면 두 가지를 통합해서 볼 수 있다. 
n_name = [0, 0, 0, 0, 0]
n_name_survived = [0, 0, 0, 0, 0]


for line in rdr:
    for i in range(len(names)):
        if line[att[i]] == names[i]: ##
            n_name[i] += 1
            if line[0] == '1':
                n_name_survived[i] += 1
                
for i in range(len(names)):
    print()
##

#image 파일 읽기
#PIL, matplotlib 설치 (터미널에 입력)
'''
python -m pip install -U pip
python -m pip install -U matplotlib
'''
#
from PIL import Image #PIL 설치해야함

im = Image.open('apple.jpg')
im.show() 

#
import matplotlib.pyplot as plt

im = plt.imread('apple.jpg')
plt.imshow(im)
plt.show() 

#python open cv - 그냥 이런 게 있다만 알아두기
import cv2
im = cv2.imread('apple.jpg')
cv2.imshow('apple', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
