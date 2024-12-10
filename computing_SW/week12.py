import numpy as np

print(np.arange(10))
print(np.arange(2,10,2))

print(np.linspace(1,2,3)) #1부터 2가지 3개로 쪼개기 #float
print(np.linspace(1,3,3)) #1부터 3까지 3개로 쪼개기

v1 = np.array([1,2,3]) #벡터
v2 = np.array([4,5,6])
v3 = np.array([7,8])

print(v1 + v2) #[5 7 9]
print(v1 * 3) #[3 6 9]
print(v1 / v2) #[0.25 0.4  0.5 ]
#print(v1 + v3) #사이즈가 안 맞으면 오류

m1 = np.array([[1, 2], [3, 4]]) #matrix
m2 = np.array([[5, 6], [7, 8]])

print(m1 + m2)
print(m2 // m1)
print(m1 * m2) #요소끼리 곱함
print(m1 @ m2) #행렬의 곱
print(np.matmul(m1, m2)) #행렬의 곱2
print(m1.T) #transpose

#np.reshape(array_like, newshape)
v4 = np.arange(1, 10)
m3 = np.reshape(v4, (3, 3)) 

s1 = m3[1, 1]
m4 = m3[0 : 1] #matrix 형태로 빼겠다 #첫번째 행 슬라이싱
v5 = m3 [0, : ] # 첫번째 행 전체 #1차원의 배열로 출력 앞과 다른 거임.

print(m3)
print(s1) #5
print(m4) #[[1 2 3]]
print(v5) #[1 2 3]

#Practice
v4 = np.arange(1, 10) # [1 2 3 4 5 6 7 8 9]
m3 = np.reshape(v4, (3, 3)) 
m5 = np.reshape(v4[1:], (2, 4)) #2부터 9까지 2*4로
m6 = np.zeros_like(m3) #shape(3*3)만 가져와서 0으로 채우기
m7 = np.ones_like(m5) #shape(2*4)만 가져와서 1로 채우기
m8 = np.reshape(v4[1:], (4, -1)) #2부터 9까지 #행은 4행, 열은 자동으로 구성

print(v4, m3, m5, m6, m7, m8, sep = '\n')

#np.where()
a = np.arange(10)
out = np.where(a<5, a, a*10) #(조건, 만족할 경우, 만족하지 않을 경우) 
print(out) #[ 0  1  2  3  4 50 60 70 80 90]

a = np.arange(0, 100, 10)
print(a) #[ 0 10 20 30 40 50 60 70 80 90]
out1 = np.where(a%20 == 0) #조건만 적으면 조건에 맞는 index 반환
print(out1) #(array([0, 2, 4, 6, 8], dtype=int64),)
out2 = a[np.where(a%20 == 0)] #이렇게 해야 인덱스에 맞는 값 반환
print(out2) #[ 0 20 40 60 80]

#선형 그래프 그리기
import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)
plt.show() #이걸 해야 결과가 뜬다. 

#바형 그래프 그리기
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 5)
y = x * 10

plt.bar(x, y)
plt.show()

#2차 함수 그래프 그리기

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-7, 7, 0.1)
y = x * x

plt.xlabel('x') #x축 이름
plt.ylabel('y')
plt.plot(x, y)
plt.show()

#파이 차트 그리기
import matplotlib.pyplot as plt

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']

plt.pie(ratio, labels = labels, autopct='%.1f%%') #%를 표기하려면 %%로 써야 표기가 됨 #둘 다 지우면 % 표시 없어짐
plt.show()

#subplots
data = np.arange(100, 201)
plt.subplot(2, 1, 1)
plt.plot(data)

data2 = np.arange(200, 301)
plt.subplot(2, 1, 2)
plt.plot(data2)

plt.show()

#subplots_2
data = np.arange(1, 51)
fig, axes = plt.subplots(2, 3) # 2 * 3
axes[0, 0].plot(data)
axes[0, 1].plot(data*data)
axes[0, 2].plot(data**3)
axes[1, 0].plot(data%10)
axes[1, 1].plot(-data)
axes[1, 2].plot(data//20)

plt.tight_layout()
plt.show()

#Attributes
import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.arange(10), np.arange(10)*2, label = '2x', linestyle = '-', color = 'tab:orange')
plt.plot(np.arange(10), np.arange(10)**2, label = '(x)^2')
plt.plot(np.arange(10), np.log(np.arange(10)), label = 'ln(x)', marker = '*', linestyle = ':', color = 'lime')

plt.title('Here is a title', fontsize = 20)

plt.xlabel ('x-axis', fontsize = 10)
plt.ylabel ('y-axis', fontsize = 10)

plt.legend(loc = 'lower right') #location #여기에 범례를 박아줘.

plt.xlim(0, 5) #x limitation, x축 여기까지만 출력해
plt.ylim(0.5, 10)
plt.show()

#Practice

x = np.linspace(0, 2*np.pi, 200) # 0부터 2π까지의 범위를 200개의 등간격으로 나눈 배열을 생성
fig, axes = plt.subplots(2,2)
fig.suptitle("Sinusoidal Graph", fontsize = 20) #super title #전체, 큰 제목

axes[0,0].plot(x, np.sin(2*x), linestyle = '-', color = 'c')
axes[0,0].set_title("sin(x)") #이 그래프 제목(작은 제목)
axes[0,0].set_xticks([0, 1, 2, 3, 4, 5, 6]) #x축 눈금 지정

axes[0,1].plot(x, np.sin(2*x), linestyle = '--', color = 'b')
axes[0,1].plot(x, np.sin(3*x), linestyle = '--', color = 'g')
axes[0,1].plot(x, np.sin(4*x), linestyle = '--', color = 'r')
axes[0,1].set_title("sin(nx), n=2,3,4")

axes[1,0].plot(x, np.cos(x), linestyle = '-.', color = 'r')
axes[1,0].set_title("cos(x)")

axes[1,1].plot(x, np.cos(2*x), linestyle = ':', color = 'k')
axes[1,1].set_title("cos(2x)")

plt.tight_layout()
plt.show()

#scatterplot
import csv

f = open('./data.csv', 'r')
data = list(csv.reader(f)) ##<_csv.reader object at 0x000001F6220861A0>를 list로 만들어 가공 가능하도록~
data = np.array(data, dtype='float64')
x = data[:, 0] #0열 전체
y = data[:, 1] #1열 전체
plt.scatter(x, y)

x_1 = 2
y_1 = 2
plt.scatter(x_1, y_1, c = 'g', s=100, marker = '*') #marker 넣기

plt.show()
f.close()
