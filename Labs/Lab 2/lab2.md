# Anagram Checking

## Problem
Given two strings `s` and `t`, determine if `t` is an anagram of `s`.

## High-Level Approaches
### Python Solution
1. Check if lengths of `s` and `t` are different; if so, they can't be anagrams, return `False`.
2. Sort characters in both strings using `sorted()`.
3. Compare sorted strings; return `True` if equal, otherwise return `False`.

### Java Solution
1. Check if lengths of `s` and `t` are different; if so, they can't be anagrams, return `false`.
2. Convert strings to character arrays, sort using `Arrays.sort()`.
3. Compare sorted arrays using `Arrays.equals()`, return `true` if equal, otherwise return `false`.
