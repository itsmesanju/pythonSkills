'''This is very simple approach to solve this question. First of all, we are calculating the product of all "non-zero" numbers and based on count of zeros in the given array, the logic will define the o/p.

If there are more than 2 zeros, the resulting array will be all zeros because at any given time, one of the zero is part of the product.
If there are no zeros, we are deviding the product the the item of each index (in a way to determine the product of except).
If there is one zero, all other items will be zero except the 0th item in given array.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1    
        zero_counts=0
        
        for num in nums:
            if num != 0:
                total*=num
            else:
                zero_counts +=1
                
        if zero_counts > 1:
            return [0] * len(nums)
         
        elif zero_counts == 1:
            for index in range(len(nums)):
                if nums[index] == 0:
                    nums[index] = total
                else:
                    nums[index] = 0
            return nums
                    
        elif zero_counts == 0:
            for index in range(len(nums)):
                nums[index] = total//nums[index]
            
            return nums
