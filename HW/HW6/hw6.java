public List<List<Integer>> threeSum(int[] nums) {
    // Check for valid array length (3 <= nums.length <= 3000)
    if (nums.length < 3) {
        return new ArrayList<>(); // Handle edge case of too few elements
    }

    Arrays.sort(nums); // Sort the array to enable Two Pointers
    List<List<Integer>> triplets = new ArrayList<>();

    for (int i = 0; i < nums.length - 2; i++) {
        // Skip duplicates for the first element to avoid duplicate triplets
        if (i > 0 && nums.length <= 3000 && nums[i] == nums[i - 1]) {
            continue;
        }

        int left = i + 1, right = nums.length - 1;

        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];

            if (sum == 0) {
                if (nums[i] == nums[left] && nums[left] == nums[right]) {
                  // Skip triplets with all identical elements
                  left++;
                  right--;
                } 
                else {
                triplets.add(Arrays.asList(nums[i], nums[left], nums[right]));

                // Skip duplicates for left and right pointers
                while (left < right && nums[left] == nums[left + 1]) {
                    left++;
                }
                while (left < right && nums[right] == nums[right - 1]) {
                    right--;
                }

                left++;
                right--;
                }
            }
            else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }

    return triplets; // No specific order guaranteed for the output or triplets
}
