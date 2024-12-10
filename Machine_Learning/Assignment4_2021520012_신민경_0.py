import csv
import matplotlib.pyplot as plt
import numpy as np

x_TV = []
y_Sales = []

#파일
f = open('advertising.csv', 'r', encoding = 'utf-8')
rdr = csv.reader(f)
header = next(rdr)
for line in rdr:
    #print(line)
    x_TV.append(float(line[0]))
    y_Sales.append(float(line[3])) 
    
f.close()

#
x_TV = np.array(x_TV)
y_Sales = np.array(y_Sales)

#
w1 = 0
b = 0

#
lr = 0.0000001
iteration = 100000

#J(w) #Loss 그래프 안 그리면 이 부분 필요 없음
def loss_function(y_hat, y_Sales):
    return np.mean((y_hat - y_Sales)**2) /2 

#update
for i in range(iteration):
    y_hat = w1 * x_TV + b
    
    dw1 = np.mean((y_hat - y_Sales) * x_TV) 
    db = np.mean(y_hat - y_Sales) 
    
    w1 = w1 - lr * dw1
    b = b - lr * db

#output_plot
plt.scatter(x_TV, y_Sales, s=20)
plt.plot(x_TV, w1 * x_TV + b, color='red')
plt.xlabel('TV')
plt.ylabel('Sales')
plt.grid(True)

plt.tight_layout()
plt.show()
    
