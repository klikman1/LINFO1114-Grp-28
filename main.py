import numpy as np
import math
from Floyd_Warshall import Floyd_Warshall
from Bellman_Ford import Bellman_Ford
from Dijkstra_algorithm import Dijkstra_algorithm
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



def main(input_csv_file: str = "MatriceDesCouts.csv"):
    """ Executes the program :
          (1) Read the CSV input file,
          (2) Run our 3 functions and
          (3) print the matrix of the csv file with the result returned by all the 3 functions.
    :arg input_csv_file : The pathname to the csv file that contains the weighted matrix.
    :return: None.
    """
    input_matrix = read_csv(input_csv_file)
    #print(f"{'*' * 8} Input Matrix From CSV {'*' * 8}")
    #print(input_matrix)

    #floyd_warshall_output = Floyd_Warshall(input_matrix)
    #print(f"{'*' * 8} Floyd_Warshall Output {'*' * 8}")
    #print(floyd_warshall_output)

    bellman_ford_output = Bellman_Ford(input_matrix)
    print(f"{'*' * 8} Bellman_Ford( Output {'*' * 8}")
    print(bellman_ford_output)

    dijkstra_output = Dijkstra_algorithm(input_matrix)
    print(f"{'*' * 8} Dijkstra Output {'*' * 8}")
    print(dijkstra_output)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        print("""
You can give the path_name to the csv file in as follow:   
> python main.py [path_name]                             
Running on default path_name = MatriceDesCouts.csv \n""")
        main()
