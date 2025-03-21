import numpy as np


def eigen_finder(matrix: np.ndarray):
    r, c = matrix.shape
    if r != c:
        return []

    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return list(eigenvalues)


def frobenious_norm_finder(matrix: np.ndarray):
    return float(np.linalg.norm(matrix, "fro"))


def infinity_norm_finder(matrix: np.ndarray):
    return float(np.linalg.norm(matrix, np.inf))


def min_max_normalizer(matrix: np.ndarray):
    matrix = matrix.astype(float)
    matrix_min = np.min(matrix)
    matrix_max = np.max(matrix)
    if matrix_min == matrix_max:
        return np.zeros_like(matrix, dtype=float)
    matrix = (matrix - matrix_min) / (matrix_max - matrix_min)
    return matrix
