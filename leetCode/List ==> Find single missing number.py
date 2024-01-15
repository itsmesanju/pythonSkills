#Approach 1: BruteForce
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i
            

    #use of set
#The missing number is the difference between the sum of the given list and its supposed value.
#The actual value can be calculated by multiplying the sum of all unique elements by two. (Two because each value repeats itself twice)

    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)
