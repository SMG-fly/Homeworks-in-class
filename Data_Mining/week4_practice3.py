import mglearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression #
from sklearn.linear_model import Ridge #
import matplotlib.pyplot as plt


X, y = mglearn.datasets.load_extended_boston()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Linear Regression
lr = LinearRegression().fit(X_train, y_train)

# Ridge (alpha=1)
ridge = Ridge().fit(X_train, y_train)
print("Training set score: {:.2f}".format(ridge.score(X_train, y_train)))
print("Test set score: {:.2f}".format(ridge.score(X_test, y_test)))

# Ridge (alpha=10)
ridge10 = Ridge(alpha=10).fit(X_train, y_train)
print("Training set score: {:.2f}".format(ridge10.score(X_train, y_train)))
print("Test set score: {:.2f}".format(ridge10.score(X_test, y_test)))

# Ridge (alpha=0.1)
ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)
print("Training set score: {:.2f}".format(ridge01.score(X_train, y_train)))
print("Test set score: {:.2f}".format(ridge01.score(X_test, y_test)))

plt.plot(ridge.coef_, 's', label="Ridge alpha=1")
plt.plot(ridge10.coef_, "^", label="Ridge alpha=10")
plt.plot(ridge01.coef_, "v", label="Ridge alpha=0.1")

plt.plot(lr.coef_, "o", label="LinearRegression")
plt.xlabel("Coefficient index")
plt.ylabel("Coefficient magnitude")
xlims = plt.xlim()
plt.hlines(0, xlims[0], xlims[1]) # 무슨 의미인지 알아보기
plt.xlim(xlims)
plt.ylim(-25, 25)
plt.legend()

plt.show()

# Result
'''
Training set score: 0.87
Test set score: 0.81
Training set score: 0.77
Test set score: 0.73
Training set score: 0.92
Test set score: 0.82
'''
