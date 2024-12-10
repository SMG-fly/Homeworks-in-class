import csv
import matplotlib.pyplot as plt
import numpy as np

x = [] 
y = []
mapping = {'Versicolor': 0,
           'Virginica': 1,
           'Setosa': 2}

# 파일
with open('./iris.csv', 'r', encoding = 'utf-8') as f:
    rdr = csv.reader(f)
    header = next(rdr)
    for line in rdr:
        #print(line)
        x.append([float(line[1]), float(line[2])])
        y.append(float(mapping[line[4]])) 

#
x = np.array(x[50: ])
x = np.insert(x, 0, 1, axis=1) # x의 0번 열에 1추가(bias) #w0 * 1
y = np.array(y[50: ])

# 
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# J(w) #미분 안 한 거
def loss_function(x, y, w): 
    fx = sigmoid(x @ w)
    Jw = np.mean(-y * np.log(fx) - (1 - y) * np.log(1 - fx)) ##
    return Jw

#
w = np.zeros(x.shape[1])

#
lr = 0.1
iteration = 10000

# Gradient Descent
loss_history = []

for i in range(iteration):
    fx = sigmoid(x @ w)

    #dw0 = np.mean(x[:, 0] * (fx - y)) #다 따로따로 해줘야 함. #axis=1 사용해서 따로 해줄 수도 있음(벡터 계산)
    #dw1 = np.mean(x[:, 1] * (fx - y))
    #dw2 = np.mean(x[:, 2] * (fx - y))
    dw = np.mean(x * (fx - y)[:, np.newaxis], axis=0) 
    #fx-y (100,)에서 (100,1)로 바꿔서 broadcasting 용이하도록~
    
    #w[0] = w[0] - lr * dw0
    #w[1] = w[1] - lr * dw1
    #w[2] = w[2] - lr * dw2
    w = w - lr * dw
    
    loss_history.append(loss_function(x, y, w))

#plt.figure(figsize=(10, 4))

# Scatter plot (versicolor and virginica)
#plt.subplot(1, 2, 1)
plt.scatter(x[y == 0][:, 1], x[y == 0][:, 2], label='versicolor', color='blue') #x_sepal, x_petal
plt.scatter(x[y == 1][:, 1], x[y == 1][:, 2], label='virginica', color='red') 

# Decision boundary (y=0.5)
x1_db = np.array([min(x[:, 1]), max(x[:, 1])])
x2_db = -(w[0] + w[1] * x1_db) / w[2] ## # 'w[0] + w[1]*x1 + w[2]*x2 = 0' 을 정리한 것
plt.plot(x1_db, x2_db, label='Decision Boundary', color='green')

plt.xlabel('Sepal Width')
plt.ylabel('Petal Length')
plt.title('Iris Decision Boundary')
plt.legend()
plt.grid(True)

#Loss
'''
plt.subplot(1, 2, 2)
plt.plot(loss_history)
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.title('Training Loss')
'''

plt.show()

print(w)