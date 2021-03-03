#Traverse throughout the list.
#Initialize a start array and run over elements.
#If start of the element is greater than the end of previous element:
#   Push the element as it is in answer/output array
#   Keep start and end as the inserted values.
#else
#   update the end with the max out of previous end or the element of current end.
#append the result into array and return in the end

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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
