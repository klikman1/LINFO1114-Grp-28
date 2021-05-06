import numpy as np


def Floyd_Warshall(input_matrix: np.array) -> np.array:
    """ Calculates a matrix containing the minimum cost from a point to another.
    :param input_matrix: The weighted matrix of the graph (n x n).
    :return: distance_matrix (n x n)
    """
    # We copy the input array in order to not modify it
    distance_matrix = np.copy(input_matrix)
    # We get the dimensions
    n = distance_matrix.shape[0]
    # We apply the Floyd Warshall Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
    return distance_matrix
