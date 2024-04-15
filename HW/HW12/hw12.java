import java.util.*;

public class Main {
    public static void main(String[] args) {
        int n = 2;
        int[] wells = {1, 1};
        int[][] pipes = {{1, 2, 1}, {1, 2, 2}};
        System.out.println(minCostToSupplyWater(n, wells, pipes));  // Output: 2
    }

    public static int minCostToSupplyWater(int n, int[] wells, int[][] pipes) {
        List<int[]> edges = new ArrayList<>();

        // Add edges from wells
        for (int i = 0; i < n; i++) {
            edges.add(new int[]{wells[i], 0, i + 1});
        }

        // Add edges from pipes
        for (int[] pipe : pipes) {
            edges.add(new int[]{pipe[2], pipe[0], pipe[1]});
        }

        // Sort edges by their cost
        edges.sort((a, b) -> Integer.compare(a[0], b[0]));

        int[] parent = new int[n + 1];
        int[] rank = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }

        int totalCost = 0;

        for (int[] edge : edges) {
            int cost = edge[0];
            int house1 = edge[1];
            int house2 = edge[2];

            int xRoot = find(parent, house1);
            int yRoot = find(parent, house2);

            if (xRoot != yRoot) {
                union(parent, rank, xRoot, yRoot);
                totalCost += cost;
            }
        }

        return totalCost;
    }

    public static int find(int[] parent, int i) {
        if (parent[i] == i) {
            return i;
        }
        return parent[i] = find(parent, parent[i]);
    }

    public static void union(int[] parent, int[] rank, int x, int y) {
        int xRoot = find(parent, x);
        int yRoot = find(parent, y);

        if (rank[xRoot] < rank[yRoot]) {
            parent[xRoot] = yRoot;
        } else if (rank[xRoot] > rank[yRoot]) {
            parent[yRoot] = xRoot;
        } else {
            parent[yRoot] = xRoot;
            rank[xRoot]++;
        }
    }
}
