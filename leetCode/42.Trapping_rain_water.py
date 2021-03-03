#Solution goes through each position and checks for max heights max_left and max_right of current position, then takes the minimum of the two max heights (if take max, then water will overflow) and subtract the max height potential from height[i] and add the amount of holdable water to ans.

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i in range(1,len(height)-1): 
            max_left = max(height[:i])
            max_right = max(height[i+1:])
            potential = min(max_left, max_right) - height[i]
            ans += max(0, potential) 
        return ans
#===================


class Solution:
    def trap(self, height: List[int]) -> int:
       rainWater = 0
       for i in range(1, len(height)-1):
          #print("I -> ", i)
          #print("Height :i -> ",height[:i], max(height[:i]))
          #print("Height i+1: -> ",height[i+1:], max(height[i+1:]))
          #print("Height[i] -> ",height[i])
          temp = min(max(height[:i]),max(height[i+1:])) - height[i]
          #print("Temp ->  ", temp)
          if temp > 0:
             rainWater+=temp
       return (rainWater)
