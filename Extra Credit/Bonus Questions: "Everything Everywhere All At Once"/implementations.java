public class ExtraCredit {
    
    public static int[][] adjacencyListToMatrix(List<List<Integer>> adjList) {
        int n = adjList.size();
        int[][] adjMatrix = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            for (int neighbor : adjList.get(i)) {
                adjMatrix[i][neighbor] = 1;
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
        int n = adjList.size();
        List<List<Integer>> reversedList = new ArrayList<>(Collections.nCopies(n, new ArrayList<>()));

        for (int i = 0; i < n; i++) {
            for (int neighbor : adjList.get(i)) {
                reversedList.get(neighbor).add(i);
            }
        }
        
        return reversedList;
    }
    
}

