import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x_TV = []
y_Sales = []

#파일
with open('advertising.csv', 'r', encoding = 'utf-8') as f:
    rdr = csv.reader(f)
    header = next(rdr)
    for line in rdr:
    #print(line)
        x_TV.append(float(line[0]))
        y_Sales.append(float(line[3])) 
    
#
x_TV = np.array(x_TV)
y_Sales = np.array(y_Sales)

# parameter 초기화
w_range = np.linspace(0.0, 0.1, 200)
b_range = np.linspace(0, 10, 200)

w1, b = np.meshgrid(w_range, b_range)

#J(w)
def loss_function(y_hat, y_Sales):
    return np.mean((y_hat - y_Sales)**2) /2

#update
losses = np.zeros_like(w1)
for i in range(w1.shape[0]):
    for j in range(b.shape[0]):
        y_hat = w1[i, j] * x_TV + b[i, j] #특정한 w1과 b의 조합
        loss = loss_function(y_hat, y_Sales)
        losses[i, j] = loss


#output_plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(w1, b, losses, cmap='viridis')

ax.set_xlabel('Weight (w)')
ax.set_ylabel('Bias (b)')
ax.set_zlabel('Loss')

plt.title('Loss Surface (Linear Regression)')

plt.show()