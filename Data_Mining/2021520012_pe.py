import numpy as np

def PerformanceEvaluator(y_true, y_pred, print_confusion=False):
    
    # confusion matrix
    num_classes = max(max(y_true), max(y_pred)) + 1 # include 0
    confusion_matrix = np.zeros(shape=(num_classes, num_classes))
    for true, pred in zip(y_true, y_pred): # 같은 순서의 값들 짝꿍 만들어주기
        confusion_matrix[true, pred] += 1
        
    # TP, TN, FP, FN    
    true_po = np.diag(confusion_matrix) # 대각 성분 추출 # 벡터값
    false_ne = np.sum(confusion_matrix, axis=1) - true_po
    false_po = np.sum(confusion_matrix, axis=0) - true_po
   
    # Accuracy
    accuracy = np.sum(true_po) / len(y_true) # TP/전체
    
    # recall(average)
    recall_vector = true_po / (true_po + false_ne) # each class
    recall_avg = np.mean(recall_vector)
    
    # precision(average)
    precision_vector = true_po / (true_po + false_po) # each class
    precision_avg = np.mean(precision_vector)
    
    # F1-score
    F1_vector = 2 * (precision_vector * recall_vector) / (precision_vector + recall_vector)
    F1_score_Mac_avg = np.mean(F1_vector)

    # print outcome
    print(f'Accuracy: {accuracy}')
    print(f'Recall(average): {recall_avg}')
    print(f'Precision(average): {precision_avg}')
    print(f'F1-score: {F1_score_Mac_avg}')

    # print confusion matrix
    if print_confusion:
        print('Confusion Matrix:')
        print(confusion_matrix)

# example
y_true_example = [0, 0, 1, 1, 2, 2, 2]
y_pred_example = [0, 1, 1, 2, 2, 2, 1]

# call function
PerformanceEvaluator(y_true_example, y_pred_example, True)