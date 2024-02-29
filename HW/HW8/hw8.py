    def longestPalindrome(self, s):
        if not 1 <= len(s) <= 2000:
            raise ValueError("Input string length must be between 1 and 2000 characters.")
            
        if not all(c.isalpha() for c in s):
            raise ValueError("Input string must only contain lowercase and/or uppercase English letters.")
            
        char_count = [0] * 128

        for c in s:
            char_count[ord(c)] += 1

        length = 0
        odd_count = False

        for count in char_count:
            length += count // 2 * 2
            if count % 2 == 1:
                odd_count = True

        return length + 1 if odd_count else length
