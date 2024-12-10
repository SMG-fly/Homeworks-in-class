# Regression

import mglearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

X, y = mglearn.datasets.make_wave(n_samples=40)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

reg = KNeighborsRegressor(n_neighbors=3)
reg.fit(X_train, y_train)

print("Test set ground truth:\n", y_test)
print("Test set predictions:\n", reg.predict(X_test))

# prediction
y_test_hat = reg.predict(X_test)

# Evaluation 
print('MAE:', mean_absolute_error(y_test, y_test_hat))
print('RMSE:', mean_squared_error(y_test, y_test_hat)**0.5)
print('R_square:', r2_score(y_test, y_test_hat))


