import mglearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# generate dataset
X, y = mglearn.datasets.make_forge()

#plot dataset
mglearn.discrete_scatter(X[:,0], X[:, 1], y)
plt.legend(['Class 0', 'Class 1'], loc=4)
plt.xlabel('First feature')
plt.ylabel('Second feature')
plt.show()
print('X.shape: {}'.format(X.shape))

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# make model --> model??
clf = KNeighborsClassifier(n_neighbors=3) # KNeighborsClassifier 객체 생성
clf.fit(X_train, y_train) # 데이터를 학습

# prediction
y_test_hat = clf.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_test_hat)
print(accuracy)

# k = 1, 3, 9
fig, axes = plt.subplots(1, 3, figsize = (10, 3))

for n_neighbors, ax in zip([1, 3, 9], axes):
    #객체 생성 및 데이터 학습을 한 줄로 할 수 있다.
    clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
    
    mglearn.plots.plot_2d_separator(clf, X, fill=True, eps = 0.5, ax=ax, alpha=.4) # draw deicision boundary
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
    ax.set_title("{} neighbor(s)".format(n_neighbors))
    ax.set_xlabel("feature 0")
    ax.set_ylabel("feature 1")
    
axes[0].legend(loc=3)
plt.show()