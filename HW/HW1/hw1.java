public static boolean isPalindrome(String s) {
    // Check if the string is empty
    if (s == "" || s == " ") {
        System.out.println("Invalid Input!");
        return false;
    }

    // Convert to lowercase and remove non-alphanumeric characters
    String cleanedString = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");

    // Check if the cleaned string is a palindrome
    int left = 0;
    int right = cleanedString.length() - 1;

    while (left < right) {
        if (cleanedString.charAt(left) != cleanedString.charAt(right)) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
