#This approach uses nested loops to fix two elements (nums[i] and nums[j]) and then calculates the third element (complement) required for a zero sum. 
If the complement is found in the remaining part of the array, a triplet is added to the set to avoid duplicates.



def find_triplets_with_zero_sum(nums):
    triplets = set()

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            complement = -(nums[i] + nums[j])
            if complement in nums[j + 1:]:
                triplet = tuple(sorted([nums[i], nums[j], complement]))
                triplets.add(triplet)

    return list(triplets)

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
result = find_triplets_with_zero_sum(nums)

print("Triplets with zero sum:", result)
