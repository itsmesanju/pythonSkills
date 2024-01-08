#Nested loops
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            second_target = target - nums[i]
            for j in range (i+1, n):
                    if second_target == nums[j]:
                        return [i,j]



#Brute force using dictionary... 

class Solution:
    def twoSum(self, nums, target):
        values = dict()

        for i, val in enumerate(nums):
            complement = target - val

            if complement in values:
                return [values[complement], i]

            values[val] = i

        return []      
