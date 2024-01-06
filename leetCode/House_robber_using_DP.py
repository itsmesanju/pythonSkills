#Python DP
def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        #Dynamics programming
        #Assuming that 0 is the robbed amount from 2 more houses before... its to compare the values and add in
        # [ rob1, rob2, n, n+1, ..... n]
        for houses in nums:
            temp = max (rob1+ houses, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

#Odd even
class Solution:
     def rob(self, nums):
          
        odd = even = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                odd = max(even, odd + nums[i])
            else:
                even = max(odd, even + nums[i])
        return max(odd, even)
