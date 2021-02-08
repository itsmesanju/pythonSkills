class Solution:
    def maxArea(self, height: List[int]) -> int:
        size=(len(height))
        maxWater=0
        p1 = 0
        p2 = size-1
        while (p1 < p2):
            print(p1,p2,maxWater)
            length = min(height[p1],height[p2])
            width = p2 -p1
            area = length * width
            maxWater=max(maxWater,area)
            #print(height[p1],height[p2])
            if (height[p1] <= height[p2]):
                #print("p1 increment")
                p1 += 1
            else:
                #print("p2 decrement")
                p2 -= 1
        return maxWater
