class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        we can implement a solution for the job scheduling problem using dynamic programming. 
        The code uses a bottom-up approach to fill in the dp array, where each element dp[i] 
        represents the maximum profit starting from job i.

        This loop iterates in reverse order through the sorted jobs. 
        
        For each job i, it calculates two values:
            start_idx: The index of the first job whose end time is greater than or equal to the start time of job i.
            take: The maximum profit if we include the current job i. It is the sum of the profit of job i and the maximum profit starting from the job at index start_idx.
            leave: The maximum profit if we exclude the current job i. It is the maximum profit starting from the next job.

The dp[i] is then updated to be the maximum of take and leave.

        """
        data = list(zip(startTime, endTime, profit))
        data.sort()


        dp = [0] * (len(data) + 1)

        for i in range(len(data) - 1, -1, -1):
            start_idx = bisect_left(data, (data[i][1],))
            take = data[i][2] + dp[start_idx]
            leave = dp[i+1]
            dp[i] = max(take, leave)
                
        return dp[0]  
