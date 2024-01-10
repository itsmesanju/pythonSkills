class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
'''This is very simple approach to solve this question. First of all, we are calculating the product of all "non-zero" numbers and based on count of zeros in the given array, the logic will define the o/p.

If there are more than 2 zeros, the resulting array will be all zeros because at any given time, one of the zero is part of the product.
If there is one zero, all other items will be zero except the 0th item in given array.
If there are no zeros, we are deviding the product the the item of each index (in a way to determine the product of except).

'''
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
