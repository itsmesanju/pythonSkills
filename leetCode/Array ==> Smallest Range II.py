class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        """
        The smallestRangeII method aims to find the smallest possible difference between the maximum and 
        minimum values in the given nums array by adding or subtracting a constant k to each element.

        The approach leverages the fact that, to minimize the range, we want to add k to the smaller elements 
        and subtract k from the larger elements, aiming to bring the overall range as close as possible.

        This solution has a time complexity of O(N * log(N)), where N is the length of the nums array, mainly due to the sorting step.
        """
        nums.sort()

        ans = nums[-1] - nums[0]

        for i in range(len(nums) - 1):
            max_val = max(nums[i] + k, nums[-1] - k)
            min_val = min(nums[0] + k, nums[i + 1] - k)
            ans = min(ans, max_val - min_val)
        return ans
