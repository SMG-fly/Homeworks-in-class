import csv
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)

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
        x.append([float(line[0]), float(line[1]), float(line[2]), float(line[3])])
        y.append(float(mapping[line[4]])) 

#
x = np.array(x[50: ])
y = np.array(y[50: ])

# 
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# J(w) #미분 안 한 거
def loss_function(y_pred, y): 
    
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon) #로그의 무한대 발산을 막아 계산 안정성 유지
    Jw = np.mean(-y * np.log(y_pred) - (1 - y) * np.log(1 - y_pred)) ##
    
    return Jw

class NeuralNet:
    def __init__(self, config_layer):
        self.cf = config_layer
        self.W1 = np.random.rand(self.cf[1], self.cf[0]) # (3 * 4) matrix로 랜덤 난수 생성
        self.b1 = np.random.rand(self.cf[1], 1) # (3 * 1) matrix로 랜덤 난수 생성
        self.W2 = np.random.rand(self.cf[2], self.cf[1])
        self.b2 = np.random.rand(self.cf[2], 1)
        self.W3 = np.random.rand(self.cf[3], self.cf[2])
        self.b3 = np.random.rand(self.cf[3], 1)        

    def forward(self, x, y):
           
        # hidden1    
        self.z1 = self.W1 @ x + self.b1
        self.a1 = sigmoid(self.z1)
        
        # hidden2
        self.z2 = self.W2 @ self.a1 + self.b2
        self.a2 = sigmoid(self.z2)
        
        # Output
        self.z3 = self.W3 @ self.a2 + self.b3
        self.a3 = sigmoid(self.z3)
        
        #self.J_w = loss_function(self.a3, y)
        


    def update(self, x, y, lr):
        
        #Backpropagation
        d3 = (self.a3 - y) 
        d2 = (self.W3.T @ d3) * self.a2 * (1-self.a2)
        d1 = (self.W2.T @ d2) * self.a1 * (1-self.a1)
        #print(d1.shape, d2.shape, d3.shape) #(3, 100), (2, 100), (1, 100)
        
        #Gradient Descent
        self.W3 -= lr * d3 @ self.a2.T #사례 별로 다 더해줘야 하는 거 아냐? # i
        self.b3 -= lr * np.mean(d3, axis=1, keepdims=True) # 결과로 얻는 차원이 원본과 동일
        self.W2 -= lr * d2 @ self.a1.T
        self.b2 -= lr * np.mean(d2, axis=1, keepdims=True)
        self.W1 -= lr * d1 @ x.T
        self.b1 -= lr * np.mean(d1, axis=1, keepdims=True)

def plot():        

    # Plotting hidden2 activations
    a2_0 = model.a2[0, :]
    a2_1 = model.a2[1, :]
    # print(a2_0.shape, a2_1.shape) # (100,) (100,)
    plt.scatter(a2_0[y == 0], a2_1[y == 0], label='Versicolor', color='red', s=10) #요거 해결하기
    plt.scatter(a2_0[y == 1], a2_1[y == 1], label='Virginica', color='blue', s=10) 
    plt.xlabel('a1')
    plt.ylabel('a2')
    plt.title('Hidden2 Activations')
    plt.legend()

    # Plotting decision boundary
    #plt.xlim(min(a2_0)-0.0001, max(a2_1)+0.0001)
    #plt.ylim(min(a2_1)-0.0001, max(a2_1)+0.0001)
    a1_db = np.linspace(min(model.a2[0, :]), max(model.a2[0, :]), 100)
    a1_db = a1_db.reshape(-1, 1)
    a2_db = -(model.b3 + model.W3[0, 0] * a1_db) / model.W3[0, 1] 
    plt.plot(a1_db, a2_db, label='Decision Boundary', color='green')

    plt.show()



config_layer = [4, 3, 2, 1] # input, h1, h2, output
model = NeuralNet(config_layer) ## ?

#
lr = 0.01
iteration = 100000
loss_history = [] 

for i in range(iteration):
    model.forward(x.T, y) # x.T 는 (4 * 100), 100이 i
    model.update(x.T, y, lr)
    loss = loss_function(model.a3, y)
    loss_history.append(loss)
    
    if (i+1) % 20000 == 0:
        plot()
    
# Loss curve
'''
plt.plot(loss_history)
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.show()
'''

# shape
#print(model.a2.shape) #(2,100)
#print(model.W3.shape) #(1, 2)
#print(x.shape) #(100, 4)
#print(model.b3.shape) #(1, 1)

#print(model.a2)
#print(model.W3)
