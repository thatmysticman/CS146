import java.util.Arrays;

public class AnagramChecker {

    public static boolean isAnagram(String s, String t) {
        // Check if the lengths are different
        if (s.length() != t.length()) {
            return false;
        }//if-length

        // Convert strings to character arrays and sort them
        char[] charArrayS = s.toCharArray();
        char[] charArrayT = t.toCharArray();
        Arrays.sort(charArrayS);
        Arrays.sort(charArrayT);

        // Compare the sorted arrays
        return Arrays.equals(charArrayS, charArrayT);
    }//isAnagram
  
}//AnagramChecker
