import numpy as np

# A = np.array([[1, 2], [3, 4]])
# print(A.shape)

# B = np.array([[5, 6], [7, 8]])
# print(B.shape)

# print(np.dot(A, B))

X = np.array([1, 2])
print(X.shape)

W = np.array([[1, 3, 5], [2, 4, 6]])
print(W)
print(W.shape)

Y = np.dot(X, W)
print(Y)