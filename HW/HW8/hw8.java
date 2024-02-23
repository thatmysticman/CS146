public class Solution {
    public int longestPalindrome(String s) {
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

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.longestPalindrome("abccccdd")); // Output: 7
        System.out.println(solution.longestPalindrome("speediskey")); // Output: 5
    }
}
