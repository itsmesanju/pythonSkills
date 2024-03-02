class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        This algorithm iterates through the string, pushing the index of each '(' encountered onto the stack. When a ')' is encountered, it pops the top index from the stack. If the stack becomes empty, it means all previous parentheses are matched, so it pushes the current index onto the stack as a new base index. If the stack is not empty after popping, it calculates the length of the valid parentheses substring and updates the maximum length if necessary.

This approach runs in O(n) time complexity, where n is the length of the input string, because it only requires a single pass through the string.


        """
        stack = [-1]  # Initialize stack with -1 as the base index. Otherwise pop will error
        """
        if we encounter ')' at index 0, we can't directly calculate the length of the valid parentheses substring because there is no corresponding '(' to match it. 
        However, if we initialize the stack with -1, it acts as a reference point indicating the beginning of the string.
        """
        max_length = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # Push index of '(' onto the stack
            else:
                stack.pop()  # Pop the top index from the stack
                if len(stack) == 0:
                    stack.append(i)  # Push the current index if stack becomes empty
                else:
                    # Calculate the length of valid parentheses substring
                    max_length = max(max_length, i - stack[-1])  
        
        return max_length
