import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data[:, [0, 1]], cancer.target, test_size=0.3, stratify=cancer.target, random_state=66)

# KNN 분류기 학습 및 예측
def plot_decision_boundary(X, y, n_neighbors):
    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    clf.fit(X, y)

    # decision boundary
    # grid 생성 
    h = 0.1  # mesh의 스텝 사이즈
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h)) 
    
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]) # ravel(): 다차원 배열 -> 1차원 배열로 펼쳐줌 # np.c_: 배열을 열로 연결 -> 2차원 배열
    # 즉, 좌표((x, y)) 생성 후 예측 진행하는 코드

    # 결과를 색상으로 표시
    Z = Z.reshape(xx.shape) # Z는 등고선 영역을 나타낸다. # 1차원 예측 결과를 다시 2차원 배열의 형태로 변환
    plt.contourf(xx, yy, Z, alpha=0.3, cmap=ListedColormap(['lightcoral', 'lightblue']))

# 각 K 값에 대한 결정 경계 그리기
plt.figure(figsize=(15, 5))
for i, k in enumerate([1, 3, 15]):
    plt.subplot(1, 3, i+1)
    plot_decision_boundary(X_train, y_train, k)
    plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=ListedColormap(['red', 'blue']), edgecolor='k', s=20)
    plt.title(f'Decision boundary (k={k})')
    plt.xlabel('Feature 0')
    plt.ylabel('Feature 1')
plt.tight_layout()
plt.show()
