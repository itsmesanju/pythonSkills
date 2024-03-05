class Solution:
  """
  Binary search
  """
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = left + (right-left)// 2 + 1
            print(mid)
            if mid * mid > x:
                right = mid -1
            else:
                left = mid
        return left
