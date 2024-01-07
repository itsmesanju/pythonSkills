class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums), -1, -1): #First loop to traverse in backward direction to fill the DP array
            for j in range(i, len(nums)): #2nd loop is to compare the numbers in forward diretion to check
                if nums[i] < nums[j]: #check if numbers are in increasing order
                    dp[i] = max(dp[i], dp[j]+1) #if increasing, update the dparray.
        
        return max(dp)
