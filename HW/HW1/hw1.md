# HW 1

## Problem
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters INCLUDE letters and numbers. Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## High-Level Approaches

### Python Approach

1. Convert the input string to lowercase.
2. Use a isalnum function to create a new string by including only alphanumeric characters.
3. Use a two-pointer approach to check if the cleaned string is a palindrome.
4. Initialize two pointers, one at the beginning (left) and the other at the end (right) of the cleaned string.
5. Compare characters at the left and right positions and move towards the center until the pointers meet.

### Java Approach

1. Convert the input string to lowercase.
2. Use a replaceAll function to remove all non-alphanumeric characters, leaving only letters and numbers.
3. Use a two-pointer approach to check if the cleaned string is a palindrome.
4. Initialize two pointers, one at the beginning (left) and the other at the end (right) of the cleaned string.
5. Compare characters at the left and right positions and move towards the center until the pointers meet.
