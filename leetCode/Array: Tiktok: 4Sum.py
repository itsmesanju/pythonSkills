class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Sort the input list of numbers to ensure that identical elements are grouped together.
        Iterate through the list with two outer loops, considering each pair of numbers as potential candidates for the first two elements of the quadruplet.
        Within these loops, use two pointer technique (left and right pointers) to find the remaining two numbers that sum up to the target.
        Handle duplicates by skipping over identical elements when iterating through the list.
        If a quadruplet with the target sum is found, add it to the result list.
        Continue until all combinations have been checked.
        Return the list of quadruplets that sum up to the target.
        """
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return result
