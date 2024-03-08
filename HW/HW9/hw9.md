# HW 9

## Problem
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

The lowest common ancestor is defined between two nodes p and q as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).

### Constraints:

- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All values are unique.
- p != q
- p and q will exist in the BST.

## High-Level Approaches

### Python Approach

1. Check if the given root is `None`. If so, return `None` as there is no common ancestor in an empty tree.
2. Verify if the values of nodes `p` and `q` fall within the specified range [-10^9, 10^9]. If not, raise a `ValueError` with the message "Node value out of bounds."
3. Ensure that nodes `p` and `q` are distinct. If they have the same value, raise a `ValueError` with the message "p and q should be distinct nodes."
4. If both `p` and `q` values are less than the current root value, make a recursive call to the left subtree using `self.lowestCommonAncestor(root.left, p, q)`.
5. If both `p` and `q` values are greater than the current root value, make a recursive call to the right subtree using `self.lowestCommonAncestor(root.right, p, q)`.
6. If the values of `p` and `q` are on opposite sides of the current root, then the current root is the lowest common ancestor. Return the current root.

### Java Approach

1. Check if the given root is `null`. If so, return `null` as there is no common ancestor in an empty tree.
2. Verify if the values of nodes `p` and `q` fall within the specified range [-10^9, 10^9]. If not, throw an `IllegalArgumentException` with the message "Node value out of bounds."
3. Ensure that nodes p and q are distinct. If they have the same value, throw an `IllegalArgumentException` with the message "p and q should be distinct nodes."
4. If both `p` and `q` values are less than the current root value, make a recursive call to the left subtree using `lowestCommonAncestor(root.left, p, q)`.
5. If both `p` and `q` values are greater than the current root value, make a recursive call to the right subtree using `lowestCommonAncestor(root.right, p, q)`.
6. If the values of `p` and `q` are on opposite sides of the current root, then the current root is the lowest common ancestor. Return the current root.
