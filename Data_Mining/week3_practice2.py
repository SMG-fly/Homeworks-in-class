import mglearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X, y = mglearn.datasets.make_forge()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

# output 비교
y_test_hat = clf.predict(X_test)
print(y_test)
print(y_test_hat)

# calculate accuracy
y_train_hat = clf.predict(X_train)
print('train acc:', accuracy_score(y_train, y_train_hat))
y_test_hat = clf.predict(X_test)
print('test acc:', accuracy_score(y_test, y_test_hat))
