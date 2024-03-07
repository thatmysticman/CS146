# Lab 2

## Problem
Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

## High-Level Approaches
### Python Approach
1. The 'isValidBST' method takes the root of a binary tree as input and calls the 'isValidBSTHelper' method with the initial minimum and maximum values set to negative infinity and positive infinity, respectively.
2. The 'isValidBSTHelper' method is a recursive helper function that checks if the binary tree rooted at the given node is a valid BST within the specified range (min_val, max_val).
3. If the current node is null, the function returns True, as an empty subtree is considered a valid BST.
4. If the value of the current node is outside the range (min_val, max_val), the function returns False, indicating that the current subtree is not a valid BST.
5. Recursively call the 'isValidBSTHelper' function for the left and right subtrees with updated min_val and max_val parameters based on the current node's value.
6. The final result is the logical AND of the validity of both left and right subtrees.

### Java Approach
1. The 'isValidBST' method in Java takes the root of a binary tree as input and calls the 'isValidBSTHelper' method with the initial minimum and maximum values set to Long.MIN_VALUE and Long.MAX_VALUE, respectively.
2. The 'isValidBSTHelper' method is a recursive helper function that checks if the binary tree rooted at the given node is a valid BST within the specified range (min, max).
3. If the current node is null, the function returns True, as an empty subtree is considered a valid BST.
4. If the value of the current node is outside the range (min, max), the function returns False, indicating that the current subtree is not a valid BST.
5. Recursively call the 'isValidBSTHelper' function for the left and right subtrees with updated min and max parameters based on the current node's value.
6. The final result is the logical AND of the validity of both left and right subtrees.
