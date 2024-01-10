class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sorts the intervals based on their start times in ascending order. 
        Initialize an empty list ans to store the merged intervals.
        Initialize start and end with the start and end times of the first interval in the sorted list.
        Iterate through the sorted intervals using a for loop:
            If the start time of the current interval is greater than the end time of the previous merged interval, it means a new non-overlapping interval starts. In this case:
            Append the previous merged interval [start, end] to the result list ans.
            Update start and end to the current interval's start and end times.

        If there is an overlap, update the end time to be the maximum of the current interval's end time and the existing end. This step effectively merges overlapping intervals.
        After the loop, append the last merged interval [start, end] to the result list.

        Return the final list of merged non-overlapping intervals stored in ans.
        """
        intervals = sorted(intervals)

        ans = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in intervals:
            if i[0] > end:
                ans.append([start, end])
                start, end = i[0], i[1]
            else:
                end = max(end, i[1])

        ans.append([start, end])
        return ans
