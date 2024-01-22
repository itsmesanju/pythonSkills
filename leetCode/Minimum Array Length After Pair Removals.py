"""
The minLengthAfterRemovals algorithm finds the minimum length of an array after removing some elements. 

It identifies consecutive identical elements, calculates their maximum count, and determines the number of elements to be removed based on the comparison between distinct elements and the maximum consecutive count. 

The final count reflects the minimum length of the array after removals. The algorithm efficiently handles consecutive identical elements and distinct elements in the array.

"""

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        maximum = left = right = count = 0
        if nums[0] == nums[-1]:
            return len(nums)
        while left < len(nums):
            right = left + 1
            while right < len(nums) and nums[left] == nums[right]:
                right += 1
            temp = right - left
            if temp > 1: 
                maximum = max(maximum, temp)
            left = right
        distinct = len(nums) - maximum
        
        if distinct >= maximum:
            if len(nums) % 2: count += 1
        else:
            count += (maximum - distinct)
        return count
