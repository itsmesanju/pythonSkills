class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = 0, 0
        water = 0
        for i in range(len(height)):
            left_max = max(height[0:i+1])
            right_max = max(height[i:])
            water = water + min(left_max, right_max) - height[i]
        
        return water
