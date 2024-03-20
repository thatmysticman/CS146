## Conversion from Adjacency List to Adjacency Matrix:
### Explanation:
To convert an adjacency list to an adjacency matrix, we iterate through each vertex in the graph and check its adjacent vertices. For each adjacent vertex, we mark the corresponding entry in the adjacency matrix as 1 if there's an edge between the vertices, and 0 otherwise.
### Pseudocode:
`Function adjacencyListToMatrix(adjList)`    
`    n = Length(adjList)`   
`    Initialize matrix[n][n] with all values as 0`    

    For i = 0 to n-1
        For each vertex v in adjList[i]
            matrix[i][v] = 1
        EndFor
    EndFor

    Return matrix
`EndFunction`


## Conversion from Adjacency Matrix to Adjacency List:
### Explanation:
To convert an adjacency matrix to an adjacency list, we iterate through each row of the matrix. For each vertex, we traverse its corresponding row in the matrix and add the indices of vertices where the entry is 1 to its adjacency list.
### Pseudocode:
`Function adjacencyMatrixToList(matrix)`
`    n = Length(matrix) // Assuming square matrix`
`    Initialize adjList[n] with empty lists`

    For i = 0 to n-1
        For j = 0 to n-1
            If matrix[i][j] == 1
                Append j to adjList[i]
            EndIf
        EndFor
    EndFor

    Return adjList
`EndFunction`


## Reversing the Direction of Edges in a Directed Graph:
### Explanation:
To reverse the direction of each edge in a directed graph, we swap the source and destination vertices for each edge.
### Pseudocode:
`Function reverseDirectedGraph(originalGraph)`
`    // Initialize reversedGraph with the same number of vertices as originalGraph`
`    // but with empty lists for adjacency representation`
    n = NumberOfVertices(originalGraph)
    Initialize reversedGraph[n]

    For each vertex v in originalGraph
        For each neighbor u of vertex v
            Add v to the adjacency list of u in reversedGraph
        EndFor
    EndFor

    Return reversedGraph
`EndFunction`
