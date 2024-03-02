class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Permutations: A permutation of a set is an arrangement of its elements. For example, the permutations of the set {1, 2, 3} are {1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2}, and {3, 2, 1}.

Lexicographic Order: In lexicographic order, sequences are ordered based on their dictionary order. For example, in lexicographic order, {1, 2, 3} comes before {1, 3, 2}, and {1, 3, 2} comes before {2, 1, 3}.

The process to find the next permutation involves the following steps:

        """
        # Step 1: Find the first element nums[i] such that nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # If no such element exists, the array is in descending order, return the reverse
        if i == -1:
            nums.reverse()
            return nums
        
        # Step 2: Find the smallest element nums[j] in the subarray nums[i+1:] such that nums[j] > nums[i]
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        
        # Step 3: Swap nums[i] with nums[j]
        nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the subarray nums[i+1:]
        nums[i+1:] = reversed(nums[i+1:])
        
        return nums
