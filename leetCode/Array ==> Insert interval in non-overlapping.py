
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Everything that ends before  new interval starts and can be added to the solution

        Now either two things will happen:
        we are able to add new interval with no interuptions OR
        we add new interval and there is some mreging to do

        so we will figure out now what overlaps what by doing this
        for each i in intervals while the start of i'th interval <= newInterval.end
        startNewInterval = min(newIntervalStart, interval[i]Start)
        end would be same way but the max
        Now what we have done is compute what the newinterval is inclusive of overlaps

        """
        merged = []
        i, n = 0, len(intervals)

        # Add all intervals before the new interval
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        merged.append(newInterval)

        # Add remaining intervals
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged

#Time complexity:
#O(n)
#Space complexity:
#AO(1)
