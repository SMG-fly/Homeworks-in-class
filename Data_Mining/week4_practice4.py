import mglearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge #
from sklearn.linear_model import Lasso #
import numpy as np
import matplotlib.pyplot as plt


X, y = mglearn.datasets.load_extended_boston()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Ridge (alpha=0.1)
ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)

# Lasso (alpha=1)
lasso = Lasso().fit(X_train, y_train)
print("Training set score: {:.2f}".format(lasso.score(X_train, y_train)))
print("Test set score: {:.2f}".format(lasso.score(X_test, y_test)))
print("Number of features used: ", np.sum(lasso.coef_ != 0)) # 죽지 않은 값은 몇 개?

# Lasso (alpha=0.01)
lasso001 = Lasso(alpha=0.01, max_iter=100000).fit(X_train, y_train)
print("Training set score: {:.2f}".format(lasso001.score(X_train, y_train)))
print("Test set score: {:.2f}".format(lasso001.score(X_test, y_test)))
print("Number of features used: ", np.sum(lasso001.coef_ != 0))

# Lasso (alpha=0.0001)
lasso00001 = Lasso(alpha=0.0001).fit(X_train, y_train)
print("Training set score: {:.2f}".format(lasso00001.score(X_train, y_train)))
print("Test set score: {:.2f}".format(lasso00001.score(X_test, y_test)))
print("Number of features used: ", np.sum(lasso00001.coef_ != 0))

# Plot
plt.plot(lasso.coef_, 's', label="Lasso alpha=1")
plt.plot(lasso001.coef_, "^", label="Lasso alpha=0.01")
plt.plot(lasso00001.coef_, "v", label="Lasso alpha=0.0001")

plt.plot(ridge01.coef_, "o", label="Ridge alpha=0.1")

plt.legend(ncol=2, loc=(0, 1.05))
plt.ylim(-25, 25)
plt.xlabel("Coefficient index")
plt.ylabel("Coefficient magnitude")

plt.show()

# Result
'''
Training set score: 0.94
Test set score: 0.78
Number of features used:  102
'''