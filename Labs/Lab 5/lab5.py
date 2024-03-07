def isValidBST(self, root):
    return self.isValidBSTHelper(root, float('-inf'), float('inf'))

def isValidBSTHelper(self, node, min_val, max_val):
    if not node:
        return True
    
    if node.val <= min_val or node.val >= max_val:
        return False
    
    return (self.isValidBSTHelper(node.left, min_val, node.val) and
            self.isValidBSTHelper(node.right, node.val, max_val))
