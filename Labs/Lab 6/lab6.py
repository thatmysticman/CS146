def canFinish(numCourses, prerequisites):
    # Construct the graph
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    # Function to perform DFS traversal
    def dfs(course, visited):
        if visited[course] == -1:
            return False  # Cycle detected
        if visited[course] == 1:
            return True   # Already visited and processed
        
        visited[course] = -1  # Mark as visiting
        
        # Visit all neighbors (prerequisites) of the current course
        for neighbor in graph[course]:
            if not dfs(neighbor, visited):
                return False
        
        visited[course] = 1  # Mark as visited and processed
        return True
    
    # Initialize visited array
    visited = [0] * numCourses
    
    # Perform DFS for each course
    for course in range(numCourses):
        if not dfs(course, visited):
            return False  # Cycle detected
    
    return True
