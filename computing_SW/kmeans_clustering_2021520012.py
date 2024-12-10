import numpy as np
import matplotlib.pyplot as plt
import csv

f = open('./data.csv', 'r')
data = list(csv.reader(f))
data = np.array(data, dtype='float64')
x = data[:, 0] #0열 전체
y = data[:, 1] #1열 전체


fig, axes = plt.subplots(2,4)
x_1, y_1 = [2.0, 2.0]
x_2, y_2 = [2.2, 2.2]
axes[0,0].scatter(x, y, s = 10)
axes[0,0].scatter(x_1, y_1, c = 'g', s=100, marker = '*') #marker 넣기
axes[0,0].scatter(x_2, y_2, c = 'r', s=100, marker = '*')

for i in range(3):
    x_1_list = []
    y_1_list = []
    x_2_list = []
    y_2_list = []
    list_1 = []
    list_2 = []
    
    for j in range(len(x)):
        diff_1 = ((x_1 - x[j])**2) + ((y_1 - y[j])**2)
        diff_2 = ((x_2 - x[j])**2) + ((y_2 - y[j])**2)
        if diff_1 < diff_2:
            x_1_list.append(x[j])
            y_1_list.append(y[j])
            list_1.append([x[j], y[j]])
        else:
            x_2_list.append(x[j])
            y_2_list.append(y[j])
            list_2.append([x[j], y[j]])
            
    axes[1,i].scatter(x_1_list, y_1_list, c = 'palegreen', s = 10)
    axes[1,i].scatter(x_2_list, y_2_list, c = 'salmon', s = 10)
    axes[1,i].scatter(x_1, y_1, c = 'g', s=100, marker = '*') #marker 넣기
    axes[1,i].scatter(x_2, y_2, c = 'r', s=100, marker = '*')
    
    x_1, y_1 = np.mean(np.array(list_1), axis = 0)
    x_2, y_2 = np.mean(np.array(list_2), axis = 0)
    
    axes[0,i+1].scatter(x, y, s = 10)
    axes[0,i+1].scatter(x_1, y_1, c = 'g', s=100, marker = '*') #marker 넣기
    axes[0,i+1].scatter(x_2, y_2, c = 'r', s=100, marker = '*')

i = 3
x_1_list = []
y_1_list = []
x_2_list = []
y_2_list = []
for j in range(len(x)):
        diff_1 = ((x_1 - x[j])**2) + ((y_1 - y[j])**2)
        diff_2 = ((x_2 - x[j])**2) + ((y_2 - y[j])**2)
        if diff_1 < diff_2:
            x_1_list.append(x[j])
            y_1_list.append(y[j])
        else:
            x_2_list.append(x[j])
            y_2_list.append(y[j])
            
axes[1,i].scatter(x_1_list, y_1_list, c = 'palegreen', s = 10)
axes[1,i].scatter(x_2_list, y_2_list, c = 'salmon', s = 10)
axes[1,i].scatter(x_1, y_1, c = 'g', s=100, marker = '*') #marker 넣기
axes[1,i].scatter(x_2, y_2, c = 'r', s=100, marker = '*')

plt.tight_layout()
plt.show()
f.close()