import numpy as np
import math


def TheMinimum(vector, vectorToCompareTo, recentMin):
    min = recentMin
    theId = 0
    i = 0
    while i < len(vector):
        if not(vector[i] in vectorToCompareTo) and vector[i] <= min:
            min = vector[i]
            theId = i
        i += 1
    return min, theId 

def Dijkstra_algorithm(A):
    
    L = np.zeros(len(A))
    S = np.empty((0,10))
    u = 0
    v = u+1
    
    toBeReturned= np.empty((0,10))
    
    #I initialize the all indices of L to 'inf' except the first one
    for i in range(1, len(A)):
        L[i] = math.inf

    # I copy the first index in S as it is the smallest distance
    MinDist, id = TheMinimum(L, S, len(S))
    S = np.append(S, MinDist)
    i = id
    
    while (i < len(A)):
        for j in range(len(A[i])):
            W = A[i][j]

            if L[j] == math.inf or (L[i] + W) < L[j]:
                L[j] = (L[i] + W)
        MinDist, id = TheMinimum(L, S, S[len(S)-1])
        S = np.append(S, MinDist)
        i +=1
    toBeReturned = np.vstack([toBeReturned, L])
        
    
    return toBeReturned
