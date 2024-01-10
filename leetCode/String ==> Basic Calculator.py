class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1
        result = 0

        """In the approach, the multiplication by 10 is employed to construct multi-digit numbers 
        while parsing the input string representing a mathematical expression. 
        
        As the algorithm iterates through the characters, encountering digits one by one, the 
        variable num is used to accumulate the value of the digits. By multiplying the existing 
        value of num by 10 and then adding the current digit, the algorithm ensures that it 
        correctly builds multi-digit numbers. This technique is crucial for accurately evaluating
        numeric expressions, where the order and value of digits contribute to the overall numerical result.
        
        The algorithm for evaluating a mathematical expression with basic arithmetic operations and 
        parentheses employs a stack and iterative parsing. It maintains variables such as num for the
        current number being constructed, sign to keep track of the current sign, and result as the 
        running total. The algorithm iterates through each character in the input string. For digits, 
        it accumulates the value into num using the multiplication by 10 technique. When encountering 
        operators '+', and '-', it updates the running total result based on the current num and sign, 
        resetting num to 0. For parentheses, it uses a stack to manage the state, pushing and popping 
        results and signs accordingly. The final result is the running total result after processing 
        the entire string. This approach ensures correct evaluation, handling order of operations and 
        nested expressions. The use of a stack facilitates proper handling of parentheses and maintains 
        the state during the iterative parsing of the expression.
"""

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += sign * num
                num = 0
                sign = 1
            elif char == '-':
                result += sign * num
                num = 0
                sign = -1
            elif char == '(':
                stack.append((result, sign))
                result, sign = 0, 1
            elif char == ')':
                print(stack)
                result += sign * num
                num = 0
                prev_result, prev_sign = stack.pop()
                result = prev_result + prev_sign * result

        return result + sign * num
