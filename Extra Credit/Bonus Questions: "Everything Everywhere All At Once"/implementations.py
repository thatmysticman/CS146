class ExtraCredit:
    @staticmethod
    def adjacency_list_to_matrix(adj_list):
        n = len(adj_list)
        # Create an n x n matrix initialized with 0s
        adj_matrix = [[0] * n for _ in range(n)]
        
        for i, neighbors in enumerate(adj_list):
            for neighbor in neighbors:
                adj_matrix[i][neighbor] = 1
        
        return adj_matrix

    @staticmethod
    def adjacency_matrix_to_list(adj_matrix):
        adj_list = []
        for i in range(len(adj_matrix)):
            # Find all indices of columns with a 1 (edge) in row i
            neighbors = [j for j in range(len(adj_matrix[i])) if adj_matrix[i][j] == 1]
            adj_list.append(neighbors)
        
        return adj_list

    @staticmethod
    def reverse_graph(adj_list):
        n = len(adj_list)
        reversed_list = [[] for _ in range(n)]
        
        for i, neighbors in enumerate(adj_list):
            for neighbor in neighbors:
                reversed_list[neighbor].append(i)
        
        return reversed_list

# Example usage:
# adj_list = [[1, 2], [0, 2], [0, 1]]
# adj_matrix = ExtraCredit.adjacency_list_to_matrix(adj_list)
# reversed_list = ExtraCredit.reverse_graph(adj_list)
