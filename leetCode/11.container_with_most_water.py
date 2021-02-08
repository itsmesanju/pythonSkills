class Solution:
    def maxArea(self, height: List[int]) -> int:
        size=(len(height))
        maxWater=0
        for x in range(0,size):
            for y in range(x+1, size):
                width = y-x
                length = min(height[x],height[y])
                temp = width * length
                #print(x,y,width,length,temp)
                if maxWater < temp:
                    maxWater = temp
        return maxWater
