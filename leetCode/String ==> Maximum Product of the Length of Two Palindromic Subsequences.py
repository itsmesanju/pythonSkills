class Solution:
    def maxProduct(self, s: str) -> int:

            """

            It find the maximum product of the lengths of two palindromic substrings that can be formed from the input string.
             The method uses a recursive approach to generate all possible pairs of palindromic substrings and keeps track of the maximum product encountered.

            The function makes three recursive calls:
            dfs(i + 1, word + s[i], word2): Include the current character in the first substring.
            dfs(i + 1, word, word2 + s[i]): Include the current character in the second substring.
            dfs(i + 1, word, word2): Skip the current character.
            """
            self.answer = 0
            
            def dfs(i, word, word2):
                if i >= len(s):
                    if word == word[::-1] and word2 == word2[::-1]:
                        self.answer = max(len(word) * len(word2), self.answer)
                    return
                
                
                dfs(i + 1, word + s[i], word2)
                dfs(i + 1, word, word2 + s[i])
                dfs(i + 1, word, word2)
                
            dfs(0, '', '')
            
            return self.answer
