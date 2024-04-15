public int findTheCity(int n, int[][] edges, int distanceThreshold) {
    // Initialize the distance matrix with max value and 0 for diagonal elements
    int[][] distance = new int[n][n];
    for (int i = 0; i < n; i++) {
        Arrays.fill(distance[i], Integer.MAX_VALUE);
        distance[i][i] = 0;
    }

    // Populate the distance matrix with edge weights
    for (int[] edge : edges) {
        int from = edge[0];
        int to = edge[1];
        int weight = edge[2];
        distance[from][to] = weight;
        distance[to][from] = weight;
    }

    // Floyd-Warshall algorithm to find the shortest paths between all pairs of cities
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (distance[i][k] != Integer.MAX_VALUE && distance[k][j] != Integer.MAX_VALUE) {
                    distance[i][j] = Math.min(distance[i][j], distance[i][k] + distance[k][j]);
                }
            }
        }
    }

    int minCity = -1;
    int minReachable = n;
    
    // Iterate through all the cities and count reachable cities
    for (int i = 0; i < n; i++) {
        int reachable = 0;
        for (int j = 0; j < n; j++) {
            if (i != j && distance[i][j] <= distanceThreshold) {
                reachable++;
            }
        }
        if (reachable <= minReachable) {
            minReachable = reachable;
            minCity = i;
        }
    }
    
    return minCity;
}
