#Dynamic programming N**2
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums), -1, -1): #First loop to traverse in backward direction to fill the DP array
            for j in range(i, len(nums)): #2nd loop is to compare the numbers in forward diretion to check
                if nums[i] < nums[j]: #check if numbers are in increasing order
                    dp[i] = max(dp[i], dp[j]+1) #if increasing, update the dparray.
        
        return max(dp)



#Binary search- Alternative 1:
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]  # Initialize an empty list to store the subsequence.

        for num in nums[1:]:
            # Find the index at which 'num' should be inserted in 'sub' using binary search.
            if num > sub[-1]:
                sub.append(num) # If 'num' should be inserted at the end of 'sub', simply append it.
            else:
                idx = bisect.bisect_left(sub, num)
                # idx = self.binarySearchInsertion(sub, num)
                sub[idx] = num  # If 'num' should replace an existing element in 'sub', update it.
        return len(sub)  # Return the length of the final LIS.



#Binary search- Alternative 2 with binary search implementation
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]  # Initialize an empty list to store the subsequence.

        for num in nums[1:]:
            # Find the index at which 'num' should be inserted in 'sub' using binary search.
            if num > sub[-1]:
                sub.append(num) # If 'num' should be inserted at the end of 'sub', simply append it.
            else:
                idx = self.binarySearchInsertion(sub, num)
                sub[idx] = num  # If 'num' should replace an existing element in 'sub', update it.
        return len(sub)  # Return the length of the final LIS.
    
    
    def binarySearchInsertion(self, sub, num):
        # Manually find the index where 'num' should be inserted into 'sub' using binary search.
        left, right = 0, len(sub) - 1
        
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the middle index.
            
            if sub[mid] < num:
                left = mid + 1
            else:
                right = mid - 1

        return left  # 'left' is the index where 'num' should be inserted.
