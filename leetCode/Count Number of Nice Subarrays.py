class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #convert all odd numbers to 1 and all even numbers to 0
        #now "count number of subarrays whose sum equals k "
        for i in range(len(nums)):
            if(nums[i]%2==1):
                nums[i]=1
            else:
                nums[i]=0

        prefix_sum = 0
        count = 0
        prefix_counts = Counter([0])  # Initialize with 0 to account for the prefix sum itself

        for num in nums:
            prefix_sum += num
            count += prefix_counts[prefix_sum - k]
            prefix_counts[prefix_sum] += 1

        return count

        """
        #In this version, two pointers (left and right) are used to maintain a sliding window. 
        #The odd_count variable keeps track of the number of odd elements within the window. 
        #The inner while loop adjusts the window size to meet the condition (odd_count <= k),
        # and the count is updated accordingly.
        
        left, right, odd_count, count = 0, 0, 0, 0

        while right < len(nums):
            if nums[right] % 2 == 1:
                odd_count += 1

            while odd_count > k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1

            count += right - left + 1
            right += 1

        return count
        """
