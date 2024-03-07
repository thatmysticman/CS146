public void reverseTree(TreeNode root) {
    if (root == null) {
        return;
    }

    TreeNode temp = root.right;
    root.right = root.left;
    root.left = temp;

    reverseTree(root.left);
    reverseTree(root.right);
}

public TreeNode invertTree(TreeNode root) {
    reverseTree(root);
    return root;
}
