import numpy as np
import math
from Floyd_Warshall import Floyd_Warshall
import sys


def read_csv(file_name: str) -> np.array:
    """ Reads a CSV file which contains the weights matrix.
    :arg file_name : The pathname to the csv file.
    :return The numpy matrix of the input weighted matrix read from numpy.
    :raise AttributeError : If the dimension of the input is not squared.
    :raise FileNotFoundError : If the file is not found.
    """
    # Here, we are reading the csv file
    with open(file_name, "r") as csv_file:
        data = csv_file.readlines()
    # We are going to parse the csv file
    number_of_rows = len(data)
    to_return = np.zeros((number_of_rows, number_of_rows), dtype=float)
    for row_index in range(number_of_rows):
        data[row_index] = data[row_index].replace("\n", "").split(",")
        number_of_columns = len(data[row_index])
        if number_of_columns != number_of_columns:
            raise AttributeError(f"The matric is not squared ! {number_of_rows}x{number_of_columns}")
        for column_index in range(number_of_columns):
            to_return[row_index][column_index] = int(data[row_index][column_index]) if (
                    data[row_index][column_index] != "inf") else np.inf
    return to_return


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
    v = u + 1
    toBeReturned = np.empty((0, 10))

    # I initialize the all indices of L to 'inf' except the first one
    for i in range(1, len(M)):
        L[i] = math.inf

    # I copy the first index in S as it is the smallest distance
    MinDist, id = TheMinimum(L, 0, len(S))
    S = np.append(S, MinDist)
    for i in range(len(M)):
        u = i
        v = u + 1
        MinDist, id = TheMinimum(L, i, S[len(S) - 1])
        if not (MinDist in S):
            S = np.append(S, MinDist)

        for j in range(i + 1, len(M[i])):
            W = M[i][j]

            if L[v] == math.inf or (L[u] + W) < L[v]:
                L[v] = (L[u] + W)
            v += 1
        toBeReturned = np.vstack([toBeReturned, L])
        print(S)

    return toBeReturned


def main(input_csv_file: str = "MatriceDesCouts.csv"):
    """ Executes the program :
          (1) Read the CSV input file,
          (2) Run our 3 functions and
          (3) print the matrix of the csv file with the result returned by all the 3 functions.
    :arg input_csv_file : The pathname to the csv file that contains the weighted matrix.
    :return: None.
    """
    input_matrix = read_csv(input_csv_file)
    print(f"{'*' * 8} Input Matrix From CSV {'*' * 8}")
    print(input_matrix)

    floyd_warshall_output = Floyd_Warshall(input_matrix)
    print(f"{'*' * 8} Floyd_Warshall Output {'*' * 8}")
    print(floyd_warshall_output)


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        print("""
You can give the path_name to the csv file in as follow:   
> python main.py [path_name]                             
Running on default path_name = MatriceDesCouts.csv \n""")
        main()
