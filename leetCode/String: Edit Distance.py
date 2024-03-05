class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def helper(i, j):
            # Base cases: if one of the strings is empty
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            # If the current characters match, move to the next characters
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                memo[(i, j)] = helper(i + 1, j + 1)
            else:
                # If characters don't match, we have three options:
                # 1. Insert a character
                # 2. Delete a character
                # 3. Substitute a character
                insert = 1 + helper(i, j + 1)
                delete = 1 + helper(i + 1, j)
                substitute = 1 + helper(i + 1, j + 1)
                memo[(i, j)] = min(insert, delete, substitute)

            return memo[(i, j)]

        return helper(0, 0)
