class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ret=0
        for items in range(0,len(nums)+1):
            if items not in nums:
               return items
