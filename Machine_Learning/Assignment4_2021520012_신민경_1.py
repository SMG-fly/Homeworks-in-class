import csv
import matplotlib.pyplot as plt
import numpy as np

x_TV = []
y_Sales = []

#파일
f = open('./advertising.csv', 'r', encoding = 'utf-8')
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
epoch = 1000

#J(w)
def loss_function(y_hat, y_Sales):
    return np.mean((y_hat - y_Sales)**2) /2 

#update
for i in range(epoch):
    for j in range(len(x_TV)):
        rand_idx = np.random.randint(len(x_TV))
        x_rand = x_TV[rand_idx]
        y_rand = y_Sales[rand_idx]
        
        y_hat = w1 * x_rand + b
    
        dw1 = np.mean((y_hat - y_rand) * x_TV)
        db = np.mean(y_hat - y_rand) 
    
        w1 = w1 - lr * dw1
        b = b - lr * db

#output_plot
plt.scatter(x_TV, y_Sales, s=10)
plt.plot(x_TV, w1 * x_TV + b, color='red')
plt.xlabel('TV')
plt.ylabel('Sales')
plt.grid(True)

plt.tight_layout()
plt.show()
    
