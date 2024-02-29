class Solution:
    def calculate(self, s: str) -> int:
        def update(op, val):
            if op == '+':
                stack.append(val)
            elif op == '-':
                stack.append(-val)
            elif op == '*':
                stack.append(val * stack.pop())
            elif op == '/':
                stack.append(int(stack.pop() / val))

        curr_val, op, stack = 0, '+', []
        for c in s:
            if c == ' ': continue
            elif c.isdigit():
                curr_val *= 10
                curr_val += int(c)
            elif c in ['+', '-', '*', '/', ')']:
                update(op, curr_val)
                if c == ')':
                    curr_val = 0
                    while isinstance(stack[-1], int):
                        curr_val += stack.pop()
                    op = stack.pop()
                    update(op, curr_val)
                
                curr_val, op = 0, c
            elif c == '(':
                stack.append(op)
                curr_val, op = 0, '+'

        update(op, curr_val)
        return sum(stack)        
