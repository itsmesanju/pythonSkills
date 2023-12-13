#Algo: There would be water on a bar only if there are taller bars both to left and right of it.
# tallest_to_left is initialized with a single element -1. This is done to handle the border case where there are no bars to the left.
# The variable curr_tallest is initialized with the first height in the list (height[0]). This variable keeps track of the tallest bar encountered so far.
# The code then iterates through the heights from the second one (height[1:]) and updates the tallest_to_left list. 
# For each height, it appends the current tallest height to the tallest_to_left list and updates curr_tallest if the current height is taller than the current tallest height.

# Similar steps are performed for the heights from right to left. tallest_to_right is initialized with a single element -1, 
# The loop iterates from the second-to-last height to the first height. It updates the tallest_to_right list in a manner similar to updating tallest_to_left.

# The tallest_to_right list is reversed to make it aligned properly with the original order of heights.
# The code then prints the two lists (tallest_to_left and tallest_to_right) for debugging purposes.
# The variable water_trapped is initialized to 0. This variable will be used to accumulate the total amount of trapped water.

# A loop iterates through the heights along with their indices. 
# For each height, it checks if the height is less than both the corresponding tallest height to the left and the tallest height to the right.

# If the current height is lower than both the tallest heights to the left and right, 
# the code calculates the amount of water that can be trapped at that position and adds it to the water_trapped variable. 
# The trapped water is calculated as the difference between the minimum of the tallest heights to the left and right and the current height.


class Solution:
 def trap(self, height: List[int]) -> int:
        print(height)
        tallest_to_left = [-1]# for border line case
        curr_tallest = height[0]

        for h in height[1:]:
            tallest_to_left.append(curr_tallest)
            curr_tallest = max(curr_tallest, h)
        
        tallest_to_right = [-1]
        curr_tallest = height[-1]

        for idx in range(len(height)-2, -1, -1):
            tallest_to_right.append(curr_tallest)
            curr_tallest = max(curr_tallest, height[idx])
        
        tallest_to_right = tallest_to_right[::-1]
        print(tallest_to_left, tallest_to_right )
        water_trapped = 0

        for idx, h in enumerate(height):
            if h < tallest_to_left[idx] and h < tallest_to_right[idx]:
                water_trapped += (min(tallest_to_left[idx], tallest_to_right[idx]) - h)
                print(f"Water trapped at idx {idx} is: {water_trapped} including previous one")
        return water_trapped
