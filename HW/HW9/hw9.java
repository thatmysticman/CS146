public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    if (root == null) {
        return null;
    }
    
    int rootVal = root.val;
    int pVal = p.val;
    int qVal = q.val;
    
    if (pVal < -1000000000 || pVal > 1000000000 || qVal < -1000000000 || qVal > 1000000000) {
        throw new IllegalArgumentException("Node value out of bounds");
    }
    
    if (pVal == qVal) {
        throw new IllegalArgumentException("p and q should be distinct nodes");
    }
    
    if (pVal < rootVal && qVal < rootVal) {
        return lowestCommonAncestor(root.left, p, q);
    } else if (pVal > rootVal && qVal > rootVal) {
        return lowestCommonAncestor(root.right, p, q);
    } else {
        return root;
    }
}
