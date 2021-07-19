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
