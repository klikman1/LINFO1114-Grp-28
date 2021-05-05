#In this file we are going to create a .csv of our matrix(n*n) of costs C between a pair of vertices.
import math
import numpy as np
import csv

costMatrix = [[0, 4, 5, 4, math.inf, math.inf, math.inf, math.inf,math.inf,math.inf],
                [4, 0, 2, math.inf, 3, math.inf, 3, math.inf, math.inf, math.inf],
                [5, 2, 0, 3, 5, 3, math.inf, math.inf, math.inf, math.inf],
                [4, math.inf, 3, 0, math.inf, 4,math.inf, math.inf, 1, math.inf],
                [math.inf, 3, 5, math.inf, 0, 5, 1, 2, math.inf, math.inf],
                [math.inf, math.inf, 3, 4, 5, 0, math.inf, 2, 2, math.inf],
                [math.inf, 3, math.inf, math.inf, 1, math.inf, 0, 3, math.inf, 5],
                [math.inf, math.inf, math.inf, math.inf, 2, 2, 3, 0, 2, 1],
                [math.inf, math.inf, math.inf, 1, math.inf, 2, math.inf, 2, 0, 3],
                [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 5, 1, 3, 0]]

with open( 'MatriceDesCouts.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    
    writer.writerows(costMatrix)
    
    print("Csv file Created")