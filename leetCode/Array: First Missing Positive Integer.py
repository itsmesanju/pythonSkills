class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        e=len(nums)
        print(nums,e)
        for i in range(1,e+1):
            if i not in nums:
                return i
        return e+1
