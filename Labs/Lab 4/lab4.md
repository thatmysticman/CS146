# Lab 4

## Problem
Given the `root` of a binary tree, invert the tree, and return its root.

## High-Level Approaches
### Python Approach
1. Define a function `reverseTree` that takes the root of a binary tree as input.
2. Check if the root is `None`. If so, return.
3. Swap the left and right children of the current root node.
4. Recursively call `reverseTree` on the left and right subtrees.
5. Define a function invertTree that takes the root of a binary tree as input.
6. Call `reverseTree` on the root.
7. Return the modified root.

### Java Approach
1. Define a method `reverseTree` that takes the root of a binary tree node as input and reverses the tree recursively.
2. Check if the root is `null`. If so, return.
3. Swap the left and right children of the current root node.
4. Recursively call `reverseTree` on the left and right subtrees.
5. Define a method `invertTree` that takes the root of a binary tree node as input and returns the inverted tree.
6. Call `reverseTree` on the root.
7. Return the modified root.
