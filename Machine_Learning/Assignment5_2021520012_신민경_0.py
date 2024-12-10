import csv
import matplotlib.pyplot as plt
import numpy as np

x = [] # TV, Radio, Newspaper
y_Sales = []

#파일
f = open('./advertising.csv', 'r', encoding = 'utf-8')
rdr = csv.reader(f)
header = next(rdr)
for line in rdr:
    #print(line)
    x.append([float(line[0]), float(line[1]), float(line[2])])
    y_Sales.append(float(line[3])) 
    
f.close()

#
x = np.array(x)
y_Sales = np.array(y_Sales)

#
w = np.zeros ((3, 1))
b = 0

#
lr = 0.0000006
iteration = 100

#J(w) #미분 안 한 거
def loss_function(x, y_Sales, w, b):
    y_hat = x @ w + b 
    return np.mean((y_hat - y_Sales)**2) / 2 

#update  # 여기서부터 작업하기
losses = []
x_transpose = np.transpose(x)

for i in range(iteration):
    
    y_hat = x @ w + b
    
    dw = np.mean(x_transpose @ (y_hat - y_Sales)) 
    db = np.mean(y_hat - y_Sales) 
    
    w = w - lr * dw
    b = b - lr * db
    
    loss = loss_function(x, y_Sales, w, b)
    losses.append(loss)

# 학습된 모델 w, b 출력
print('w', w)
print('b', b)

#Loss 변화 plot - 수렴, 발산 확인
plt.plot(losses)
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.title('Training Loss')

plt.tight_layout()
plt.show()