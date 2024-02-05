public class Solution {
    public int firstBadVersion(int n) {
        int left = 1, right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    // This is a placeholder for the isBadVersion method.
    // You should replace it with the actual implementation provided by the API.
    private boolean isBadVersion(int version) {
        // Your implementation here.
        return false;
    }
}

