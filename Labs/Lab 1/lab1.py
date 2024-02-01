def two_sum(nums, target):
    result = [0, 0]

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result[0] = i
                result[1] = j
                return result

    # If no solution is found, return an empty list
    return []
