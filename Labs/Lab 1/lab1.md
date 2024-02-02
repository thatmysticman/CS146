# Two Sum Problem

## Problem Statement
Given an array of integers `nums` and an integer `target`, the task is to find and return the indices of two numbers in the array such that they add up to the target. Each input has exactly one solution, and the same element cannot be used twice. The solution can be returned in any order.

## Approach
We have used a simple brute-force approach with nested loops to solve the Two Sum problem without using a hashmap or dictionary.

### Java Implementation
1. We use a nested loop to iterate through each pair of elements in the array.
2. For each pair, we check if the sum of the two elements equals the target.
3. If a matching pair is found, we store their indices in the result array and return it.
4. If no solution is found, we return an empty array.

### Python Implementation
1. Similar to the Java approach, we use a nested loop to iterate through each pair of elements in the array.
2. For each pair, we check if the sum of the two elements equals the target.
3. If a matching pair is found, we store their indices in the result list and return it.
4. If no solution is found, we return an empty list.
