class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        """
        Put simply, if we detect a cycle, it is impossible to complete all the courses
        using DFS and maintaining a list called visited to keep track of visited nodes
        """
        adj_list = defaultdict(list)
        for course1, course2 in prerequisites:
            adj_list[course2].append(course1)


        def has_cycle(course):
            if visited[course] == 1:
                return True
            if visited[course] == -1:
                return False

            visited[course] = 1
            for neighbor in adj_list[course]:
                if has_cycle(neighbor):
                    return True
            visited[course] = -1
            return False

        visited = [0] * numCourses
        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True
