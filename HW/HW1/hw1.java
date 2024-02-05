public class Solution {
    public static boolean isPalindrome(String input) {
        
        // Check if the string is empty
        if (input == "" || input == " ") {
            System.out.println("Invalid Input!");
            return false;
        }
    
        // Convert to lowercase and remove non-alphanumeric characters
        String newInput = input.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
    
        // Check if the cleaned string is a palindrome
        int left = 0;
        int right = newInput.length() - 1;
    
        while (left < right) {
            if (newInput.charAt(left) != newInput.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
