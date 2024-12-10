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
x = np.array(x) # (150, 4)
y = np.eye(len(mapping))[np.array(y).astype(int)] # One-hot encoding

# Activation function
def relu(z):
    return np.maximum(0, z)

# Derivative of relu # g'(z), a = g(z) # a를 z로 미분
def d_relu(a):
    return np.where(a < 0, 0, 1) # 조건을 충족하면 0, 아니면 1로 바꿔줌

# softmax 
def softmax(z): # z가 리스트 형태로 들어올거야.
    exp_z = np.exp(z - np.max(z, axis=0, keepdims=True)) # overflow 방지 
    sum_exp_z = np.sum(exp_z, axis=0, keepdims=True)
    return (exp_z / sum_exp_z)

# cross_entropy_function
def loss_function(y_pred, y_true): 
    
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon) #로그의 무한대 발산을 막아 계산 안정성 유지
    Jw = -np.mean(np.sum(y_true.T * np.log(y_pred), axis=1)) ## axis = 1은 150
    
    return Jw

class NeuralNet:
    def __init__(self, config_layer):
        self.cf = config_layer
        
        # weight, bias initialize
        self.W1 = np.random.standard_normal((self.cf[1], self.cf[0])) # (input * h1) matrix로 랜덤 난수 생성
        self.W2 = np.random.standard_normal((self.cf[2], self.cf[1]))
        self.W3 = np.random.standard_normal((self.cf[3], self.cf[2]))
        self.W4 = np.random.standard_normal((self.cf[4], self.cf[3]))
        self.W5 = np.random.standard_normal((self.cf[5], self.cf[4]))
        
        self.b1 = np.random.standard_normal((self.cf[1], 1)) # (input * 1) matrix로 랜덤 난수 생성
        self.b2 = np.random.standard_normal((self.cf[2], 1))
        self.b3 = np.random.standard_normal((self.cf[3], 1))
        self.b4 = np.random.standard_normal((self.cf[4], 1))
        self.b5 = np.random.standard_normal((self.cf[5], 1))
      

    def forward(self, x): # 여기서 x는 x.T (tranpose)
           
        # hidden1    
        self.z1 = self.W1 @ x + self.b1 # x:(4, 150), self.z1:(h1, 150)
        self.a1 = relu(self.z1)
        
        # hidden2
        self.z2 = self.W2 @ self.a1 + self.b2 # (h2, 150)
        self.a2 = relu(self.z2)
        
        # hidden3
        self.z3 = self.W3 @ self.a2 + self.b3
        self.a3 = relu(self.z3)
        
        # hidden4
        self.z4 = self.W4 @ self.a3 + self.b4
        self.a4 = relu(self.z4)
        
        # Output
        self.z5 = self.W5 @ self.a4 + self.b5 # (Output, 150)
        self.a5 = softmax(self.z5)
        
        return self.a5
        
    # Backpropagation   
    def backward(self, x, y_true, lr): # update
        m = x.shape[1] # 150 
        
        # delta
        d5 = (self.a5 - y_true.T) # (Output(3), 150), J(w, b)를 z5로 미분
        d4 = (self.W5.T @ d5) * d_relu(self.a4) # (h4, 150) ## 앞부분이 delta * dz/da(-1), 뒷 부분이 da(-1)/dz(-1)
        d3 = (self.W4.T @ d4) * d_relu(self.a3)
        d2 = (self.W3.T @ d3) * d_relu(self.a2)
        d1 = (self.W2.T @ d2) * d_relu(self.a1)
        #print(d1.shape, d2.shape, d3.shape) #(3, 100), (2, 100), (1, 100)
        
        #Gradient Descent
        self.W5 -= lr * (1/m) * d5 @ self.a4.T # (Output, hidden4) # (z를 w로 미분) = a 니까 그걸 delta에 곱해줘
        self.W4 -= lr * (1/m) * d4 @ self.a3.T
        self.W3 -= lr * (1/m) * d3 @ self.a2.T
        self.W2 -= lr * (1/m) * d2 @ self.a1.T
        self.W1 -= lr * (1/m) * d1 @ x # (150, 4)인 x가 와야함. 그래서 x.T가 아님
        
        self.b5 -= lr * np.mean(d5, axis=1, keepdims=True) 
        self.b4 -= lr * np.mean(d4, axis=1, keepdims=True)
        self.b3 -= lr * np.mean(d3, axis=1, keepdims=True)
        self.b2 -= lr * np.mean(d2, axis=1, keepdims=True)
        self.b1 -= lr * np.mean(d1, axis=1, keepdims=True)
        
    

#
config_layer = [4, 10, 20, 10, 5, 3] # input, h1, h2, h3, h4, output 
model = NeuralNet(config_layer) ##

#
lr = 0.000001
iteration = 10000
loss_history = [] 

for i in range(iteration):
    model.forward(x.T) 
    
    loss = loss_function(model.a5, y)
    loss_history.append(loss)
    
    model.backward(x, y, lr)
    
# Loss curve

plt.plot(loss_history)
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.show()

