def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    def dfs(course, visited):
        if visited[course] == -1:
            return False 
        if visited[course] == 1:
            return True   
        
        visited[course] = -1  
        
        for neighbor in graph[course]:
            if not dfs(neighbor, visited):
                return False
        
        visited[course] = 1
        return True
    
    visited = [0] * numCourses
    
    for course in range(numCourses):
        if not dfs(course, visited):
            return False
    
    return True
