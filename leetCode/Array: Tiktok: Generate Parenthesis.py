class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      """
      The algorithm systematically explores different combinations of parentheses using a breadth-first search (BFS) approach. It starts with an empty string and gradually builds valid combinations by adding either a left or a right parenthesis. At each step, it checks whether adding a parenthesis would result in a valid combination according to the rules of balanced parentheses:

      It ensures that the number of left parentheses (left) does not exceed n, the total number of pairs of parentheses allowed.
      It ensures that the number of right parentheses (right) does not exceed the number of left parentheses (left), as adding a right parenthesis only makes sense if there are corresponding left parentheses to match it.

      """
        result = []
        left = right = 0
        q = [(left, right, '')]
        while q:
            left, right, s = q.pop()
            if len(s) == 2 * n:
                result.append(s)
            if left < n:
                q.append((left + 1, right, s + '('))
            if right < left:
                q.append((left, right + 1, s + ')'))
        return result        
