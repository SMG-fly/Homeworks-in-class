#import numpy as np
import matplotlib.pyplot as plt
#import mglearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.tree import plot_tree

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, test_size=0.1, random_state=42)

#tree = DecisionTreeClassifier(random_state=0)
#tree = DecisionTreeClassifier(random_state=0, min_samples_leaf=5)
tree = DecisionTreeClassifier(random_state=0, max_depth=6)
tree.fit(X_train, y_train)

print("Accuracy on training set: {:.3f}".format(tree.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(tree.score(X_test, y_test)))

plt.figure(figsize=(12, 6))
plot_tree(tree, class_names=["malignant", "benign"], feature_names=cancer.feature_names,
          impurity=False, filled=True, rounded=True, fontsize=8)
plt.show()