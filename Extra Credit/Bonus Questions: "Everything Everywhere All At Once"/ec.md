### Conversion from Adjacency List to Adjacency Matrix:
- Explanation:
To convert an adjacency list to an adjacency matrix, we iterate through each vertex in the graph and check its adjacent vertices. For each adjacent vertex, we mark the corresponding entry in the adjacency matrix as 1 if there's an edge between the vertices, and 0 otherwise.
- Pseudocode:
function adjacencyListToMatrix(adjList):
    n = length(adjList)  // Number of vertices in the graph
    matrix = initializeMatrix(n, n)  // Initialize an n x n matrix with all zeros
    
    for i from 0 to n-1:
        for each vertex v in adjList[i]:
            matrix[i][v] = 1  // Mark the entry as 1 to represent the existence of an edge
    
    return matrix

### Conversion from Adjacency Matrix to Adjacency List:
- Explanation:
To convert an adjacency matrix to an adjacency list, we iterate through each row of the matrix. For each vertex, we traverse its corresponding row in the matrix and add the indices of vertices where the entry is 1 to its adjacency list.
- Pseudocode:
function adjacencyMatrixToList(matrix):
    n = number of rows in matrix
    adjList = initialize an empty list of lists
    
    for i from 0 to n-1:
        neighbors = []
        for j from 0 to n-1:
            if matrix[i][j] == 1:
                neighbors.append(j)
        adjList.append(neighbors)
    
    return adjList

### Reversing the Direction of Edges in a Directed Graph:
- Explanation:
To reverse the direction of each edge in a directed graph, we simply swap the source and destination vertices for each edge.
- Pseudocode:
function reverseDirectedGraph(graph):
    reversedGraph = initialize an empty graph
    
    for each edge (u, v) in graph:
        reversedGraph.addEdge(v, u)  // Reverse the direction of the edge
    
    return reversedGraph
