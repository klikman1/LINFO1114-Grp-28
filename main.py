import csv
import numpy as np
import math

#theMinimum and Dijkstra functions are not yet functional
def TheMinimum(vector, index, recentMin):
    min = recentMin
    theId = index
    while index < len(vector):
        if vector[index] <= min:
            min = vector[index]
            theId = index
        
        index += 1

    return min, theId 

def Dijkstra_algorithm(A):
    
    L = np.zeros(len(A))
    S = np.array([])
    M = np.copy(A)
    u = 0
    v = u+1
    toBeReturned= np.empty((0,10))
    
    #I initialize the all indices of L to 'inf' except the first one
    for i in range(1, len(M)):
        L[i] = math.inf

    # I copy the first index in S as it is the smallest distance
    MinDist, id = TheMinimum(L, 0, len(S))
    S = np.append(S, MinDist)
    for i in range(len(M)):
        u = i
        v = u+1
        MinDist, id  = TheMinimum(L, i, S[len(S)-1])
        if not(MinDist in S):
            S = np.append(S, MinDist)
            
        
        for j in range(i+1, len(M[i])):
            W = M[i][j]

            if L[v] == math.inf or (L[u] + W) < L[v]:
                L[v] = (L[u] + W)
            v += 1   
        toBeReturned = np.vstack([toBeReturned, L])
        print(S)
    
    return toBeReturned

"""
Our function main has:
1. To read the Csv file
2. To run our 3 functions and 
3. print the matrix of the csv file + the result returned by
all the 3 functions.
"""
mainMatrix = np.empty((0,10))
#Here, we are reading the csv file
with open("MatriceDesCouts.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter = ",")
    for row in reader:
        array_row = []
        for n in row:
            array_row.append(float(n))
        array_row = np.array([array_row])
        mainMatrix = np.vstack([mainMatrix, array_row]) 


#Here, We are calling our functions
res1 = Dijkstra_algorithm(mainMatrix)

#Here, We are printing the main matrix and the results returned by our functions
print("La matrice des coûts\n")
print(mainMatrix)
print("\n")

print("La matrice retourné par la fonction Dijsktra\n")
print(res1)
print("\n")

print("La matrice retourné par la fonction Bellman_Ford\n")
print("--------------------------------")
print("\n")

print("La matrice retourné par la fonction Floyd_Warshall\n")
print("--------------------------------")
print("\n")

