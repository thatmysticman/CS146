public int longestPalindrome(String s) {
        if (s.length() < 1 || s.length() > 2000) {
        throw new IllegalArgumentException("Input string length must be between 1 and 2000 characters.");
    }
        int[] charCount = new int[128]; // Assuming ASCII characters
        
        for (char c : s.toCharArray()) {
            charCount[c]++;
        }
        
        int palindromeLength = 0;
        boolean oddCountFound = false;
        
        for (int count : charCount) {
            palindromeLength += (count / 2) * 2;
            
            if (count % 2 == 1) {
                oddCountFound = true;
            }
        }
        
        return palindromeLength + (oddCountFound ? 1 : 0);
    }
