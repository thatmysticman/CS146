    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] prerequisite : prerequisites) {
            int course = prerequisite[0];
            int prereq = prerequisite[1];
            graph.putIfAbsent(course, new ArrayList<>());
            graph.get(course).add(prereq);
        }

        int[] visited = new int[numCourses];

        for (int course = 0; course < numCourses; course++) {
            if (!dfs(course, visited, graph))
                return false;
        }

        return true;
    }

    private boolean dfs(int course, int[] visited, Map<Integer, List<Integer>> graph) {
        if (visited[course] == -1)
            return false;
        if (visited[course] == 1)
            return true;

        visited[course] = -1;

        if (graph.containsKey(course)) {
            for (int neighbor : graph.get(course)) {
                if (!dfs(neighbor, visited, graph))
                    return false;
            }
        }

        visited[course] = 1;
        return true;
    }
