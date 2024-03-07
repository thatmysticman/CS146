def reverseTree(self, root):
        if root is None:
            return

        temp = root.right
        root.right = root.left
        root.left = temp

        self.reverseTree(root.left)
        self.reverseTree(root.right)

    def invertTree(self, root):
        self.reverseTree(root)
        return root
