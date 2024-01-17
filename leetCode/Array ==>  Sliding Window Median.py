class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        """
        The medianSlidingWindow method in this solution calculates the median for a sliding window of size k moving 
        through the input array nums. The algorithm uses a sorted window and maintains it efficiently using the bisect module.

        if we use inbuilt sorted function, it will be very slow.


        Iterate from k to the end of the input array (nums) using index i.
        Calculate the index of the element to be removed from the window (remove_index) using bisect.bisect_left.
        Remove the element at remove_index from the window.
        Insert the new element (nums[i]) into the sorted window using bisect.insort.
        Calculate the median of the updated window using get_median and append it to the result list.
        """
        import bisect

        result = []
        window = sorted(nums[:k])
        
        def get_median(window):
            n = len(window)
            if n % 2 == 0:
                return (window[n // 2 - 1] + window[n // 2]) / 2.0
            else:
                return window[n // 2]
        
        result.append(get_median(window))
        
        for i in range(k, len(nums)):
            remove_index = bisect.bisect_left(window, nums[i - k])
            window.pop(remove_index)
            bisect.insort(window, nums[i])
            result.append(get_median(window))
        
        return result
