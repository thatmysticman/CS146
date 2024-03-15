def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return None
    
    result = []
    queue = deque([root])
    
    nodeCount = 1
    
    while queue:
        level_size = len(queue)
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.popleft()

            if node.val < -1000 or node.val > 1000:
                raise ValueError("TreeNode value is out of range [-1000, 1000]")
            
            level_nodes.append(node.val)
            
            if node.left:
                queue.append(node.left)
                nodeCount += 1
                
            if node.right:
                queue.append(node.right)
                nodeCount += 1
                
        result.append(level_nodes)
        
        if nodeCount > 2000:
            raise ValueError("Number of nodes exceeds the limit of 2000")
    
    return result
