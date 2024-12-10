# Logistic Regression - breast cancer

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression #
from sklearn.linear_model import Ridge #
from sklearn.linear_model import Lasso #
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

diabetes = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, random_state=15)

# Linear Regression
lr = LinearRegression().fit(X_train, y_train)
lr_rmse = mean_squared_error(y_test, lr.predict(X_test), squared=False)
print("Linear Regression coefficient:", lr.coef_) 
print("Linear Regression intercept:", lr.intercept_) 
print("Linear Regression RMSE:", lr_rmse)

# Ridge Regression
ridge_alpha_values = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
best_ridge_rmse = float('inf') # 초기값 무한대로 설정(infinite)
best_ridge_alpha = None

for alpha in ridge_alpha_values:
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train, y_train)
    rmse = mean_squared_error(y_test, ridge.predict(X_test), squared=False)
    if rmse < best_ridge_rmse:
        best_ridge_rmse = rmse
        best_ridge_alpha = alpha

best_ridge_model = Ridge(alpha=best_ridge_alpha)
best_ridge_model.fit(X_train, y_train)

print("Best ridge alpha:", best_ridge_alpha)
print("Best ridge coefficients:", best_ridge_model.coef_)
print("Best ridge intercept:", best_ridge_model.intercept_)
print("Best ridge RMSE:", best_ridge_rmse)

# Lasso Regression
lasso_alpha_values = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
best_lasso_rmse = float('inf') # 초기값 무한대로 설정(infinite)
best_lasso_alpha = None

for alpha in lasso_alpha_values:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    rmse = mean_squared_error(y_test, lasso.predict(X_test), squared=False)
    if rmse < best_lasso_rmse:
        best_lasso_rmse = rmse
        best_lasso_alpha = alpha

best_lasso_model = Lasso(alpha=best_lasso_alpha)
best_lasso_model.fit(X_train, y_train)

print("Best lasso alpha:", best_lasso_alpha)
print("Best lasso coefficients:", best_lasso_model.coef_)
print("Best lasso intercept:", best_lasso_model.intercept_)
print("Best lasso RMSE:", best_lasso_rmse)

# print feature name
#print(diabetes.feature_names) 
#print(diabetes.DESCR)