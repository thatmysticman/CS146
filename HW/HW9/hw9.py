def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
        return None
    
    root_val = root.val
    p_val = p.val
    q_val = q.val
    
    if p_val < -1000000000 or p_val > 1000000000 or q_val < -1000000000 or q_val > 1000000000:
        raise ValueError("Node value out of bounds")
    
    if p_val == q_val:
        raise ValueError("p and q should be distinct nodes")
        
    if p_val < root_val and q_val < root_val:
        return self.lowestCommonAncestor(root.left, p, q)
    elif p_val > root_val and q_val > root_val:
        return self.lowestCommonAncestor(root.right, p, q)
    else:
        return root
