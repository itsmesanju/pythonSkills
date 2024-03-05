class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diagsr = set()
        diagsl = set()
        board = [['.'] * n for _ in range(n)]

        def addToAns(b):
            temp = []
            for l in b:
                temp.append(''.join(l))
            ans.append(temp)

        def backtrack(i):
            if i >= n:
                addToAns(board)
                return
            for j in range(n):
                if j not in cols and i - j not in diagsr and j + i not in diagsl:
                    cols.add(j)
                    diagsr.add(i - j)
                    diagsl.add(j + i)
                    board[i][j] = 'Q'
                    backtrack(i + 1)
                    cols.remove(j)
                    diagsr.remove(i - j)
                    diagsl.remove(j + i)
                    board[i][j] = '.'
            return

        ans = []
        backtrack(0)
        return ans
