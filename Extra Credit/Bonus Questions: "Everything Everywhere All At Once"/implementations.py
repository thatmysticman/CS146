# Function to convert adjacency list to adjacency matrix
def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)
    matrix = [[0] * n for _ in range(n)]  # Initialize an n x n matrix with all zeros
    
    for i in range(n):
        for v in adj_list[i]:
            matrix[i][v] = 1  # Mark the entry as 1 to represent the existence of an edge
    
    return matrix

# Function to convert adjacency matrix to adjacency list
def adjacency_matrix_to_list(matrix):
    n = len(matrix)
    adj_list = [[] for _ in range(n)]  # Initialize an empty list of lists
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                adj_list[i].append(j)
    
    return adj_list

# Function to reverse the direction of edges in a directed graph
def reverse_directed_graph(graph):
    reversed_graph = [[] for _ in range(len(graph))]  # Initialize an empty graph
    
    for i in range(len(graph)):
        for v in graph[i]:
            reversed_graph[v].append(i)  # Reverse the direction of the edge
    
    return reversed_graph

# Example usage:
adj_list = [[1, 2], [0, 2], [0, 1, 3], [2]]
adj_matrix = adjacency_list_to_matrix(adj_list)
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

reversed_adj_list = adjacency_matrix_to_list(adj_matrix)
print("\nAdjacency List:")
for i, neighbors in enumerate(reversed_adj_list):
    print(f"{i}: {neighbors}")

# Example directed graph
directed_graph = [[1, 2], [2], [0, 3], [0]]
reversed_graph = reverse_directed_graph(directed_graph)
print("\nReversed Directed Graph:")
for i, neighbors in enumerate(reversed_graph):
    print(f"{i}: {neighbors}")
