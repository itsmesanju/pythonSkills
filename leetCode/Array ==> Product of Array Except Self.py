class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total_product = 1
        zero_count = 0

        result = []
        for num in nums:
            if num != 0:
                total_product = total_product * num
            else:
                zero_count = zero_count + 1

        #If there are more than 1 zeros. Entire result of array will be zero.
        if zero_count > 1:
            result = [0] * len(nums)

        # If there is one zero, all other elements in the result are zero except at the  index of the zero item
        if zero_count == 1:
            result = [0] * len(nums) #Make new array of same size filled with zero
            zero_index = nums.index(0)
            result[zero_index] = total_product

        # If no Zeroes
        if zero_count == 0:
            result = [total_product // num for num in nums]

        return result
