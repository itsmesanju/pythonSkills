#Python DP
class Solution:
     def rob(self, nums):
            if not nums:
                return 0

            if len(nums) <= 2: #handle the case of array is 1 or 2 items longs.
                return max(nums)

            dp = [0] * len(nums) #initialize a new array to hold the cummulative values
            dp[0] = nums[0] #copy first element as it to compare it with further
            dp[1] = max(nums[0], nums[1]) #compare the first two elements from nums array and choose the higher one to rob and place in 2nd index.

            #once two houses are determined to rob, run a loop on entire range to decide which houses to rob.

            for house in range(2,len(nums)): #starting from 3rd element to the entire range of array
                dp[house] = max(dp[house -1], nums[house] + dp [house -2])

            return dp[-1] #return last element updated from for loop which will have the highest robbed money
#Python NO EXTRA ARRAY

class Solution:
     def rob(self, nums):
            prev = 0
            curr = 0

            for num in nums:
                temp = prev
                prev = curr
                curr = max((num + temp), prev)

            return curr
