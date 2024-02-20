def threeSum(self, nums: List[int]) -> List[List[int]]:
    """
    Finds all unique triplets in a given array that sum to 0.

    Args:
        nums: A list of integers.

    Returns:
        A list of lists, where each inner list represents a triplet.

    Raises:
        ValueError: If the length of the input array is less than 3.
    """

    if len(nums) < 3:
        raise ValueError("Array must have at least 3 elements")

    # Ensure elements are within valid range (-10^5 <= nums[i] <= 10^5)
    for num in nums:
        if num < -10**5 or num > 10**5:
            raise ValueError("Element out of range (-10^5, 10^5)")

    nums.sort()  # Sort the array for Two Pointers
    triplets = []

    for i in range(len(nums) - 2):
        # Skip duplicates for the first element to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum == 0:
                if nums[i] == 0 and nums[left] == 0 and nums[right] == 0:
                    break  # Skip this triplet entirely, as it's not unique
                
                triplets.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left and right pointers while maintaining order
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1

return triplets
