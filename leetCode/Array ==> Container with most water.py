#Comment: Worst complexity
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


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        size = (len(height))

        if size < 2:
            return 0
        
        max_area = 0
        width = 0
        length = 0
        left = 0
        right = size - 1

        print(left,right, max_area)
        while left < right:
            length = min(height[left], height[right])
            width = right - left
            max_area = max(length * width, max_area)
            if height[left] > height[right]:
                right = right -1
            else:
                left = left + 1
        return max_area
