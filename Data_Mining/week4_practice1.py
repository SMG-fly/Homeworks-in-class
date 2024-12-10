# Linear Regression
import mglearn
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression #
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

mglearn.plots.plot_linear_regression_wave()

X, y = mglearn.datasets.make_wave(n_samples=60)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Regression
reg = LinearRegression()
reg.fit(X_train, y_train)
#lr(linear regression) = LinearRegression().fit(X_train, y_train) # 같은 거임

# Prediction
y_test_hat = reg.predict(X_test)

# Evaluation
print("reg.coef_:", reg.coef_) # 기울기(w)
print("reg.intercept_:", reg.intercept_) # y절편(b)

print("Training set score: {:.2f}".format(reg.score(X_train, y_train)))
print("Test set score: {:.2f}".format(reg.score(X_test, y_test)))

# Result
'''
w[0]: 0.393906  b: -0.031804
reg.coef_: [0.39390555]
reg.intercept_: -0.031804343026759746
Training set score: 0.67
Test set score: 0.66
'''