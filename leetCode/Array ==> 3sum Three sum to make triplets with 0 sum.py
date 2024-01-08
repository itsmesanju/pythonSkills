class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """
        We can use a two-pointer approach along with sorting the input array. 
        The idea is to fix one element and use two pointers to find the other two elements such that their sum is zero. 

        Sort the input array nums to simplify the process of finding triplets.
        Iterate through the array with a fixed element (nums[i]) using a for loop.
        Use two pointers (left and right) to find the other two elements such that their sum is equal to the negative of the fixed element.
        Skip duplicates to avoid duplicate triplets.
        If a triplet is found, append it to the result list.
        Continue the iteration until all possible triplets are considered.
        """
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            # Skip duplicates to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result
