public class ExtraCredit {
    
    public static int[][] adjacencyListToMatrix(List<List<Integer>> adjList) {
        int n = adjList.size(); // Number of vertices
        int[][] adjMatrix = new int[n][n]; // Initialize n x n matrix with 0s
        
        for (int i = 0; i < n; i++) {
            for (int neighbor : adjList.get(i)) {
                adjMatrix[i][neighbor] = 1; // Set to 1 where there's an edge
            }
        }
        
        return adjMatrix;
    }

    public static List<List<Integer>> adjacencyMatrixToList(int[][] adjMatrix) {
        List<List<Integer>> adjList = new ArrayList<>();
        int n = adjMatrix.length;
        
        for (int i = 0; i < n; i++) {
            List<Integer> neighbors = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                if (adjMatrix[i][j] == 1) {
                    neighbors.add(j);
                }
            }
            adjList.add(neighbors);
        }
        
        return adjList;
    }

    public static List<List<Integer>> reverseGraph(List<List<Integer>> adjList) {
        int n = adjList.size(); // Number of vertices
        List<List<Integer>> reversedList = new ArrayList<>(Collections.nCopies(n, new ArrayList<>()));

        for (int i = 0; i < n; i++) {
            for (int neighbor : adjList.get(i)) {
                reversedList.get(neighbor).add(i); // Add i to the adjacency list of its neighbor
            }
        }
        
        return reversedList;
    }
    
}

