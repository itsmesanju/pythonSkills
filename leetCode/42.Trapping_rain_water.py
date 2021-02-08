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
