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
w1 = np.linspace(-3, 3, 300)
b = 0

#J(w)
def loss_function(y_hat, y_Sales):
    return np.sum((y_hat - y_Sales)**2) /2

#update
losses = []
for w1_one in w1:
    
    w1_one_losses = []
    for i in range(len(x_TV)):
        y_hat = w1_one * x_TV[i] + b
    
        loss = loss_function(y_hat, y_Sales)
        w1_one_losses.append(loss)

    losses.append(np.mean(w1_one_losses))

#output_plot
plt.plot(w1, losses)
plt.xlabel('w1')
plt.ylabel('Average Loss')
plt.grid(True)
plt.title('Loss Surface 2D')

plt.tight_layout()
plt.show()
    