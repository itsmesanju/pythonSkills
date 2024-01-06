class Solution:
    def rob(self, nums: List[int]) -> int:
        #Define the helper function
        def helper(nums):
            rob1, rob2 = 0, 0
            for houses in nums:
                temp = max (rob1 + houses, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        
        #Run the  helper function on array 2 times...
        #1st: Element 2nd onwareds till end
        #2nd: Elements upto 2nd last
        #The 3rd comparision nums[0] is used for cases when array size is 1
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
