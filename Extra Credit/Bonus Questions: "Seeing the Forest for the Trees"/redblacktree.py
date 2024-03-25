class Node:
    def __init__(self, key, color='RED'):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color='BLACK')
        self.root = self.NIL

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.left = self.NIL
        node.right = self.NIL
        node.color = 'RED'

        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        if node.parent is None:
            node.color = 'BLACK'
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def fix_insert(self, node):
        while node.parent.color == 'RED':
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.left_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right

                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.right_rotate(node.parent.parent)

            if node == self.root:
                break

        self.root.color = 'BLACK'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def delete(self, key):
        self.delete_node_helper(self.root, key)

    def delete_node_helper(self, root, key):
        z = self.NIL
        while root != self.NIL:
            if root.key == key:
                z = root

            if root.key <= key:
                root = root.right
            else:
                root = root.left

        if z == self.NIL:
            print("Couldn't find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 'BLACK':
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == 'BLACK':
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.left_rotate(x.parent)
                    sibling = x.parent.right

                if sibling.left.color == 'BLACK' and sibling.right.color == 'BLACK':
                    sibling.color = 'RED'
                    x = x.parent
                else:
                    if sibling.right.color == 'BLACK':
                        sibling.left.color = 'BLACK'
                        sibling.color = 'RED'
                        self.right_rotate(sibling)
                        sibling = x.parent.right

                    sibling.color = x.parent.color
                    x.parent.color = 'BLACK'
                    sibling.right.color = 'BLACK'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.right_rotate(x.parent)
                    sibling = x.parent.left

                if sibling.right.color == 'BLACK' and sibling.left.color == 'BLACK':
                    sibling.color = 'RED'
                    x = x.parent
                else:
                    if sibling.left.color == 'BLACK':
                        sibling.right.color = 'BLACK'
                        sibling.color = 'RED'
                        self.left_rotate(sibling)
                        sibling = x.parent.left

                    sibling.color = x.parent.color
                    x.parent.color = 'BLACK'
                    sibling.left.color = 'BLACK'
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = 'BLACK'

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def inorder_traversal(self, node):
        if node != self.NIL:
            self.inorder_traversal(node.left)
            print(node.key, end=' ')
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node != self.NIL:
            print(node.key, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self):
        self.postorder_traversal_helper(self.root)

    def postorder_traversal_helper(self, node):
        if node != self.NIL:
            self.postorder_traversal_helper(node.left)
            self.postorder_traversal_helper(node.right)
            print(node.key, end=' ')

    def inorder_traversal(self):
        self.inorder_traversal_helper(self.root)

    def inorder_traversal_helper(self, node):
        if node != self.NIL:
            self.inorder_traversal_helper(node.left)
            print(node.key, end=' ')
            self.inorder_traversal_helper(node.right)

    def preorder_traversal(self):
        self.preorder_traversal_helper(self.root)

    def preorder_traversal_helper(self, node):
        if node != self.NIL:
            print(node.key, end=' ')
            self.preorder_traversal_helper(node.left)
            self.preorder_traversal_helper(node.right)


# Demonstration
if __name__ == "__main__":
    tree = RedBlackTree()

    print("Inserting values:")
    values = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13]
    for value in values:
        tree.insert(value)
        print(f"Inserted {value}. Inorder traversal:", end=' ')
        tree.inorder_traversal()
        print()

    print("\nInorder traversal of the tree:")
    tree.inorder_traversal()
    print("\nPreorder traversal of the tree:")
    tree.preorder_traversal()
    print("\nPostorder traversal of the tree:")
    tree.postorder_traversal()

    print("\nDeleting value 18:")
    tree.delete(18)
    print("Inorder traversal after deletion:", end=' ')
    tree.inorder_traversal()

    print("\nDeleting value 11:")
    tree.delete(11)
    print("Inorder traversal after deletion:", end=' ')
    tree.inorder_traversal()

    print("\nDeleting value 3:")
    tree.delete(3)
    print("Inorder traversal after deletion:", end=' ')
    tree.inorder_traversal()
