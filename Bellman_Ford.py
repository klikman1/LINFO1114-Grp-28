import numpy as np
import math

def Bellman_Ford(input_matrix: np.array):
    distance_matrix = np.copy(input_matrix) #copy of the input
    n = distance_matrix.shape[0] # n -> number of edges in a graph
    """
    pre 'distance_matrix' matrix of distances with size nXn where n is the number of nedges in the graph
    post returns the shortest path matrix
    post if the matrix contains negative clycles returns the mensaje "Negative Clycle"
    """
    for k in range(n):
        for i in range(n):
            for j in range(n):
                w = distance_matrix[k][j]
                if distance_matrix[i][j] > distance_matrix[i][k] + w: #relaxation step
                    distance_matrix[i][j] = distance_matrix[i][k]+ w # update the values
    # verification of negative cycles 
    for i in range(n):
        for j in range(n-1): 
            w = distance_matrix[i][j]       
            if distance_matrix[i][j] > distance_matrix[i][j+1] + w:
                return "Cycle negatif"
    return distance_matrix