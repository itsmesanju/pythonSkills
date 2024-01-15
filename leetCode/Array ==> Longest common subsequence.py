#dynamic programming solution
#keep a table of dimensions (m+1) * (n+1) where m is length of t1, n = length of t2
#pad the matrix with 0s at left and top

#then iterate through the table from 1->m+1 and 1->n+1
#compare text1[i-1], text2[j-1]
#if same, then add 1 to table[i-1][j-1] and set that to table[i][j]
#otherwise, take the max of table[i-1][j] and table[i][j-1]
#update maximum length as you go


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        table = [[0 for j in range(n+1)] for i in range (m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])
        
        return table[m][n]
