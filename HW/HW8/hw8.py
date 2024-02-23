class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = [0] * 128  # Assuming ASCII characters
        
        for c in s:
            char_count[ord(c)] += 1
        
        palindrome_length = 0
        odd_count_found = False
        
        for count in char_count:
            palindrome_length += (count // 2) * 2
            
            if count % 2 == 1:
                odd_count_found = True
        
        return palindrome_length + (1 if odd_count_found else 0)

# Test cases
solution = Solution()
print(solution.longestPalindrome("abccccdd"))  # Output: 7
print(solution.longestPalindrome("speediskey"))  # Output: 5
