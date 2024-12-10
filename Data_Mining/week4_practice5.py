# Logistic Regression - forge

import mglearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression #
import matplotlib.pyplot as plt

X, y = mglearn.datasets.make_forge()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_test_hat = logreg.predict(X_test)
print(y_test)
print(y_test_hat)

print("Training set score: {:.2f}".format(logreg.score(X_train, y_train)))
print("Test set score: {:.2f}".format(logreg.score(X_test, y_test)))

# Result
'''
[1 1 1 1 1 1 0]
[1 1 1 1 0 1 0]
Training set score: 0.95
Test set score: 0.86
'''

# Plot
fig, axes = plt.subplots(1, 2, figsize=(10, 3))
mglearn.plots.plot_2d_separator(logreg, X_train, fill=False, eps=0.5, ax=axes[0], alpha=.7)

mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train, ax=axes[0])
axes[0].set_title("Training data")
axes[0].set_xlabel("Feature 0")
axes[0].set_ylabel("Feature 1")
mglearn.plots.plot_2d_separator(logreg, X_test, fill=False, eps=0.5, ax=axes[1], alpha=.7)

mglearn.discrete_scatter(X_test[:, 0], X_test[:, 1], y_test, ax=axes[1])
axes[1].set_title("Test data")
axes[1].set_xlabel("Feature 0")
axes[1].set_ylabel("Feature 1")

plt.show()