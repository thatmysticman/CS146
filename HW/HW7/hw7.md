# HW 7

## Problem
Given an array of time intervals `intervals` where `intervals[i] = [start_i, end_i]`, representing the start and end time for a particular job that needs to be executed, return the minimum number of servers required to run all jobs.

### Constraints:

- 1 <= intervals.length <= 10^4
- 0 <= start_i < end_i <= 10^6    

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
