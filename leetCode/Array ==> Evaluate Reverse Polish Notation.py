class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        def operation(a,b, operation):
            result = 0
            match operation:
                case "*":
                    result = a * b
                case "+":
                    result = a + b
                case "-":
                    result = a - b
                case "/":
                    result = int(a / b)

            return result

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                print(f"Operands: {token}")
                stack.append(int(token))
            else:
                print(f"Operation: {token}")
                b = stack.pop()
                a = stack.pop()
                result = operation(a, b, token)
                stack.append(result)

        return stack[0]
