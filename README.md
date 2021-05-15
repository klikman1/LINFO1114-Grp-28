# LINFO1114-Grp-28
Hello,
In this Github, You will find our project of Maths Discrète.

# Main Purpose

The goal of this project was to calculate the shortest path between each pair of nodes.
For this we had to use 3 known algorithms (Bellman-Ford, Floyd-Warshall and Dijkstra) which we had to, firstly, implement and use to find the distance. You can find more details in `Enonce.pdf`

# Structure of our Folder.

```
| Bellman_Ford.py : 
| ConseilsRapport.pdf
| CreateCsvFile.py
| Dijkstra_algorithm.py
| Enonce.pdf
| Floyd_Warshall.py
| Graphe28.png
| Main.py
| MatriceDesCouts.csv
| Rapport.pdf
| ReadME.md
```
The `Graphe28.png` is our reference graph. 

We create the cost matrix (in french: la matrice des coûts) of our graph in csv (comma-separated values) format in `CreateCsvFile.py`.

`MatriceDesCouts.csv` is our cost matrix in csv format.

In `Bellman_ford.py`, we implemented the Bellman-ford algorithm.

In `Floyd_Warshall.py`, we implemented the Floyd-Warshall algorithm.

And in `Dijkstra_algorithm.py` is where the Dijkstra algorithm is implemented.

`Main.py` is our main file. It is where we import all files and execute our codes.

# Requirements
To execute our code without problems of modules, make sure you have installed: 
* Python 3
* Numpy 

# Execution 
To execute our code you can run in terminal like follow:
> python main.py [path_name_to_csv]
