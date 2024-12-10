import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


titanic_data = pd.read_csv("titanic.csv")
#print(titanic_data)

X = titanic_data[['sex','age','n_siblings_spouses','parch','fare','class','deck','embark_town','alone']] 
y = titanic_data['survived']
#print(X)
#print(y)

# Label Encoding
X = X.copy()
label_encoder = LabelEncoder()
X['sex'] = label_encoder.fit_transform(X['sex'])
X['class'] = label_encoder.fit_transform(X['class'])
X['deck'] = label_encoder.fit_transform(X['deck'])
X['embark_town'] = label_encoder.fit_transform(X['embark_town'])
X['alone'] = label_encoder.fit_transform(X['alone'])
#print(X)
#print(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# varying the hyperparameter criterion
tree = DecisionTreeClassifier(random_state=1)
tree.fit(X_train, y_train)
#print("training_accuracy(gini)", tree.score(X_train, y_train)) # 0.9920159680638723
#print("test_accuracy(gini)", tree.score(X_test, y_test)) # 0.7301587301587301

tree = DecisionTreeClassifier(criterion="entropy", random_state=1)
tree.fit(X_train, y_train)
#print("training_accuracy(entropy)", tree.score(X_train, y_train)) # 0.9920159680638723
#print("test_accuracy(entropy)", tree.score(X_test, y_test)) # 0.7777777777777778


# varying the hyperparameter min_samples_leaf
training_accuracy_1 = []
test_accuracy_1 = []
max_depth_1 = []

m_settings = [1, 2, 5, 7, 10, 20]
for m in m_settings:
    tree = DecisionTreeClassifier(criterion="entropy", min_samples_leaf=m, random_state=1)
    tree.fit(X_train, y_train)
    
    training_accuracy_1.append(tree.score(X_train, y_train))
    test_accuracy_1.append(tree.score(X_test, y_test))
    max_depth_1.append(tree.tree_.max_depth)
    
print("training accuracy:", training_accuracy_1)
print("test accuracy:", test_accuracy_1)
print("max depth:", max_depth_1)

# best min_sample_leaf = 7
# best training accuracy = 0.8682634730538922
# best test accuracy = 0.7936507936507936
# best max depth = 17


# varying the hyperparameter max_depth
training_accuracy_2 = []
test_accuracy_2 = []
max_depth_2 = []

m_settings = [1, 2, 5, 7, 10, 20, 30, 100]
for m in m_settings:
    tree = DecisionTreeClassifier(criterion="entropy", min_samples_leaf=7, max_depth=m, random_state=1)
    tree.fit(X_train, y_train)
    
    training_accuracy_2.append(tree.score(X_train, y_train))
    test_accuracy_2.append(tree.score(X_test, y_test))
    max_depth_2.append(tree.tree_.max_depth)
    
#print("training accuracy:", training_accuracy_2)
#print("test accuracy:", test_accuracy_2)
#print("max depth:", max_depth_2)

# best max_depth = 5 // # depth가 커져도 accuracy 변화X, max_depth를 15이상 설정해도 depth는 17이상 늘어나지 않음 # 왜 이걸 줄여주는 게 좋지?
# best training accuracy = 0.8483033932135728 # training accuracy 조금 낮아져도 test가 높아짐
# best test accuracy = 0.8015873015873016

# selected tree
tree = DecisionTreeClassifier(criterion="entropy", min_samples_leaf=7, max_depth=5, random_state=1)
tree.fit(X_train, y_train)
    
# plot_tree 
'''
plt.figure(figsize=(12, 6))
plot_tree(tree, class_names=["dead", "survived"], feature_names=['sex','age','n_siblings_spouses','parch','fare','class','deck','embark_town','alone'],
          impurity=False, filled=True, rounded=True, fontsize=8)
plt.show()
'''