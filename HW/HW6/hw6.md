# HW 6

## Problem
Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

### Constraints:

- The solution set **must not** contain duplicate triplets.    
- The order of the output and the order of the triplets does not matter.    
- `3 <= nums.length <= 3000`    
- `-105 <= nums[i] <= 105`     

## High-Level Approaches

### Python Approach

1. Check for a valid array length (3 <= nums.length <= 3000).
2. Sort the input array.
3. Iterate through the array, fixing one element at a time.
4. Use two pointers to find pairs that sum to the negation of the fixed element.
5. Skip duplicates to avoid redundant triplets.
6. Handle edge cases and ensure no duplicate triplets with identical elements.

### Java Approach

1. Check for a valid array length (3 <= nums.length <= 3000).
2. Sort the array.
3. Iterate through the array, fixing one element at a time.
4. Use two pointers to find pairs that sum to the negation of the fixed element.
5. Skip duplicates to avoid redundant triplets.
6. Handle edge cases and ensure no duplicate triplets with identical elements.
