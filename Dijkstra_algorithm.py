import numpy as np
import math

def TheMinimumDistance(Label, nodeInTheFridge, sizeOfInputMatrix):
    """
    For a given label, Calculate the shortest distance in it but first, check if the given distance isn't already in the fridge
    :parameters
    Label: list
        Equivalent of L
    
    nodeInTheFridge: list
        Equivalent of a list of nodes (A to J)
    
    sizeOfInputMatrix: int 
        The length of the inputMatrix

    :return : 
        The shortest distance found, it's index
    """
    minimumDistance = math.inf
    idx = -10 #If all nodes were visited it will return this 
    for i in range(sizeOfInputMatrix):
        if not(nodeInTheFridge[i]) and Label[i] < minimumDistance:
            minimumDistance = Label[i]
            idx = i
    return minimumDistance, idx 

def Dijkstra_algorithm(A):
    """
    Source inspired from : https://www.algorithms-and-technologies.com/dijkstra/python
    As each row represents a letter( == node), we do the Dijkstra algorithm from each node to the node J.
    Returns a matrix of shortest distance between each pair of nodes.
    :param A: matrix
        np.matrix of n * n 
    :return toBeReturned: matrix
        np.matrix of n*n
    """
    toBeReturned = np.empty((0,len(A)))
    for row_number in range (len(A)):
        L = np.array([math.inf for _ in range(len(A))])
        nodeBeenVisited = np.array([False for _ in range(len(A))])
        S = np.empty((0,len(A)))
        index = 0
        #I initialize all indices of L to 'inf' except the node we are on 
        #because the shortest distance from a node to itself is 0. 
        #For ex: If we want to calculate the shortest distance from A to J, We will have L = [0, inf, inf, inf, ...]
        #        If we want from B to J, We will have L = [inf, 0, inf, inf, ...]
        #That's what we are doing below
        L[row_number] = 0

        while index != -10:
            MinDist, index = TheMinimumDistance(L, nodeBeenVisited, len(A))
            
            if not (MinDist in S):
                S = np.append(S, MinDist) #We put the node (in our case, it's the shortest distance found now) in the frigde
            for i in range(len(A[index])):# We apply the dijkstra algorithm.
                W = A[index][i]
                if L[i] > (L[index] + W):
                    L[i] = (L[index] + W)
            
            nodeBeenVisited[index] = True # Help us to make sure all nodes were visisted.
        toBeReturned = np.vstack([toBeReturned, L])
    return toBeReturned