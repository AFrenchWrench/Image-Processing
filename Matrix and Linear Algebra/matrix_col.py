import numpy as np


r = int(input())

matrix = []


for _ in range(r):
    matrix.append(list(map(float, input().split())))

matrix = np.array(matrix, dtype=float)

eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(" ".join(map("{:.3f}".format, eigenvalues)))

for i in range(r):
    print(" ".join(map("{:.3f}".format, eigenvectors[:, i])))
