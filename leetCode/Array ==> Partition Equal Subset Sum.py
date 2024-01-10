class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        """
        The algorithm checks if it's possible to split a given list (nums) into two subsets with equal sums. 
        It calculates the total sum and ensures it's even. 
        It then uses a recursive approach with memoization to explore all possible subsets and checks if any
        subset's sum is half of the total sum. The result indicates whether such a subset exists or not.
        """
        s = sum(nums)
        if s % 2 != 0: return False

        @cache
        def sol(idx, target):
            if idx == len(nums): return False
            if nums[idx] == target: return True
            return sol(idx + 1, target) or sol(idx + 1, target - nums[idx])
        
        return sol(0, s // 2)
