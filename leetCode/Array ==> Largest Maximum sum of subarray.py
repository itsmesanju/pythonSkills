class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        This is a divide and conquer approach

        initialize max sum to the first element in the arrays #nums[0]
        Iterate through the array and update current_sum at each step. 
        If adding the current number decreases the current sum, start a new subarray from the current number.

        Update max_sum whenever a new maximum sum is found during the iteration.
        At the end of the iteration, max_sum holds the maximum subarray sum.
        """

        max_sum = nums[0]  # Initialize max_sum to first element... or may be set to infinity
        current_sum = 0  # Initialize current_sum to 0

        for num in nums:
            # If adding the current number decreases the current sum, start a new subarray
            current_sum = max(num, current_sum + num)

            # Update the maximum sum if the current sum becomes greater
            max_sum = max(max_sum, current_sum)

        return max_sum
