class Solution:
    def longestPalindrome(self, s):
        char_count = [0] * 128  # Assuming ASCII character set

        for c in s:
            char_count[ord(c)] += 1

        length = 0
        odd_count = False

        for count in char_count:
            length += count // 2 * 2  # Add even occurrences
            if count % 2 == 1:
                odd_count = True  # Mark if there is an odd occurrence

        return length + 1 if odd_count else length  # Add one character with odd occurrence if exists

# Test cases
solution = Solution()
print(solution.longestPalindrome("abccccdd"))  # Output: 7
print(solution.longestPalindrome("speediskey"))  # Output: 5
print(solution.longestPalindrome("zakikazan"))  # Output: 7
print(solution.longestPalindrome("indeed"))  # Output: 5
print(solution.longestPalindrome("Aa"))  # Output: 1
print(solution.longestPalindrome("toinksFfdssksdf"))  # Output: 11
