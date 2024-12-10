import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.3, stratify=cancer.target, random_state=66)

training_accuracy = []
test_accuracy = []

# try n_neighbors from 1 to 10
for p in range(1, 21): # dimension
    for n_neighbors in range(1, 51): 
        # build the model
        clf = KNeighborsClassifier(n_neighbors=n_neighbors, p=p)
        clf.fit(X_train, y_train)
        
        # record training set accuracy
        training_accuracy.append(clf.score(X_train, y_train)) # clf.score : 예측을 수행하고, 이 예측의 정확도를 계산
        
        # record generalization accuracy
        test_accuracy.append(clf.score(X_test, y_test))

#print(training_accuracy)
#print(test_accuracy)

# find max accuracy
max_test_accuracy = max(test_accuracy)
index_of_max_accuracy = test_accuracy.index(max_test_accuracy)
optimal_n_neighbors = (index_of_max_accuracy // 20) + 1  # p가 20번 돌면 1씩 커지므로
optimal_p = (index_of_max_accuracy % 20) + 1  

print("Max test accuracy:", max_test_accuracy)
print("Optimal n_neighbors:", optimal_n_neighbors)
print("Optimal p:", optimal_p)

# accuracy plot
# Plotting training and test accuracies
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
for p in range(1, 21): # training accuracy
    plt.plot(range(1, 51), training_accuracy[(p-1)*50:p*50], label=f"p={p}")

plt.ylim(0.9, 1)
plt.xlabel("n_neighbors")
plt.ylabel("Accuracy")
plt.title("Training Accuracy")
plt.legend()
    

plt.subplot(1, 2, 2)
for p in range(1, 21): # test accuracy
    plt.plot(range(1, 51), test_accuracy[(p-1)*50:p*50], label=f"p={p}")

plt.ylim(0.9, 1)
plt.xlabel("n_neighbors")
plt.ylabel("Accuracy")
plt.title("Test Accuracy")
plt.legend()


plt.show()


