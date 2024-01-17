class MedianFinder:
    """
    To find the median from a data stream, we can use two heaps – 
    a max-heap to represent the left half of the numbers and a min-heap to represent the right half. 
    
    The idea is to keep the two heaps balanced such that the sizes differ at most by one. This allows easy access to the median.

    Using heaps (specifically a max-heap and a min-heap) in the implementation of finding the median from a data stream
    provides an efficient way to maintain the elements in a sorted order while allowing for constant time access to the median.

    """
    def __init__(self):
        self.max_heap = []  # max heap for the left half
        self.min_heap = []  # min heap for the right half

    def addNum(self, num: int) -> None:
        # Add the number to one of the heaps
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Balance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # Calculate and return the median
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0] / 1.0



#Alternate / Slow
import bisect

class MedianFinder:
    def __init__(self):
        self.sorted_nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.sorted_nums, num)

    def findMedian(self) -> float:
        n = len(self.sorted_nums)
        if n % 2 == 0:
            mid1 = n // 2 - 1
            mid2 = n // 2
            return (self.sorted_nums[mid1] + self.sorted_nums[mid2]) / 2.0
        else:
            return float(self.sorted_nums[n // 2])
