import numpy as np
import math

def Bellman_Ford(input_matrix: np.array):
    distance_matrix = np.copy(input_matrix)
    n = distance_matrix.shape[0]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                w = distance_matrix[k][j]
                if distance_matrix[i][j] > distance_matrix[i][k] + w:
                    distance_matrix[i][j] = distance_matrix[i][k]+ w
    for i in range(n):
        for j in range(n-1): 
            w = distance_matrix[i][j]       
            if distance_matrix[i][j] > distance_matrix[i][j+1] + w:
                return "Cycle negatif"
    return distance_matrix