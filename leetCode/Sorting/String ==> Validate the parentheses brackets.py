def is_well_formed(expression):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != closing_brackets[char]:
                return False

    # Check if the stack is empty at the end
    return not stack

# Example usage:
expression1 = "({[()]})"
expression2 = "({[()]}"
expression3 = "({[()]})}"

print(f"Expression 1 is well-formed: {is_well_formed(expression1)}")
print(f"Expression 2 is well-formed: {is_well_formed(expression2)}")
print(f"Expression 3 is well-formed: {is_well_formed(expression3)}")
