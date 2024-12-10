import numpy as np
A = np.array ([[1, 2, 3], [4, 5, 6]])
a = np.pad(A, ((1,2), (0,1)), 'constant', constant_values=2) #((위 행, 아래 행), (왼쪽 열, 오른쪽 열)) // 2(constant_values)로 채워라.
print(a)

