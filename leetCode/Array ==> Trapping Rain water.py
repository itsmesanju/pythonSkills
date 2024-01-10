class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = 0, 0
        water = 0
        for i in range(len(height)):
            left_max = max(height[0:i+1])
            right_max = max(height[i:])
            water = water + min(left_max, right_max) - height[i]
        
        return water

class Solution:
 def trap(self, height: List[int]) -> int:
        left_index, left_sum, right_index, right_sum = 0, 0, 0, 0
        for i in height:
            left_index = max(i, left_index)
            left_sum += left_index
        for i in height[::-1]:
            right_index = max(i, right_index)
            right_sum += right_index


        array_height = max(height)
        return left_sum + right_sum - sum(height) - (array_height * len(height))
