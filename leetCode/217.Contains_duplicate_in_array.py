#Brute force method:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            if nums.count(i) >= 2:
                return True
        return False


# Using set
   def containsDuplicate(self, nums: List[int]) -> bool
        return len(set(nums)) != len(nums)

