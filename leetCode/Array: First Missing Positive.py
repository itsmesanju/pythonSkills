class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums) #Set is used to handle the large input. Otherswise we can directly check in nums array too.
        e=len(nums)
        for i in range(1,e+1):
            if i not in nums:
                return i
        return e+1
