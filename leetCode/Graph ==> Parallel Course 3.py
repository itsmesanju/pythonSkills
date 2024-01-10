class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """
        The goal is to calculate the minimum time required to complete a set of tasks with dependencies.
        g = defaultdict(list): This defaultdict called g, where key has a default value of an empty list. 
        This dictionary will be used to represent a directed graph where the keys are tasks, and the values are lists of tasks that depend on the key task.

        This recursive function calculates the minimum time required to complete a task x. 
        It does this by recursively calling itself on each task that depends on task x and then adding the time required for task x itself. 

        This line calculates the maximum time among the minimum times required to complete each task from 1 to n. 
        It uses the map function to apply the min_time function to each task, and then takes the maximum value.
            
        """
        g = defaultdict(list)
        for pre, nxt in relations: 
            g[pre].append(nxt)

        @cache
        def min_time(x: int) -> int:

            return max(map(min_time, g[x]), default=0) + time[x - 1]

        return max(map(min_time, range(1, n + 1)))
