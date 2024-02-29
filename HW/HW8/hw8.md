# HW 8

## Problem
Given a string `s` which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome here.

### Constraints:

- `1 <= s.length <= 2000`
- `s` consists of lowercase **and/or** uppercase English letters only.   

## High-Level Approaches

### Python Approach

1. Check if the length of the input string s is between 1 and 2000 characters. If not, raise a `ValueError` with an appropriate message.
2. Check if all characters in the string are alphabetic using the `isalpha()` method. If not, raise a `ValueError` indicating that the string should only contain lowercase and/or uppercase English letters.
3. Create an array `char_count` of size 128, assuming ASCII characters, to store the count of each character.
4. Iterate through each character in the input string s and increment the corresponding count in the `char_count` array.
5. Initialize variables `length` and `odd_count` to keep track of the length of the palindrome and whether an odd count is encountered.
6. Iterate through the counts in the `char_count` array.
7. For each count, add the floor division by 2 multiplied by 2 to the `length`. This ensures that even counts contribute to the palindrome length.
8. If a count is odd, set `odd_count` to `True`.
9. Return `length + 1` if odd_count is `True`, indicating that there is at least one character with an odd count, and it can be placed in the middle of the palindrome.

### Java Approach

1. Check if the length of the input string s is between 1 and 2000 characters. If not, throw an `IllegalArgumentException` with an appropriate message.
2. Check if the string contains only lowercase and/or uppercase English letters using the `matches` method with a regular expression. If not, throw an `IllegalArgumentException` with a relevant message.
3. Create an array `charCount` of size 128, assuming ASCII characters, to store the count of each character.
4. Iterate through each character in the input string `s` and increment the corresponding count in the `charCount` array.
5. Initialize variables `palindromeLength` and `oddCountFound` to keep track of the length of the palindrome and whether an odd count is encountered.
6. Iterate through the counts in the `charCount` array.
7. For each count, add the floor division by 2 multiplied by 2 to the `palindromeLength`. This ensures that even counts contribute to the palindrome length.
8. If a count is odd, set `oddCountFound` to `true`.
9. Return `palindromeLength + 1` if `oddCountFound` is `true`, indicating that there is at least one character with an odd count, and it can be placed in the middle of the palindrome.
