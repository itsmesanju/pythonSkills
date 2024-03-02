class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #We can use binary search algorithm to find the starting and ending positions of a given target value in a sorted array of integers.
        """
binarySearchLeft function: This function finds the leftmost index of the target value in the array. It performs a binary search, updating the left and right pointers until the target value is found or the left pointer surpasses the right pointer.

binarySearchRight function: This function finds the rightmost index of the target value in the array. Similar to binarySearchLeft, it performs a binary search, updating the left and right pointers until the target value is found or the left pointer surpasses the right pointer.

Once both the leftmost and rightmost indices are found, we return them as the starting and ending positions of the target value in the array. If the target value is not found, we return [-1, -1].

        """

        def binarySearchLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def binarySearchRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left_index = binarySearchLeft(nums, target)
        right_index = binarySearchRight(nums, target)
        
        if left_index <= right_index:
            return [left_index, right_index]
        else:
            return [-1, -1]
