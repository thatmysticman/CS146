# Fibonacci Number Computation

## Problem:

A Fibonacci number is a sequence of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The task is to write a function to compute the nth Fibonacci number with an optimized solution having a time complexity of O(n).

## High-Level Approaches:

### Python Approach:

1. Check if the input `n` is 0 or 1, and if so, return `n` as it is the base case.
2. Create a list `fib` to store the Fibonacci numbers, initialized with zeros.
3. Set the first two elements of `fib` to 0 and 1.
4. Use a loop to iterate from 2 to `n`, updating each element in `fib` as the sum of the two preceding elements.
5. Return the `n`th element of `fib` as the result.

### Java Approach:

1. Check if the input `n` is 0 or 1, and if so, return `n` as it is the base case.
2. Create an array `fib` to store the Fibonacci numbers, initialized with zeros.
3. Set the first two elements of `fib` to 0 and 1.
4. Use a loop to iterate from 2 to `n`, updating each element in `fib` as the sum of the two preceding elements.
5. Return the `n`th element of `fib` as the result.
