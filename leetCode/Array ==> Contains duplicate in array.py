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



#Sort the array and check if two consecutive numbers are same.
    nums.sort()
    n = len(nums)
    for i in range(1,n):
        if nums[i] == nums[i-1]:
            return True
    return False

#Using hash map of checked items
        seen_set = set()
        for num in nums:
            if num in seen_set:
                return True
            seen_set.add(num)
        return False

