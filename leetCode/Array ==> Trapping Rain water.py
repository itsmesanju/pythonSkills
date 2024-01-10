#Solution goes through each position and checks for max heights max_left and max_right of current position, 
then takes the minimum of the two max heights (if take max, then water will overflow) and subtract the max height 
potential from height[i] and add the amount of holdable water to ans.

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i in range(1,len(height)-1): 
            max_left = max(height[:i])
            max_right = max(height[i+1:])
            potential = min(max_left, max_right) - height[i]
            ans += max(0, potential) 
        return ans

# This code uses a different approach by calculating the sum of maximum heights 
# encountered from the left and right separately and then subtracting the overlapping parts.
# The solution is "count twice", which means counting from left side once and from right side once.
# finally, to get the water area, we use left+right-whole area -black lines(arrats) to get the answer.

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

