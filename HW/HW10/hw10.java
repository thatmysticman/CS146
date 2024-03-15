public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) {
        return null;
    }
    
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    
    int nodeCount = 1;
    
    while (!queue.isEmpty()) {
        int levelSize = queue.size();
        List<Integer> levelNodes = new ArrayList<>();
        
        for (int i = 0; i < levelSize; i++) {
            TreeNode node = queue.poll();
            
            if (node.val < -1000 || node.val > 1000)
                throw new IllegalArgumentException("TreeNode value is out of range [-1000, 1000]");
           
            levelNodes.add(node.val);
            
            if (node.left != null)
                queue.offer(node.left);
                nodeCount++;
            
            if (node.right != null)
                queue.offer(node.right);
                nodeCount++;
        }
        
        result.add(levelNodes);
        
         if (nodeCount > 2000)
            throw new IllegalArgumentException("Number of nodes exceeds the limit of 2000");
    }
    
    return result;
}
