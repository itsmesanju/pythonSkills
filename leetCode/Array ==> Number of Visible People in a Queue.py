class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        For each person, iterate through the stack and increment the count for each shorter person, 
        as they can be seen by the current person.

        If the stack is not empty after step 1, increment the count for the person at the top of the 
        stack, as the current person is taller than them.

        Push the current index onto the stack.
        """
        stack = []
        ans = [0] * len(heights)

        for i in range(len(heights)):
            while stack and heights[i] > heights[stack[-1]]:
            # (2) getting rid of the shorter person
                ans[stack.pop()] += 1
            if stack:
            # (1) contributing to the taller person
                ans[stack[-1]] += 1
            stack.append(i)
        
        return ans
