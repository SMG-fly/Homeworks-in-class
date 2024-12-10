import numpy as np
import matplotlib.pyplot as plt
import csv

def cal_dist(p, q): #이 함수가 0번 점과 target, 1번점과 target의 거리를 측정해줄 거야
    return np.sum((p - q)**2)

def assign_cluster(center0, center1, data, c): #거리를 비교해서 뭐랑 더 가까운지 알려줄거야. # c에 저장해둘거야
    for i in range(len(data)):
        a = cal_dist(data[i,:], center0)  #한 행씩 순자척으로 검사
        b = cal_dist(data[i,:], center1)
        if a < b:
            c[i] = 0
        else:
            c[i] = 1   
    return c

def set_means(data, c):
    center0 = np.mean(data[np.where(c==0)[0]], axis=0) #[0] 무슨 뜻이라고 하셨더라?
    center1 = np.mean(data[np.where(c==1)[0]], axis=0) #아마 인덱싱해서 1차원으로 가져오려고 한 게 아닐까 추측해.
    return center0, center1
 
def plotting(axes, data, center0, center1, c, center_only=False):
    if center_only: #그냥 scatter plot 출력하고 아래에서 평균값 점만 찍을거야.
        axes.scatter(x, y, c='tab:blue', s=20)
    else:
        points_c0 = data[np.where(c==0)] # 0번 점과 가까운 data #assign_instance() 참조
        points_c1 = data[np.where(c==1)] # 1번 점과 가까운 data #np.where(조건) --> 조건에 맞는 인덱스 반환
        axes.scatter(points_c0[:,0], points_c0[:,1], c='tab:olive', s=20)
        axes.scatter(points_c1[:,0], points_c1[:,1], c='tab:pink', s=20)
    axes.scatter(center0[0], center0[1], c='g', s=100, marker='*') #0번 점
    axes.scatter(center1[0], center1[1], c='r', s=100, marker='*') #marker1
    


f = open('./data.csv', 'r')
data = list(csv.reader(f))
data = np.array(data, dtype = 'float64')
x = data[:, 0]
y = data[:, 1]
c = np.zeros_like(x)

fig, axes = plt.subplots(2, 4)
for count in range(4):
    if count == 0:
        center0 = np.array([2.0, 2.0])
        center1 = np.array([2.2, 2.2])
    else:
        center0, center1 = set_means(data, c)
    
    plotting(axes[0, count], data, center0, center1, c, center_only=True) #scatter plot에 점만 찍을거야.
    
    c = assign_cluster(center0, center1, data, c) #clustering
    plotting(axes[1, count], data, center0, center1, c, center_only=False)
    
plt.tight_layout()
plt.show()
