import numpy as np
import math

def TheMinimumDistance(Label, passedByTheNode, sizeOfInputMatrix):
    """
    For a given label, Calculate the shortest distance in it but first, check if the given distance isn't already in the fridge
    :parameters
    Label: list
        Equivalent of L
    
    passedByTheNode: list
        List that contains only booleans. 
        True at ith index if the node at ith index has been visited. False otherwise 
    
    sizeOfInputMatrix: int 
        The length of the inputMatrix

    :return : 
        The shortest distance found, it's index
    """
    minimumDistance = math.inf
    idx = 0
    for i in range(sizeOfInputMatrix):
        if not(passedByTheNode[i]) and Label[i] < minimumDistance:
            minimumDistance = Label[i]
            idx = i
    return minimumDistance, idx 

def Dijkstra_algorithm(A):
    """
    The following code was inspired from the pseudo code of the course in slides of chapter 10.
    Here the link : https://moodleucl.uclouvain.be/pluginfile.php/2225287/mod_resource/content/3/Chapter10.pdf
    
    As each row represents a letter( == node), we do the Dijkstra algorithm on each row from each node to the node J.
    Returns a matrix of shortest distance between each pair of nodes.
    :param A: matrix
        np.matrix of n * n 
    :return toBeReturned: matrix
        np.matrix of n*n
    """
    toBeReturned = np.empty((0,len(A)))
    for row_number in range (len(A)):
        
        finished = False
        
        nodeBeenVisited = np.array([False for _ in range(len(A))])
        
        L = np.array([math.inf for _ in range(len(A))])

        #I initialize all indices of L to 'inf' except the node we are on 
        #because the shortest distance from a node to itself is 0. 
        #For ex: If we want to calculate the shortest distance from A to J, We will have L = [0, inf, inf, inf, ...]
        #        If we want the shortest distance from B to J, We will have L = [inf, 0, inf, inf, ...]
        #That's what we are doing below
        L[row_number] = 0
        S = np.empty((0,len(A)))

        while not(finished):
            MinDist, index = TheMinimumDistance(L, nodeBeenVisited, len(A))
            
            if not (MinDist in S):
                S = np.append(S, MinDist) 
            for i in range(len(A[index])):
                W = A[index][i]
                if L[i] > (L[index] + W):
                    L[i] = (L[index] + W)
            
            nodeBeenVisited[index] = True # The node was visisted.
            if np.all((nodeBeenVisited== True)): #Check if all nodes were visited
                finished = True

        toBeReturned = np.vstack([toBeReturned, L])
    return toBeReturned
