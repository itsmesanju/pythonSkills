"""
Perform binary research to find the smallest num.

Approach
set left and right pointers separately starting from two ends of num list.
set while loop with condition left < right
-- if mid is larger than right, move left pointer to mid + 1
-- else, move right pointer to mid
return the num with left pointer
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        print(nums, nums[right])
        return nums[right]
