import numpy as np

def optimal_bst(p, q, n):
    e = np.zeros((n+2, n+1))
    w = np.zeros((n+2, n+1))
    root = np.zeros((n+1, n+1), dtype=int)
    
    for i in range(1, n+2):
        e[i][i-1] = q[i-1]
        w[i][i-1] = q[i-1]
    
    for l in range(1, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            e[i][j] = float('inf')
            w[i][j] = w[i][j-1] + p[j-1] + q[j]
            for r in range(i, j+1):
                t = e[i][r-1] + e[r+1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    return e, root

def construct_optimal_bst(root, i, j):
    if i <= j:
        r = root[i][j]
        print(f'k{r}', end='')
        if i == j:
            return
        print('(', end='')
        construct_optimal_bst(root, i, r-1)
        construct_optimal_bst(root, r+1, j)
        print(')', end='')

# Given probabilities
p = [0.04, 0.06, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05, 0.05]
n = 7

e, root = optimal_bst(p, q, n)

print("Cost of optimal BST:", e[1][n])
print("Structure of optimal BST:")
construct_optimal_bst(root, 1, n)
print()
