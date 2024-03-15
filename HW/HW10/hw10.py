def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return None
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
        
        result.append(level_nodes)
    
    return result
