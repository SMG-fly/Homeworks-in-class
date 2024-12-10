#import numpy as np
import matplotlib.pyplot as plt
#import mglearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
#from sklearn.tree import plot_tree

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)

tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train, y_train)

print("Accuracy on training set: {:.3f}".format(tree.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(tree.score(X_test, y_test)))

# varying the hyperparameter min_samples_leaf
training_accuracy = []
test_accuracy = []
max_depth = []

m_settings = [1, 2, 5, 7, 10, 20]
for m in m_settings:
    tree = DecisionTreeClassifier(min_samples_leaf=m, random_state=0)
    tree.fit(X_train, y_train)
    
    training_accuracy.append(tree.score(X_train, y_train))
    test_accuracy.append(tree.score(X_test, y_test))
    max_depth.append(tree.tree_.max_depth)
    
print("training accuracy: ", training_accuracy)
print("test accuracy: ", test_accuracy)
print("max_depth: ", max_depth)