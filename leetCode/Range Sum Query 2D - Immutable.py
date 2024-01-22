"""
The algorithm uses a cumulative sum matrix to efficiently handle multiple queries of calculating the sum of elements within rectangles in a 2D matrix. 
The NumMatrix class is initialized with a cumulative sum matrix representing the sum of elements from the top-left corner to each cell. 

The sumRegion method then uses the precomputed cumulative sum values at the corners of the given rectangle to quickly calculate the sum of elements inside that rectangle. 

This approach improves query performance by avoiding redundant calculations for each query and is particularly effective for scenarios with frequent sum calculations on the same matrix.
"""

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.cumulative_sum = []
        else:
            m, n = len(matrix), len(matrix[0])
            self.cumulative_sum = [[0] * (n + 1) for _ in range(m + 1)]

            # Build the cumulative sum matrix
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    self.cumulative_sum[i][j] = (
                        matrix[i - 1][j - 1]
                        + self.cumulative_sum[i - 1][j]
                        + self.cumulative_sum[i][j - 1]
                        - self.cumulative_sum[i - 1][j - 1]
                    )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.cumulative_sum:
            return 0

        return (
            self.cumulative_sum[row2 + 1][col2 + 1]
            - self.cumulative_sum[row1][col2 + 1]
            - self.cumulative_sum[row2 + 1][col1]
            + self.cumulative_sum[row1][col1]
        )
